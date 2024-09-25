import requests

match_id = None

def live_matches():
    global match_id

    live_events_url = "https://api.sofascore.com/api/v1/sport/football/events/live"


    headers = {
        'authority': 'api.sofascore.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'origin': 'https://www.sofascore.com',
        'referer': 'https://www.sofascore.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
    }


    response = requests.get(live_events_url, headers=headers)
    print("Live Events API Status Code:", response.status_code)


    if response.status_code == 200:
        live_events = response.json()


        match_input = input("Enter the match (e.g., Ladomyr vs Metalist 1925): ").strip().lower()


        match_found = False


        if 'events' in live_events:
            for event in live_events['events']:
                home_team = event['homeTeam']['name']
                away_team = event['awayTeam']['name']


                match_name = f"{home_team} vs {away_team}".lower()
                if match_name == match_input:
                    match_found = True
                    match_id = event['id']  # Get the event ID
                    match_time = event['status']['description']


                    print(f"Match found: {home_team} vs {away_team}")
                    # print(f"Match Time: {match_time}")
                    # print(f"Match ID: {match_id}")
                    break

            if not match_found:
                print(f"Match '{match_input}' not found.")
        else:
            print("No live events found.")
    else:
        print("Failed to retrieve live matches.")

def statistic():
    global match_id

    if match_id is None:
        print("No match selected or match ID is invalid.")
        return

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


    statistic_url = f'https://api.sofascore.com/api/v1/event/{match_id}/statistics'
    summary_url = f'https://api.sofascore.com/api/v1/event/{match_id}'


    response_statistics = requests.get(statistic_url, headers=headers)
    response_summary = requests.get(summary_url, headers=headers)

    print("Statistics API Status Code:", response_statistics.status_code)
    print("Summary API Status Code:", response_summary.status_code)


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
                    break  # Exit loop if found
            if stat_found:
                break

        if not stat_found:
            print(f"Statistic '{requested_stat}' not found.")
    else:
        print("No statistics available for this match.")


    if response_summary.status_code == 200:
        summary = response_summary.json()


        match_time = summary['event']['status']['description']
        home_score = summary['event']['homeScore']['current']
        away_score = summary['event']['awayScore']['current']

        print(f"Live Match Time: {match_time}")
        print(f"Score: {summary['event']['homeTeam']['name']} {home_score} - {away_score} {summary['event']['awayTeam']['name']}")

    else:
        print("Failed to retrieve match summary.")


live_matches()


statistic()
