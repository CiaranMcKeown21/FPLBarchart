import json
import requests
import pandas as pd
#https://app.flourish.studio/@flourish/bar-chart-race

leagueId = input("Enter League Id: e.g. 258305")
# print("League Id is: " + leagueId)
api_url = (f"https://fantasy.premierleague.com/api/leagues-classic/{leagueId}/standings")
print(api_url)

#Get List of managers in a league
# api_url = ("https://fantasy.premierleague.com/api/leagues-classic/258305/standings")
response = requests.get(api_url).json()

league_managers = dict()
manager_points = dict()
manager_names = []
data = []
for item in response['standings']['results']:
    managerId = item['entry']
    managerName = item['player_name']
    league_managers[managerId] = managerName
print(league_managers)


for id, manager in league_managers.items():
    players_api_url = f"https://fantasy.premierleague.com/api/entry/{id}/history/"
    playersResponse = requests.get(players_api_url).json()
    manager_dict = dict()
    manager_names.append(manager)
    for gameweek in playersResponse['current']:
        event = gameweek['event']
        total_points = gameweek['total_points']
        manager_dict[event] = total_points
    data.append(manager_dict)

print(data)
print(manager_names)
df = pd.DataFrame(data)
df.insert(0, 'Manager', manager_names)
df.to_csv('fpl_data_flourish.csv', index = False)




       