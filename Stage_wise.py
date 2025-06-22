import pandas as pd

def calculate_5(data):
    #all_data = pd.read_excel('D:\\TATA_Battery\\All.xlsx',sheet_name=0)
    all_data = data

    #print(all_data.columns)

    unique_prodno = all_data['ProdNo'].unique()

    filtered_data = all_data[(all_data['Gateno'] > 10) | (all_data['Gateno'] != 50)]

    results = []

    for prod_no in unique_prodno:
        prod_data = filtered_data[filtered_data['ProdNo'] == prod_no]

        if 200 in prod_data['Gateno'].values:
            gate_200_row = prod_data[prod_data['Gateno'] == 200].iloc[0]
            min_gate_row = prod_data.loc[prod_data['Gateno'].idxmin()]

            gate_200_row['TimeDate'] = pd.to_datetime(gate_200_row['TimeDate'])
            min_gate_row['TimeDate'] = pd.to_datetime(min_gate_row['TimeDate'])

            delta_time = (gate_200_row['TimeDate'] - min_gate_row['TimeDate']).days
            delta_voltage = gate_200_row['Voltage'] - min_gate_row['Voltage']
            delta_soc = gate_200_row['SOC'] - min_gate_row['SOC']
            if delta_time != 0:
                ratio = delta_voltage / delta_time
                results.append({
                    'ProdNo': prod_no,
                    'GateNo': gate_200_row['Gateno'],
                    'VINNO': gate_200_row['VINNO'],
                    'TimeDate':gate_200_row['TimeDate'],
                    'TimeDate1':min_gate_row['TimeDate'],
                    'Voltage':gate_200_row['Voltage'],
                    'Voltage1':min_gate_row['Voltage'],
                    'SOC':gate_200_row['SOC'],
                    'SOC1':min_gate_row['SOC'],
                    'delta_time':delta_time,
                    'delta_voltage': delta_voltage,
                    'delta_SOC':delta_soc,
                    'Ratio': ratio
                })

        if 80 in prod_data['Gateno'].values:
            gate_80_row = prod_data[prod_data['Gateno'] == 80].iloc[0]
            min_gate_row = prod_data.loc[prod_data['Gateno'].idxmin()]
            gate_80_row['TimeDate'] = pd.to_datetime(gate_80_row['TimeDate'], errors='coerce')
            min_gate_row['TimeDate'] = pd.to_datetime(min_gate_row['TimeDate'], errors='coerce')


            delta_time = (gate_80_row['TimeDate'] - min_gate_row['TimeDate']).days
            delta_voltage = gate_80_row['Voltage'] - min_gate_row['Voltage']
            delta_soc = gate_80_row['SOC'] - min_gate_row['SOC']
            if delta_time != 0:
                ratio = delta_voltage / delta_time
                results.append({
                    'ProdNo': prod_no,
                    'GateNo': gate_80_row['Gateno'],
                    'VINNO': gate_80_row['VINNO'],
                    'TimeDate':gate_80_row['TimeDate'],
                    'TimeDate1':min_gate_row['TimeDate'],
                    'Voltage':gate_80_row['Voltage'],
                    'Voltage1':min_gate_row['Voltage'],
                    'SOC':gate_80_row['SOC'],
                    'SOC1':min_gate_row['SOC'],
                    'delta_time':delta_time,
                    'delta_voltage': delta_voltage,
                    'delta_SOC':delta_soc,
                    'Ratio': ratio
                }) 
        if 70 in prod_data['Gateno'].values:
            gate_70_rows = prod_data[prod_data['Gateno'] == 70]
            latest_gate_70_row = gate_70_rows.loc[gate_70_rows['TimeDate'].idxmax()]

            latest_gate_70_row['TimeDate'] = pd.to_datetime(latest_gate_70_row['TimeDate'])
            min_gate_row['TimeDate'] = pd.to_datetime(min_gate_row['TimeDate'])

            min_gate_row = prod_data.loc[prod_data['Gateno'].idxmin()]

            latest_gate_70_row['TimeDate'] = pd.to_datetime(latest_gate_70_row['TimeDate'])
            min_gate_row['TimeDate'] = pd.to_datetime(min_gate_row['TimeDate'])

            delta_time = (latest_gate_70_row['TimeDate'] - min_gate_row['TimeDate']).days
            delta_voltage = latest_gate_70_row['Voltage'] - min_gate_row['Voltage']
            delta_soc = latest_gate_70_row['SOC'] - min_gate_row['SOC']
            if delta_time != 0:
                ratio = delta_voltage / delta_time 
                results.append({
                    'ProdNo': prod_no,
                    'GateNo': latest_gate_70_row['Gateno'],
                    'VINNO': latest_gate_70_row['VINNO'],
                    'TimeDate':latest_gate_70_row['TimeDate'],
                    'TimeDate1':min_gate_row['TimeDate'],
                    'Voltage':latest_gate_70_row['Voltage'],
                    'Voltage1':min_gate_row['Voltage'],
                    'SOC':latest_gate_70_row['SOC'],
                    'SOC1':min_gate_row['SOC'],
                    'delta_time':delta_time,
                    'delta_voltage': delta_voltage,
                    'delta_SOC':delta_soc,
                    'Ratio': ratio
                }) 

    #print(results)
    #results_df = pd.DataFrame(results)
    #results_df.to_excel('Stage_wise.xlsx', index=False)  
    return results


#calculated_results_5 = calculate_5()
