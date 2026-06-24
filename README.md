# ⚡ Smart Energy Management System: Power Distribution Analytics & Theft Detection

## 📖 Project Overview

The Smart Energy Management System is an end-to-end Data Analytics, Business Intelligence, and Machine Learning project developed to simulate the operations of a modern electricity distribution network.

The project begins with generating synthetic electricity board datasets using Python. The generated datasets are then imported into a MySQL database, where SQL queries are used to perform data analysis and extract meaningful business insights.

The query results are further integrated into Power BI to create interactive dashboards for monitoring electricity distribution performance, infrastructure reliability, consumer behavior, and outage management.

Finally, a Machine Learning model is developed to identify suspicious electricity consumption patterns and detect potential power theft cases.

This project demonstrates the integration of Python, MySQL, SQL, Power BI, and Machine Learning within the Energy & Utility domain.

---

# 🎯 Project Goals

* Analyze electricity consumption patterns.
* Monitor billing and revenue collection performance.
* Track transformer and feeder utilization.
* Analyze outage frequency and downtime.
* Detect abnormal energy consumption behavior.
* Identify potential electricity theft cases.
* Create interactive dashboards for operational monitoring.
* Enable data-driven decision making for utility management.

---

# 📂 Datasets Utilized

A total of 8 interconnected datasets were generated and used throughout the project.

| Dataset                 | Description                                 |
| ----------------------- | ------------------------------------------- |
| 01_consumers.csv        | Consumer and connection information         |
| 02_meter_readings.csv   | Monthly electricity consumption records     |
| 03_billing.csv          | Billing and payment details                 |
| 04_transformers.csv     | Transformer master information              |
| 05_transformer_load.csv | Transformer load monitoring records         |
| 06_feeders.csv          | Feeder and substation details               |
| 07_outage_logs.csv      | Power outage events and causes              |
| 08_theft_inspection.csv | Inspection records used for theft detection |

### Dataset Statistics

* 2,000 Consumers
* 24,000 Meter Reading Records
* 24,000 Billing Records
* 15,000 Transformer Monitoring Records
* 2,000 Outage Records
* 10,000 Theft Inspection Records

---

# 🗄️ Database Design & SQL Analysis

After generating the datasets, all CSV files were imported into a MySQL database.

## Database Used

* MySQL

## Database Creation

```sql
CREATE DATABASE Energy_Management;
USE Energy_Management;
```

## Tables Imported

* 01_consumers
* 02_meter_readings
* 03_billing
* 04_transformers
* 05_transformer_load
* 06_feeders
* 07_outage_logs
* 08_theft_inspection

## SQL Analysis Performed

### Consumer Analytics

* Total Consumers
* Consumer Distribution by Area
* Consumer Distribution by Tariff Category

### Billing Analytics

* Total Consumption Analysis
* Total Revenue Analysis
* Payment Status Analysis
* Collection Efficiency Calculation
* Top Consumption Analysis

### Infrastructure Analytics

* Transformer Load Monitoring
* Transformer Temperature Analysis
* Feeder Loss Monitoring
* Peak Load Analysis

### Outage Analytics

* Outage Cause Analysis
* Area-wise Outage Distribution
* Average Downtime Analysis

### Theft Analytics

* Meter Tampering Detection
* Voltage Anomaly Investigation
* Consumption Drop Analysis
* Night Usage Monitoring
* Grid Loss Analysis

The SQL query outputs were imported into Power BI for visualization and dashboard creation.

---

# 📊 Power BI Dashboard

The dashboard consists of three major analytical modules.

---

## 1️⃣ Power Distribution Overview

This dashboard provides a comprehensive overview of electricity distribution performance.

### Key KPIs

* Total Consumers
* Total Energy Consumption
* Total Revenue
* Collection Efficiency %

### Visualizations

* Consumer Distribution by Area
* Consumer Distribution by Tariff
* Revenue Analysis
* Payment Status Analysis

### Business Value

Provides utility managers with a complete view of consumers, billing performance, and revenue generation.

---

## 2️⃣ Outage & Infrastructure Monitoring

This dashboard focuses on infrastructure reliability and operational performance.

### Key KPIs

* Total Outage Events
* Average Downtime
* Average Feeder Loss Percentage

### Visualizations

* Outage Cause Analysis
* Area-wise Outage Distribution
* Transformer Temperature Monitoring
* Load Percentage Analysis
* Peak Load Tracking

### Business Value

Supports proactive maintenance planning and infrastructure reliability monitoring.

---

## 3️⃣ Power Theft Analytics

This dashboard focuses on detecting suspicious consumption behavior and potential theft cases.

### Visualizations

* Consumption Drop Analysis
* Meter Tamper Analysis
* Voltage Anomaly Analysis
* Current Anomaly Analysis
* Transformer Loss Analysis
* Night Usage Analysis

### Business Value

Helps identify high-risk consumers and reduce non-technical losses caused by electricity theft.

