# Twice MV Views Tracker

A project to track and analyze YouTube views for Twice's music videos.

## Overview

This project uses the YouTube API to fetch daily view counts for Twice's MVs and stores the data in Google Sheets. The data is visualized using Looker Studio.
YouTube API uses Video_ID stored in the google sheet doc which can be updated with new IDs for new releases as required.

## Project Structure

- `scripts/`: Python scripts for data collection and updating Google Sheets.
- `screenshots/`: Contains screenshots of the dashboard and other relevant visuals.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/twice-mv-views-tracker.git
    cd twice-mv-views-tracker
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Google Cloud credentials and YouTube API key.

## Usage

- Run `script.py` to fetch the latest views and update Google sheet:
    ```bash
    python scripts/fetch_views.py
    ```



## Dashboard

The Looker Studio dashboard provides visual insights into the view counts. Below are some screenshots of the dashboard:

### Screenshot 1: Google Sheet Datasheet
![Google Sheet Datasheet](screenshots/Screenshot1.png)

### Screenshot 2: Weekly Trend Graph
![Weekly Trend Graph](screenshots/Screenshot2.png)

### Screenshot 3: Views Distribution
![Views Distibution](screenshots/Screenshot3.png)

## Contribution

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
