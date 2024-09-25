

# url = f'https://api.sofascore.com/api/v1/event/12065790/'


import requests
from bs4 import BeautifulSoup
import json

# URL for the match details page
# url = "https://www.sofascore.com/football/match/fortaleza-corinthians/hOsvP#id:12378088"
# #
# # # Get the HTML page and status code
# response = requests.get(url)
# print("HTML Page Status Code:", response.status_code)
#
# # Parse the HTML
# soup = BeautifulSoup(response.text, "html.parser")

# Update headers to match expected API request structure
import requests

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

# Make a request to the API to get the match statistics
statistic_url = 'https://api.sofascore.com/api/v1/event/12065790/'
response_statistics = requests.get(statistic_url, headers=headers)
print("Statistics API Status Code:", response_statistics.status_code)

# Parse the JSON response
if response_statistics.status_code == 200:
    stats = response_statistics.json()

    # Check if 'statistics' key exists in the response
    if 'statistics' in stats and stats['statistics']:
        # Ask the user which statistic they want
        requested_stat = input("Enter the name of the statistic (e.g., Ball possession, Total shots, Fouls): ").strip()

        # Flag to check if the stat was found
        stat_found = False

        # Loop through the statistics in the JSON response
        for group in stats['statistics'][0]['groups']:
            for item in group['statisticsItems']:
                if item['name'].lower() == requested_stat.lower():
                    stat_found = True
                    home_value = item['home']
                    away_value = item['away']
                    print(f"{requested_stat}: Home - {home_value}, Away - {away_value}")
                    break  # Exit loop if found
            if stat_found:
                break

        if not stat_found:
            print(f"Statistic '{requested_stat}' not found.")
    else:
        print("No statistics available for this match.")
else:
    print("Failed to retrieve match statistics.")

