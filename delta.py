import pandas as pd
import openpyxl
#get sheets into code

def calculate_1(data):
    #sheet_names = pd.ExcelFile('D:\\TATA_Battery\\All.xlsx').sheet_names

    #all_data  = pd.read_excel('D:\\TATA_Battery\\All.xlsx',sheet_name =1)
    all_data = data
    results = []
    #45 days completed
    all_data['ChangeDate'] = pd.to_datetime(all_data['ChangeDate'])
    all_data['BatMFG1'] = pd.to_datetime(all_data['BatMFG1'])
    all_data['delta'] = (all_data['ChangeDate'] - all_data['BatMFG1']).dt.days
    #print(all_data['delta'])

    all_data['greaterthan_45'] = all_data['delta'] >= 45
    #print(all_data['greaterthan_45'])
    for index,row in all_data.iterrows():
        if row['greaterthan_45'] == True:
            results.append({'ProdNo':row['ProdNo'] , 'ChangeDate':row['ChangeDate']  , 'Delta_days':row['delta']})

        only_true_data = all_data[all_data['greaterthan_45']==True]
        
    #df = pd.DataFrame(all_data)
    

    #df.to_excel('Greater_45.xlsx',index=False)
    
    #print(type(results))
    return results



#calculated_results_1 = calculate_1()

