import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import datetime
import pytz

CREDENTIALS_DATA = {
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your_python_service_accound_id.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
SPREADSHEET_ID = ''
API_KEY = ''

def authenticate_gspread():
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(CREDENTIALS_DATA)
    client = gspread.authorize(credentials)
    return client.open_by_key(SPREADSHEET_ID).sheet1

def get_view_count(youtube, video_id):
    request = youtube.videos().list(part='statistics', id=video_id)
    response = request.execute()
    items = response.get('items', [])
    if items:
        return int(items[0]['statistics']['viewCount'])
    return 0

def main():
    indian_timezone = pytz.timezone('Asia/Kolkata')
    current_date = datetime.datetime.now(indian_timezone).strftime('%Y-%m-%d %H:%M:%S')

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    worksheet = authenticate_gspread()

    video_ids = worksheet.row_values(3)[1:]
    view_counts = [get_view_count(youtube, video_id) for video_id in video_ids]

    all_data = worksheet.get_all_values()
    empty_row_index = next((i for i, row in enumerate(all_data[::-1], 1) if not any(cell.strip() for cell in row)), None)

    if empty_row_index is not None:
        data = [current_date] + view_counts
        worksheet.update(f'A{empty_row_index}:Z{empty_row_index}', [data])
    else:
        data = [current_date] + view_counts
        worksheet.append_row(data)

    print("Script executed successfully.")

if __name__ == '__main__':
    main()
