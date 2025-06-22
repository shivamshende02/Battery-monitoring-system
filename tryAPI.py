import webbrowser
import requests
import os
import pandas as pd
def calt():
    header = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = "http://tmlpnewskc31137/SATAPI/WebService.asmx/GetOrgStructure"

    response = requests.post(url,json=None,headers=header)

    if response.status_code == 200:

        data = response.json()
        #print(type(data))
        #print(data["d"])
        df = pd.DataFrame(data['d'])
        df = df.drop('__type',axis=1)
        return df
        #print(df)
    else:
        print("Error:", response.status_code)
        print("Response content:", response.text) 
        with open('D:\\TATA_Battery\\templates\\error.html', 'w') as f:
            f.write(response.text)    
        webbrowser.open('file://' + os.path.realpath('D:\\TATA_Battery\\templates\\error.html'))
        # Check for additional error details