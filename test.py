import requests
import pandas as pd


url = 'https://api.github.com/repos/alvimokw/linkedin-network-visualizer/contents/finalresults.csv'
req = requests.get(url)

d = pd.read_csv(req)

print(d)
