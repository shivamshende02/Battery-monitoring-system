#import subprocess
import warnings
warnings.filterwarnings("ignore")
from multiprocessing import Value
from pydoc import text
from turtle import title
import pandas as pd
import webbrowser
import os

print('Calculating the data....')
from allBatteryAPI import cala
from tryAPI import calt
df1,df2,df3 = cala()
df4 = calt()
#print(df1)
#print(df2.columns)
#print("\n\n\n")
#print(df1.columns)
#print("\n\n\n")



from delta import calculate_1
calculated_results_1 = calculate_1(df2)


from delta2 import calculate_2
calculated_results_2 = calculate_2(df2,df1)

#print('good')
#exit(0)

from delta_old import calculate_3
calculated_results_3 = calculate_3(df2)

#print('good')
#exit(0)

from Degradation import calculate_4
calculated_results_4 = calculate_4(df1,df2)

#print('good')
#exit(0)

from Stage_wise import calculate_5
calculated_results_5 = calculate_5(df1)

#print('good')
#exit(0)

from average import calculate_6
calculated_results_6 = calculate_6(df1,df3)
#print('good')
#exit()

def display_menu():
    print("Enter the following data you want to see:")
    print("1. New Battery Age")
    print("2. Old Battery Age")
    print("3. NOK at Stage")
    print("4. Degradation Period")
    print("5. Gate wise NOK")
    print("6. Average based on Gates")
    print("0. Exit")

def toHtml(data):
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    html_table = data.to_html(index=False)

    htmlstring = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data Table</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Data Table</h1>
        {html_table}
    </body>
    </html>
    """
    with open('D:\\TATA_Battery\\templates\\Data.html', 'w') as f:
        f.write(htmlstring)    
    webbrowser.open('file://' + os.path.realpath('D:\\TATA_Battery\\templates\\Data.html'))

def toHtmlchart(data):
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    GateName = data['GateName'].tolist()
    wAvg = data['Average_Volatage'].tolist()
    var2 = data['LimitVoltage'].tolist()    
    var3 = data['Average_SOC'].tolist()

    GateName = '["' + '"," '.join(map(str, GateName)) + '"]'
    wAvg = "[" + ", ".join(map(str, wAvg)) + "]"
    var2 = "[" + ", ".join(map(str, var2)) + "]"
    var3 = "[" + ", ".join(map(str, var3)) + "]"

    

    with open('templates\\htmlTemplate.txt', 'r') as template_file:
        template = template_file.read()

        template = template.replace('@@GateNames@@', GateName)
        template = template.replace('@@AverageVoltage@@', wAvg)
        template = template.replace('@@LimitVoltage@@', var2)
        template = template.replace('@@AverageSOC@@', var3)

        with open('templates\\index.html', 'w') as output_file:
            output_file.write(template)

        webbrowser.open('file://' + os.path.realpath('D:\\TATA_Battery\\templates\\index.html'))
        


def main():

    while True:
        display_menu()
        try:
            choice = int(input("Enter the Option: "))
            if choice == 0:
                print("Exiting the program.")
                break
            elif choice == 1:
                #print(calculated_results_1)
                toHtml(calculated_results_1)
            elif choice == 3:
                ##print(calculated_results_3)
                 toHtml(calculated_results_2)  
            elif choice== 2:
                #print(calculated_results_2)
                toHtml(calculated_results_3)
            elif choice == 4:
                #print(calculated_results_4)
                toHtml(calculated_results_4)
            elif choice == 5:
                #print(calculated_results_5)
                toHtml(calculated_results_5)
            elif choice == 6:
                #print(calculated_results_6)
                
                toHtmlchart(calculated_results_6)    
            else:
                print("Invalid choice. Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        print("\n\n\n")
if __name__ == "__main__":
    main()
