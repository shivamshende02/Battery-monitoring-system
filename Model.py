import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

#Load the dataset
#Write the logic of CSV data here

#sheet_names = pd.ExcelFile('D:\TATA_Battery').sheet_names

data = []


#Feature Engineering

#Calculate battery age at each stage in days (difference between battery manufacture date and stage event date)
# This gives us the battery's age when it's used at different stages.
data['battery_age_assembly'] = (pd.to_datetime(data['stage_date_assembly']) - pd.to_datetime(data['battery_manufacture_date'])).dt.days
data['battery_age_bdf'] = (pd.to_datetime(data['stage_data_bdf'])-pd.to_datetime(data['battery_manufacture_date'])).dt.days
data['battery_age_adf'] = (pd.to_datetime(data['stage_date_adf']) - pd.to_datetime(data['battery_manufacture_date'])).dt.days
data['battery_age_level2'] = (pd.to_datetime(data['stage_date_level2']) - pd.to_datetime(data['battery_manufacture_date'])).dt.days
data['battery_age_dispatch'] = (pd.to_datetime(data['stage_date_dispatch']) - pd.to_datetime(data['battery_manufacture_date'])).dt.days

#Create voltage deltas across different stages to observe how the battery voltage changes
# These deltas will help us detect any abnormal voltage drops.
data['voltage_delta_bdf'] = data['voltage_bdf'] - data['voltage_assembly']
data['voltage_delta_adf'] = data['voltage_adf'] - data['voltage_bdf']
data['voltage_delta_level2'] = data['voltage_level2'] - data['voltage_adf']
data['voltage_delta_dispatch'] = data['voltage_dispatch'] - data['voltage_level2']

#Create flags for potential issues based on the voltage values
#We can flag potential issues like human error, alternator issues, or insufficient initial charge.

#Flag for human error (voltage drops significantly right after ADF)
# small equpiments or ECU's in the car were left turn on
data['human_error_flag'] = np.where(data['voltage_delta_adf'] < -0.5, 1, 0)  # Significant drop threshold set at -0.5V

#Flag for alternator issue (voltage drop after Level 2)
#Car is not driven for the equivalent time/ enough time that the alternator regenrative can charge the battery
data['alternator_issue_flag'] = np.where(data['voltage_delta_dispatch'] < -0.5, 1, 0)

#Flag for insufficient initial charge (low voltage at assembly)
#maybe the battery was not fully charged i.e 13v at the begining of the process or can be a data input entry
data['low_initial_charge_flag'] = np.where(data['voltage_assembly'] < 12.4, 1, 0)

#Flag for normal operation (no significant voltage drop and no flags raised)
#We'll consider a case where all voltages are within a reasonable range and there are no significant drops.
#small changes or rather the battery is charged upto the sufficent voltage therfore green flag the battery is good to go
data['no_issue_flag'] = np.where(
    (data['voltage_assembly'] >= 12.7) & (data['voltage_assembly'] <= 13.0) &
    (data['voltage_bdf'] >=12.7) & (data['voltage_bdf'] <=13.0) &
    (data['voltage_adf'] >= 12.7) & (data['voltage_adf'] <= 13.0) &
    (data['voltage_level2'] >= 12.4) & (data['voltage_level2'] <= 13.0) &
    (data['voltage_dispatch'] >= 12.4) & (data['voltage_dispatch'] <= 13.0),1,0
)

#Define target labels for the possible reasons for battery discharge or normal operation
#This function will classify each row based on the flags we've created.

def classify_discharge_reason(row):
    if row['human_error_flag'] == 1:
        return 'Human Error'  # Significant voltage drop after ADF stage
    elif row['alternator_issue_flag'] == 1:
        return 'Alternator Issue'  # Voltage drop after Level 2 due to insufficient alternator charge
    elif row['low_initial_charge_flag'] == 1:
        return 'Low Initial Charge'  # Voltage was too low during assembly
    elif row['no_issue_flag'] == 1:
        return 'No Issue'  # All voltage levels are within the normal range
    else:
        return 'Unknown'  # Catch-all for any other issues that we haven't flagged

# Apply the classification to create a new target column
data['discharge_reason'] = data.apply(classify_discharge_reason, axis=1)

# Step 5: Prepare features for model training
# We'll use voltage deltas, battery age, and the issue flags as features for our model.

# Features to use in the model
features = ['voltage_delta_bdf','voltage_delta_adf', 'voltage_delta_level2', 'voltage_delta_dispatch',
            'battery_age_bdf','battery_age_assembly', 'battery_age_adf', 'battery_age_level2', 'battery_age_dispatch',
            'human_error_flag', 'alternator_issue_flag', 'low_initial_charge_flag', 'no_issue_flag']

X = data[features]  # Feature set
y = data['discharge_reason']  # Target label (reason for discharge)

# Step 6: Train-test split for validation
# Splitting the data into training and test sets to evaluate the model's performance.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 7: Train the model using RandomForestClassifier
# We're using a Random Forest model as it works well with categorical and numerical data and provides good interpretability.
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)  # Fit the model on the training data

# Step 8: Model Evaluation
# Predicting on the test set to evaluate model performance.
y_pred = model.predict(X_test)

# Display classification report to show precision, recall, and F1 score for each class.
print(classification_report(y_test, y_pred))