---

# 🤖 Machine Learning Model

## Power Theft Detection System

A supervised Machine Learning model was developed using the Theft Inspection Dataset.

### Algorithm Used

* Random Forest Classifier

### Input Features

* Avg_Last6Months
* Current_Month_Units
* Consumption_Drop_Percentage
* Voltage_Anomaly
* Current_Anomaly
* Meter_Tamper_Flag
* Night_Usage_Ratio
* Transformer_Loss_Percentage

### Target Variable

* Theft_Flag

### Model Outputs

The model predicts whether a consumer is likely involved in electricity theft and provides:

* Theft Prediction
* Risk Score
* Risk Category
* Final Recommendation

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Performance Results

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 85% |
| Precision | 87% |
| Recall    | 32% |
| F1 Score  | 47% |


---

# 🚀 Project Execution Workflow

## Step 1 – Generate Datasets

Run:

```bash
python dataset_generator.py
```

### Output Generated

* 8 CSV datasets
* HTML dataset download portal

Generated file:

```text
energy_datasets.html
```

---

## Step 2 – Download Datasets

Open:

```text
energy_datasets.html
```

The webpage displays download links for all generated datasets.

---

## Step 3 – Create MySQL Database

```sql
CREATE DATABASE Energy_Management;
USE Energy_Management;
```

---

## Step 4 – Import Datasets into MySQL

Import all 8 generated CSV files into their respective MySQL tables.

---

## Step 5 – Execute SQL Queries

Perform analytical SQL queries for:

* Consumer Analysis
* Billing Analysis
* Revenue Analysis
* Outage Analysis
* Transformer Monitoring
* Theft Investigation

---

## Step 6 – Build Power BI Dashboard

Import SQL query results into Power BI and create:

* Power Distribution Overview Dashboard
* Outage & Infrastructure Monitoring Dashboard
* Power Theft Analytics Dashboard

---

## Step 7 – Train Machine Learning Model

Run:

```bash
python theft_detection.py
```

Workflow:

1. Load Theft Inspection Dataset
2. Data Cleaning
3. Feature Selection
4. Train-Test Split
5. Random Forest Training
6. Prediction
7. Evaluation
8. Confusion Matrix Generation

---

## Step 8 – Manual Theft Prediction

The system allows manual user inputs and generates:

* Risk Score
* Risk Category
* Theft Prediction
* Final Recommendation

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Database

* MySQL

## Query Language

* SQL

## Data Processing

* Pandas
* NumPy

## Data Visualization

* Power BI
* Matplotlib
* Seaborn

## Machine Learning

* Scikit-Learn
* Random Forest Classifier

---

# 📁 Repository Structure

```text
Smart-Energy-Management-System
│
├── Dataset_Generator
│   └── dataset_generator.py
│
├── SQL
│   └── energy_management_queries.sql
│
├── Datasets
│
├── PowerBI
│   └── Smart_Energy_Dashboard.pbix
│
├── MachineLearning
│   └── theft_detection.py
│
├── Screenshots
│   ├── Dashboard_Page1.png
│   ├── Dashboard_Page2.png
│   ├── Dashboard_Page3.png
│   └── Confusion_Matrix.png
│
├── requirements.txt
└── README.md
```

---

# 📸 Dashboard Screenshots

## Power Distribution Overview

<img width="1305" height="732" alt="Screenshot 2026-06-24 123829" src="https://github.com/user-attachments/assets/06fea2bd-0775-4da6-8861-fa7ad16ae5ee" />


---

## Outage & Infrastructure Monitoring

<img width="1296" height="728" alt="Screenshot 2026-06-24 123902" src="https://github.com/user-attachments/assets/1b14f55c-a5fb-4848-bc83-385408ea3c51" />


---

## Power Theft Analytics

<img width="1302" height="727" alt="Screenshot 2026-06-24 123930" src="https://github.com/user-attachments/assets/d60a7bf9-c881-4299-bc19-c730afbdb807" />


---

## Machine Learning Confusion Matrix

<img width="575" height="491" alt="Screenshot 2026-06-24 121636" src="https://github.com/user-attachments/assets/c63e4e3a-f2c4-44f6-ba4b-23d3a93abb8c" />


---

# 🔮 Future Enhancements

* Real-Time Smart Meter Integration
* IoT-Based Monitoring
* Automated Alert Generation
* Cloud-Based Analytics Platform
* Deep Learning-Based Theft Detection
* Web-Based Monitoring Dashboard
* Predictive Maintenance System

---

# 👨‍💻 Author

**Dhinakaran R**

B.E. Computer Science and Engineering
Anna University Regional Campus Madurai

### Skills Demonstrated

* Python Programming
* Database Management
* SQL Query Writing
* Data Analytics
* Data Modeling
* Business Intelligence
* Power BI Dashboard Development
* Machine Learning
* Predictive Analytics
* Data Visualization
* Energy Management Analytics
