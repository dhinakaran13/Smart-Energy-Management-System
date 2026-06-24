CREATE DATABASE Energy_Management;
use Energy_Management;
SELECT COUNT(Consumer_ID) AS Total_Consumers 
FROM 01_consumers;

SELECT 
    SUM(Units) AS Total_Consumption_Units,
    SUM(Amount) AS Total_Revenue_Amount
FROM 03_billing;

SELECT 
    Payment_Status,
    COUNT(Bill_ID) AS Number_of_Bills,
    SUM(Amount) AS Total_Amount
FROM 03_billing
GROUP BY Payment_Status;

SELECT 
    Area,
    COUNT(Consumer_ID) AS Total_Consumers
FROM 01_consumers
GROUP BY Area
ORDER BY Total_Consumers DESC;

SELECT 
    Tariff,
    COUNT(Consumer_ID) AS Consumer_Count
FROM 01_consumers
GROUP BY Tariff;

SELECT 
    Consumer_ID,
    Units,
    Amount,
    Payment_Status
FROM 03_billing
ORDER BY Units DESC
LIMIT 10;

SELECT 
    ROUND((SUM(CASE WHEN Payment_Status = 'Paid' THEN Amount ELSE 0 END) / SUM(Amount)) * 100, 2) AS Collection_Efficiency_Percentage
FROM 03_billing;

SELECT 
    Transformer_ID,
    AVG(Utilization_Percentage) AS Avg_Load_Percentage,
    AVG(Temperature) AS Avg_Temperature_Celsius
FROM 05_transformer_load
GROUP BY Transformer_ID
HAVING Avg_Load_Percentage > 50 OR Avg_Temperature_Celsius > 55
ORDER BY Avg_Load_Percentage DESC;

SELECT 
    Cause,
    COUNT(Outage_ID) AS Total_Outage_Events,
    SUM(Duration_Minutes) AS Total_Downtime_Minutes,
    AVG(Duration_Minutes) AS Avg_Resolution_Time_Mins
FROM 07_outage_logs
GROUP BY Cause
ORDER BY Total_Outage_Events DESC;

SELECT 
    Area,
    COUNT(Outage_ID) AS Total_Outages_Count
FROM 07_outage_logs
GROUP BY Area
ORDER BY Total_Outages_Count DESC;

SELECT 
    COUNT(Outage_ID) AS Total_Outage_Events,
    AVG(Duration_Minutes) AS Avg_Downtime_Minutes
FROM 07_outage_logs;

SELECT 
    AVG(Transformer_Loss_Percentage) AS Avg_Feeder_Loss_Percentage
FROM 08_theft_inspection;

SELECT 
    TIME(Date_Time) AS Log_Time,
    AVG(Load_KW) AS Avg_Hourly_Consumption,
    MAX(Load_KW) AS Peak_Load_KW
FROM 05_transformer_load
GROUP BY TIME(Date_Time)
ORDER BY Log_Time ASC;

SELECT 
    Meter_Tamper_Flag,
    Voltage_Anomaly,
    COUNT(Inspection_ID) AS Total_Suspected_Cases
FROM 08_theft_inspection
GROUP BY Meter_Tamper_Flag, Voltage_Anomaly;

SELECT 
    Consumer_ID,
    Avg_Last6Months,
    Current_Month_Units,
    Consumption_Drop_Percentage,
    Transformer_Loss_Percentage
FROM 08_theft_inspection
WHERE Consumption_Drop_Percentage > 40 AND Transformer_Loss_Percentage > 15
ORDER BY Consumption_Drop_Percentage DESC;

SELECT 
    Consumer_ID,
    Night_Usage_Ratio,
    Transformer_Loss_Percentage,
    Theft_Flag
FROM 08_theft_inspection
WHERE Night_Usage_Ratio > 0.70 AND Theft_Flag = 1;

SELECT 
    Theft_Flag,
    COUNT(Inspection_ID) AS Total_Cases,
    AVG(Transformer_Loss_Percentage) AS Avg_Grid_Loss_Percentage
FROM 08_theft_inspection
GROUP BY Theft_Flag;