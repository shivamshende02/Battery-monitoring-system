from datetime import datetime
import webbrowser
import requests
import os
import pandas as pd

def cala():
    header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    url = "http://tmlpnewskc31137/SATAPI/WebService.asmx/getAllBatteryData"


    payload = {
            "sdate": '2024-10-01',  
            "edate": '2024-10-31',
            
        }
    response = requests.post(url,json=payload,headers=header);

    if response.status_code == 200:    
                        data = response.json()
                        #print(type(data))
                        
                        
                        df1 = pd.DataFrame(data['d']['bsList'])
                        df2 = pd.DataFrame(data['d']['bcList'])
                        df3 = pd.DataFrame(data['d']['bgList'])
                        #print(df3)
                        #print("\n\n")
                        #print(df1)
                        #exit()
                        

                        return df1,df2,df3

                        #print(df1)
    else:
            print("Error:", response.status_code)
            print("Response content:", response.text) 
            with open('D:\\TATA_Battery\\templates\\error.html', 'w') as f:
                f.write(response.text)    
            webbrowser.open('file://' + os.path.realpath('D:\\TATA_Battery\\templates\\error.html'))    
