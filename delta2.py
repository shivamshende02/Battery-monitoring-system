import pandas as pd
import openpyxl

def calculate_2(data1,data2):
   # all_data_1  = pd.read_excel('D:\\TATA_Battery\\All.xlsx',sheet_name =1)
    all_data_1 = data1
    filtered_data = all_data_1.iloc[:, :3]
    filtered_data['ChangeDate'] = pd.to_datetime(all_data_1['ChangeDate'])
    #print(filtered_data)


    #all_data_2 = pd.read_excel('D:\\TATA_Battery\\All.xlsx',sheet_name =0)
    all_data_2 = data2

    #print(all_data_2.columns)
    row_to_add_1 = []
    row_to_add_2 = []

    for index, row in filtered_data.iterrows():
        filtered_data_2 = all_data_2[all_data_2['ProdNo']== row['ProdNo']] 
        for index,row_1 in filtered_data_2.iterrows():
            if(row_1['statusRemark'] == 'NOK'):
                row_to_add_1.append(row_1)
                flag = 1
                #print('{0} Was detected NOK at {1}'.format(row_1['ProdNo'],row_1['GateName']))
                break
        
    
    #print(row_to_add_1)
    df = pd.DataFrame(row_to_add_1)
    #df[['VINNO','OldBattery','GateName']].to_excel('Found_Nok_At_stage.xlsx',index=False)
    return row_to_add_1
                
#calculated_results_2 = calculate_2()
            
        
        
