import pandas as pd
import numpy as np
import base64
from datetime import datetime, timedelta

print("🔄 8 Datasets are being prepared... Please wait for a moment...")
np.random.seed(42)

# ==========================================
# 1. CONSUMERS DATASET
# ==========================================
num_consumers = 2000
consumer_ids = [f"CON{i:05d}" for i in range(1, num_consumers + 1)]
c_types = np.random.choice(['Residential', 'Commercial', 'Industrial', 'Agricultural'], size=num_consumers, p=[0.60, 0.25, 0.10, 0.05])
tariff_map = {'Residential': 'Tariff IA', 'Commercial': 'Tariff V', 'Industrial': 'Tariff III', 'Agricultural': 'Tariff IV'}

df_consumers = pd.DataFrame({
    'Consumer_ID': consumer_ids,
    'Consumer_Name': [f"Consumer_{i}" for i in range(1, num_consumers + 1)],
    'Consumer_Type': c_types,
    'Tariff': [tariff_map[t] for t in c_types],
    'Area': np.random.choice(['Adyar', 'Velachery', 'Anna Nagar', 'Peelamedu', 'KK Nagar'], size=num_consumers),
    'District': np.random.choice(['Chennai', 'Coimbatore', 'Madurai'], size=num_consumers),
    'Meter_Type': np.random.choice(['Smart Meter', 'Digital Meter', 'Analog Meter'], size=num_consumers),
    'Connection_Date': ['2024-01-01'] * num_consumers,
    'Sanctioned_Load_KW': np.random.uniform(1, 60, num_consumers).round(2),
    'Phase_Type': np.random.choice(['Single Phase', 'Three Phase'], size=num_consumers),
    'Status': ['Active'] * num_consumers
})

# ==========================================
# 2 & 3. METER READINGS & BILLING DATASETS (Time-Series)
# ==========================================
months = [datetime(2025, 1, 1) + timedelta(days=31 * i) for i in range(12)] 
r_ids, b_ids, r_c_ids, r_dates, r_units, r_volt, r_curr, r_pf, r_status = [], [], [], [], [], [], [], [], []
b_months, b_amts, b_due, b_pay_status, b_arrears = [], [], [], [], []

counter = 1
for idx, c_id in enumerate(consumer_ids):
    c_type = c_types[idx]
    base_units = 150 if c_type=='Residential' else 600 if c_type=='Commercial' else 4000 if c_type=='Industrial' else 50
    
    for m in months:
        r_ids.append(f"RD{counter:07d}")
        b_ids.append(f"BL{counter:07d}")
        r_c_ids.append(c_id)
        r_dates.append(m.strftime('%Y-%m-%d'))
        
        units = int(np.random.normal(base_units, base_units*0.2))
        units = max(10, units)
        if idx % 14 == 0 and m >= datetime(2025, 6, 1):
            units = int(units * 0.3)
            m_status = 'Tampered'
            pf = round(np.random.uniform(0.65, 0.80), 2)
        else:
            m_status = 'Normal'
            pf = round(np.random.uniform(0.85, 0.98), 2)
            
        r_units.append(units)
        r_volt.append(round(np.random.normal(230, 8), 1))
        r_curr.append(round((units / 30) / (7.3 * pf), 2))
        r_pf.append(pf)
        r_status.append(m_status)
        
        rate = 4.5 if c_type=='Residential' else 7.5 if c_type=='Commercial' else 9.5 if c_type=='Industrial' else 0.5
        amt = round(units * rate, 2)
        b_months.append(m.strftime('%B %Y'))
        b_amts.append(amt)
        b_due.append((m + timedelta(days=20)).strftime('%Y-%m-%d'))
        p_stat = np.random.choice(['Paid', 'Unpaid'], p=[0.9, 0.1])
        b_pay_status.append(p_stat)
        b_arrears.append(0.0 if p_stat=='Paid' else amt)
        counter += 1

df_readings = pd.DataFrame({'Reading_ID': r_ids, 'Consumer_ID': r_c_ids, 'Reading_Date': r_dates, 'Units_Consumed': r_units, 'Voltage': r_volt, 'Current': r_curr, 'Power_Factor': r_pf, 'Meter_Status': r_status})
df_billing = pd.DataFrame({'Bill_ID': b_ids, 'Consumer_ID': r_c_ids, 'Billing_Month': b_months, 'Units': r_units, 'Amount': b_amts, 'Due_Date': b_due, 'Payment_Status': b_pay_status, 'Arrear_Amount': b_arrears})

# ==========================================
# 4 & 6. TRANSFORMERS & FEEDERS
# ==========================================
num_feeders = 50
feeder_ids = [f"FDR{i:03d}" for i in range(1, num_feeders + 1)]
df_feeders = pd.DataFrame({'Feeder_ID': feeder_ids, 'Feeder_Name': [f"Feeder_Line_{i}" for i in range(1, num_feeders + 1)], 'Substation': np.random.choice(['SS_Chennai_1', 'SS_Madurai_2', 'SS_Covai_1'], size=num_feeders), 'Area': np.random.choice(['Adyar', 'Velachery', 'Anna Nagar'], size=num_feeders), 'Capacity_MW': np.random.choice([5, 10, 15], size=num_feeders)})

