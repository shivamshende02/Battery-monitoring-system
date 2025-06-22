import pandas as pd
import openpyxl
#get sheets into code

#sheet_names = pd.ExcelFile('D:\\TATA_Battery\\All.xlsx').sheet_names
def calculate_3(data):
    #all_data  = pd.read_excel('D:\\TATA_Battery\\All.xlsx',sheet_name =1)
    all_data = data
    results = []
    #45 days completed
    all_data['ChangeDate'] = pd.to_datetime(all_data['ChangeDate'])
    all_data['BatMFG2'] = pd.to_datetime(all_data['BatMFG2'])
    all_data['delta'] = (all_data['ChangeDate'] - all_data['BatMFG2']).dt.days
    #print(all_data['delta'])

    all_data['greaterthan_45'] = all_data['delta'] >= 45
    #print(all_data['greaterthan_45'])
    for index,row in all_data.iterrows():
        if row['greaterthan_45'] == True:
            results.append({'ProdNo':row['ProdNo'] , 'ChangeDate':row['ChangeDate'] , 'OldBattery':row['OldBattery'] , 'Delta_days':row['delta']})
                
            
    only_true_data = all_data[all_data['greaterthan_45']==True]
    #df = pd.DataFrame(only_true_data)

    #df.to_excel('Greater_45_old.xlsx',index=False)
    return results

#calculated_results_3 = calculate_3()


