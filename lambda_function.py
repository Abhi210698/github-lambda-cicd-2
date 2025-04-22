import json
import requests
import pandas as pd

def lambda_handler(event, context):
    print('Event Data', event)
    response = requests.get('https://www.usvisascheduling.com/')
    print(response.text)

    d = {'col 1' : [1,2], 'col 2' : [3.4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')