import pandas as pd

def calculate_4(data1,data2):
    # Read the main data from the first sheet
    #all_data = pd.read_excel('D:\\TATA_Battery\\All.xlsx', sheet_name=0)
    all_data = data1
    # Read unique product numbers from the second sheet
    #Unique_prodno = pd.read_excel('D:\\TATA_Battery\\All.xlsx', sheet_name=1, usecols=['ProdNo'])
    Unique_prodno = data2['ProdNo']
    # Get unique product numbers as a list
    unique_prodnos = Unique_prodno.unique()

    results = []

    for prod_no in unique_prodnos:
        # Filter rows for the current product number
        filtered_rows = all_data[all_data['ProdNo'] == prod_no]
        filtered_rows['TimeDate'] = pd.to_datetime(filtered_rows['TimeDate'])

        if not filtered_rows.empty:
            # Find the time difference between max and min dates
            time_difference = (filtered_rows['TimeDate'].max() - filtered_rows['TimeDate'].min())
            
            # Append the results
            results.append({
                'ProdNo': prod_no,
                'VINNO': filtered_rows.iloc[0]['VINNO'],  # First VINNO corresponding to this ProdNo
                'InitialDate': filtered_rows['TimeDate'].min(),
                'ChangeDate': filtered_rows['TimeDate'].max(),
                'DaysOfDegradation': time_difference
            })

    # Convert results to a DataFrame
    #df = pd.DataFrame(results)

    # Save to an Excel file
    #df.to_excel('Degradation.xlsx', index=False)

    return results       

#calculated_results_4 = calculate_4()
