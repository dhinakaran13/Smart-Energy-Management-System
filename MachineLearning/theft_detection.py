import warnings
warnings.filterwarnings("ignore",category=UserWarning)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 1. Load data
df = pd.read_csv("08_theft_inspection.csv")
df = df.dropna().drop_duplicates()

# Convert flags to int
df['Meter_Tamper_Flag'] = df['Meter_Tamper_Flag'].astype(int)
df['Voltage_Anomaly'] = df['Voltage_Anomaly'].astype(int)
df['Current_Anomaly'] = df['Current_Anomaly'].astype(int)

# 2. Train-Test Split
X = df[['Avg_Last6Months', 'Current_Month_Units', 'Consumption_Drop_Percentage',
        'Voltage_Anomaly', 'Current_Anomaly', 'Meter_Tamper_Flag', 
        'Night_Usage_Ratio','Transformer_Loss_Percentage']]
y = df['Theft_Flag']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 3. Model Training
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 4. Model Evaluation
y_pred = rf_model.predict(X_test)

print("=== MODEL EVALUATION METRICS ===")
print("Accuracy   :", accuracy_score(y_test, y_pred))
print("Precision  :", precision_score(y_test, y_pred))
print("Recall     :", recall_score(y_test, y_pred))
print("F1-Score   :", f1_score(y_test, y_pred))

# 5. Confusion Matrix Visualization
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Normal', 'Theft'], yticklabels=['Normal', 'Theft'])
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix')
plt.show()

# ==============================================================================
# 6. MANUAL INPUT TESTING BLOCK 
# ==============================================================================
print("\n" + "="*50)
print("             MANUAL THEFT PREDICTION SYSTEM            ")
print("="*50)

try:
    avg_6m = float(input("Enter Avg Last 6 Months Units (e.g., 500): "))
    curr_units = float(input("Enter Current Month Units (e.g., 200): "))
    drop_pct=float(input("Enter Consumption Drop Percentage(e.g.,60):"))
    volt_anom = int(input("Voltage Anomaly? (1 for Yes, 0 for No): "))
    curr_anom = int(input("Current Anomaly? (1 for Yes, 0 for No): "))
    tamper_flg = int(input("Meter Tamper Flag? (1 for Yes, 0 for No): "))
    night_ratio = float(input("Enter Night Usage Ratio (e.g., 0.75): "))
    trans_loss=float(input("Enter Transformer Loss Percentage(e.g.,25):"))
    
    user_features = pd.DataFrame([[avg_6m, curr_units,drop_pct, volt_anom, curr_anom, tamper_flg, night_ratio,trans_loss]])

    prediction = rf_model.predict(user_features)[0]
    probability = rf_model.predict_proba(user_features)[0][1]
    risk_score = int(probability * 100)

    if risk_score <= 30:
        risk_cat = 'Low Risk'
    elif risk_score <= 60:
        risk_cat = 'Medium Risk'
    else:
        risk_cat = 'High Risk'

    print("\n" + "-"*40)
    print("                PREDICTION RESULT               ")
    print("-"*40)
    print(f"Calculated Risk Score : {risk_score} / 100")
    print(f"Risk Status           : {risk_cat}")
    
    if prediction == 1:
        print("Final Verdict         : ⚠️ ALERT! SUSPECTED POWER THEFT DETECTED!")
    else:
        print("Final Verdict         : ✅ NORMAL CONSUMPTION PATTERN")
    print("-"*40)

except ValueError:
    print("\n❌ Invalid Input! Please enter numbers correctly.")
