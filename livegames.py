import requests
import json

# Define the URL for fetching all live events (current games)
live_events_url = "https://api.sofascore.com/api/v1/sport/football/events/live"

# Set up headers for the request
headers = {
    'authority': 'api.sofascore.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'if-none-match': 'W/"4bebed6144"',
    'origin': 'https://www.sofascore.com',
    'referer': 'https://www.sofascore.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

# Make the request to get live football events
response = requests.get(live_events_url, headers=headers)
print("Live Events API Status Code:", response.status_code)

# Check if the request was successful
if response.status_code == 200:
    live_events = response.json()

    if 'events' in live_events:
        for event in live_events['events']:
            home_team = event['homeTeam']['name']
            away_team = event['awayTeam']['name']
            home_score = event['homeScore']['current']
            away_score = event['awayScore']['current']

            # Display the match information
            print(f"{home_team} vs {away_team}: {home_score} - {away_score}")
    else:
        print("No live events found.")
else:
    print("Failed to retrieve live matches.")
# TNG Thai Nguyen U19 vs Phong Phu Ha Nam U19