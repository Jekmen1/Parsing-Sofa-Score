list = [
    'Ball possession',
    'Big chances',
    'Total shots',
    'Goalkeeper saves',
    'Corner kicks',
    'Fouls',
    'Passes',
    'Tackles',
    'Free kicks',
    'Yellow cards',
    'Total shots',
    'Shots on target',
    'Hit woodwork',
    'Shots off target',
    ]


import requests
from bs4 import BeautifulSoup
import json

url = "https://www.sofascore.com/football/match/fortaleza-corinthians/hOsvP#id:12378088"

response = requests.get(url)
print("HTML Page Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

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
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

statistic_url = 'https://api.sofascore.com/api/v1/event/12702525/statistics'
response_statistics = requests.get(statistic_url, headers=headers)
print("Statistics API Status Code:", response_statistics.status_code)

if response_statistics.status_code == 200:
    stats = response_statistics.json()

    requested_stat = input("Enter the name of the statistic (e.g., Ball possession, Total shots, Fouls): ").strip()

    stat_found = False

    for group in stats['statistics'][0]['groups']:
        for item in group['statisticsItems']:
            if item['name'].lower() == requested_stat.lower():
                stat_found = True
                home_value = item['home']
                away_value = item['away']
                print(f"{requested_stat}: Home - {home_value}, Away - {away_value}")
                break  
        if stat_found:
            break

    if not stat_found:
        print(f"Statistic '{requested_stat}' not found.")
else:
    print("Failed to retrieve match statistics.")
