import requests
import pandas as pd
import requests

# All urls are from mlb.com/stats they are just different pages
url1 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=0&sortStat=onBasePlusSlugging&order=desc"
url2 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=25&sortStat=onBasePlusSlugging&order=desc"
url3 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=50&sortStat=onBasePlusSlugging&order=desc"
url4 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=75&sortStat=onBasePlusSlugging&order=desc"
url5 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=100&sortStat=onBasePlusSlugging&order=desc"
url6 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=125&sortStat=onBasePlusSlugging&order=desc"
url7 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=150&sortStat=onBasePlusSlugging&order=desc"
url8 = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2024&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=175&sortStat=onBasePlusSlugging&order=desc"

payload = {}
headers = {
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'Referer': 'https://www.mlb.com/',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"'
}

# Sets up array of URL's to get every MLB Player currently
myArray = []
myArray.append(url1)
myArray.append(url2)
myArray.append(url3)
myArray.append(url4)
myArray.append(url5)
myArray.append(url6)
myArray.append(url7)
myArray.append(url8)

# Variables that will be used to store the data from the website
dfAct = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()

# While loop to find the right names from the website
while df1.empty or df2.empty:
    # Input needed to search through the site for ball player
    # EX: input = "Mookie Betts"
    playerName1 = input("Please enter first player name: ")
    playerName2 = input("Please enter second player name: ")

    for array in myArray:
        # gets the reponse from the sites above
        response = requests.get(array, headers=headers)

        # turns json response into another file
        playerdata = response.json()

        df = pd.json_normalize(playerdata['stats'])

        dfAct = dfAct.append(df, ignore_index = True)

    # Finds both names for two different data frame.
    # If one is empty then the user needs to put the name in again.
    df1 = dfAct.loc[dfAct['playerName'] == playerName1]
    if df1.empty:
        print('The first players name could not be found.')
        print('Please input both names again.')

    df2 = dfAct.loc[dfAct['playerName'] == playerName2]
    if df2.empty:
        print('The second players name could not be found.')
        print('Please input both names again.')

# Puts two data frames into one data frame then prints them to show both players selected
df3 = pd.concat([df1, df2], ignore_index = True)
print(df3)

# converting to csv sheet that can be viewed in Microsoft XL.
df3.to_csv('playerdata.csv', index=False)
