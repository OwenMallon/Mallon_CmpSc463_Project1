"""
    Developed by: Owen Mallon
    Project 1 : CmpSc463 - Design Analysis Algorithms
    Due: March 12th 2026

    Task:
    Develop an algorithm‑driven system to segment, cluster, and analyze time‑series sensor data from a real water‑pump machine.
    The system will use core algorithmic techniques—Divide‑and‑Conquer segmentation, Closest Pair, and Maximum Subarray—to characterize 
    machine behavior and relate the results to four machine‑health categories derived from RUL (Remaining Useful Life).
"""
import pandas as pd
import Project1_Task1 as tk1
import Project1_Task2 as tk2
import Project1_Task3 as tk3

def rulCategorySort(val):
    if val < Q10:
        return "Extremely Low"
    elif Q10 <= val < Q50:
        return "Moderately Low"
    elif Q50 <= val < Q90:
        return "Moderately High"
    else:
        return "Extremely High"


# Init rul_hrs.csv file for reading data
# NOTE: Dataset calls for 52 sensors, however only 50 are present; 15 and 50 are missing (?)
print("Init csv file for reading and confirming data and sensor readability...")
df = pd.read_csv("data/rul_hrs.csv")
df = df.iloc[:10000]
df = df.drop(columns=["Unnamed: 0"])

sensorCol = [col for col in df.columns if "sensor_" in col]
print(f"Sensor Count: {len(sensorCol)}")
print(f"Sensor List: {df.columns.tolist()}")

Q10 = df["rul"].quantile(0.10)
Q50 = df["rul"].quantile(0.50)
Q90 = df["rul"].quantile(0.90)

df["rul_category"] = df["rul"].apply(rulCategorySort)
print(df["rul_category"].value_counts())

# Tasks
tk1.runTask1(df, sensorCol)

tk2.runTask2(df, sensorCol)

tk3.runTask3(df, sensorCol)