num_transformers = 100
transformer_ids = [f"TX{i:04d}" for i in range(1, num_transformers + 1)]
df_transformers = pd.DataFrame({'Transformer_ID': transformer_ids, 'Feeder_ID': np.random.choice(feeder_ids, size=num_transformers), 'Location': np.random.choice(['Adyar', 'Velachery', 'Anna Nagar'], size=num_transformers), 'Capacity_KVA': np.random.choice([100, 250, 500], size=num_transformers), 'Installed_Date': ['2023-05-10'] * num_transformers, 'Status': ['Healthy'] * num_transformers})

# ==========================================
# 5. TRANSFORMER LOAD MONITORING
# ==========================================
num_load = 15000
df_tx_load = pd.DataFrame({'Load_ID': [f"LD{i:06d}" for i in range(1, num_load+1)], 'Transformer_ID': np.random.choice(transformer_ids, size=num_load), 'Date_Time': ['2026-04-01 12:00:00'] * num_load, 'Load_KW': np.random.uniform(40, 400, num_load).round(2), 'Voltage': np.random.uniform(400, 430, num_load).round(1), 'Temperature': np.random.uniform(45, 85, num_load).round(1), 'Utilization_Percentage': np.random.uniform(40, 95, num_load).round(2)})

# ==========================================
# 7. OUTAGE LOGS
# ==========================================
num_outages = 2000
df_outages = pd.DataFrame({'Outage_ID': [f"OUT{i:05d}" for i in range(1, num_outages+1)], 'Feeder_ID': np.random.choice(feeder_ids, size=num_outages), 'Start_Time': ['2026-03-15 10:00:00'] * num_outages, 'End_Time': ['2026-03-15 11:15:00'] * num_outages, 'Duration_Minutes': np.random.randint(15, 180, num_outages), 'Cause': np.random.choice(['Line Fault', 'Equipment Failure', 'Weather'], size=num_outages), 'Area': np.random.choice(['Adyar', 'Velachery', 'Anna Nagar'], size=num_outages)})

# ==========================================
# 8. THEFT INSPECTION DATASET (FIXED FOR REALISTIC ML METRICS)
# ==========================================
num_insp = 10000
avg_l = np.random.uniform(100, 1200, num_insp)
theft_f = [1 if (i % 12 == 0) else 0 for i in range(num_insp)]
drop_p = [round(np.random.uniform(45, 85), 2) if tf == 1 else round(np.random.uniform(-10, 20), 2) for tf in theft_f]

voltage_anomaly = list(theft_f)
current_anomaly = list(theft_f)


np.random.seed(45)
theft_flag_realistic = np.array(theft_f)
noise_mask = np.random.rand(num_insp) < 0.15
theft_flag_realistic[noise_mask] = 1 - theft_flag_realistic[noise_mask]

df_theft = pd.DataFrame({
    'Inspection_ID': [f"INSP{i:06d}" for i in range(1, num_insp + 1)],
    'Consumer_ID': np.random.choice(consumer_ids, size=num_insp),
    'Avg_Last6Months': avg_l,
    'Current_Month_Units': (avg_l * (1 - np.array(drop_p)/100)).round(2),
    'Consumption_Drop_Percentage': drop_p,
    'Voltage_Anomaly': voltage_anomaly,
    'Current_Anomaly': current_anomaly,
    'Meter_Tamper_Flag': np.random.choice([0, 1], size=num_insp, p=[0.9, 0.1]),
    'Night_Usage_Ratio': np.random.uniform(0.2, 0.8, num_insp).round(2),
    'Transformer_Loss_Percentage': np.random.uniform(5, 30, num_insp).round(2),
    'Theft_Flag': theft_flag_realistic
})

# Complete Map Structure
datasets = {
    "01_consumers.csv": df_consumers,
    "02_meter_readings.csv": df_readings,
    "03_billing.csv": df_billing,
    "04_transformers.csv": df_transformers,
    "05_transformer_load.csv": df_tx_load,
    "06_feeders.csv": df_feeders,
    "07_outage_logs.csv": df_outages,
    "08_theft_inspection.csv": df_theft
}

# ==========================================
# HTML WEBPAGE GENERATOR LOGIC
# ==========================================
html_content = """
<html>
<head>
    <title>TNEB 8-in-1 Dataset Hub</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; line-height: 1.6; }
        h2 { color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 10px; }
        .card { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); max-width: 600px; }
        .download-btn { display: inline-block; background-color: #007bff; color: white; padding: 8px 12px; 
                        margin: 5px 0; text-decoration: none; border-radius: 4px; font-size: 14px; font-weight: bold;}
        .download-btn:hover { background-color: #0056b3; }
        .item { margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #eee; }
    </style>
</head>
<body>
    <h2>⚡ Smart Energy Management System: All 8 Datasets Ready!</h2>
    <p>All 8 datasets have been successfully generated.Click the buttons below to download the files:</p>
    <div class="card">
"""

print("🌐 preparing download links....Please wait")
for filename, df in datasets.items():
    csv_string = df.to_csv(index=False)
    b64 = base64.b64encode(csv_string.encode('utf-8')).decode()
    href = f'<div class="item">👉 <strong>{filename}</strong> ({len(df)} Rows)<br><a class="download-btn" href="data:text/csv;base64,{b64}" download="{filename}">Download File</a></div>'
    html_content += href

html_content += """
    </div>
</body>
</html>
"""


with open("energy_datasets.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("\n🔥 Success! 'energy_datasets.html' has been successfully created.")
print("Open the file by double-clicking it, and it will launch in your default web browser.")
5
