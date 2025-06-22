import pandas as pd

def calculate_6(data1,data2):
    all_data = data1
    #gateid = data2
    #print(data1)
    #print(data2)

    result = []

    for index, row in data2.iterrows():
                #print(row)
                #exit()
                gate_rows = all_data[all_data['Gateno'] == row['GateId']]
                
                if not gate_rows.empty:
                    average_voltage = gate_rows['Voltage'].mean()
                    average_SOC = gate_rows['SOC'].mean()
                   

                    

                    result.append({
                        'GateId': row['GateId'],
                        'GateName': row['GateName'],
                        'LimitVoltage': row['LimitVoltage'],
                        'Average_Volatage': average_voltage,
                        'Average_SOC':average_SOC

                    })
    
    return result
        


