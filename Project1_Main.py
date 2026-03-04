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
import random
import matplotlib.pyplot as plt
import numpy as np
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
# NOTE: Dataset calls for 52 sensors, however only 50 are present 15 and 50 are missing (?)
print("Init csv file for reading and confirming data and sensor readability...")
df = pd.read_csv("data/rul_hrs.csv")
df = df.iloc[:10000]

df = df.drop(columns=["Unnamed: 0"])

sensor_col = [col for col in df.columns if "sensor_" in col]
print(f"Sensor Count: {len(sensor_col)}")
print(f"Sensor List: {df.columns.tolist()}")

Q10 = df["rul"].quantile(0.10)
Q50 = df["rul"].quantile(0.50)
Q90 = df["rul"].quantile(0.90)

df["rul_category"] = df["rul"].apply(rulCategorySort)
print(df["rul_category"].value_counts())

# TASK 1: Segmentation
print("\n\n TASK 1 : Segmentation \n\n")
selectedSensors = [random.choice(sensor_col) for _ in range(10)]
print(f"Selected Sensors: {selectedSensors}")

# =========================
# 5. APPLY TO ALL 10 SENSORS (COLLECT FIRST)
# =========================

all_segments = {}
complexity_scores = {}

for sensor in selectedSensors:
    signal = df[sensor].values

    # Adaptive threshold (relative to signal variance)
    threshold = np.var(signal) * 0.5

    segments = tk1.segmentation(signal, threshold=threshold)

    all_segments[sensor] = segments
    complexity_scores[sensor] = len(segments)


fig, axes = plt.subplots(5, 2, figsize=(18, 20))
axes = axes.flatten()

for i, sensor in enumerate(selectedSensors):
    signal = df[sensor].values
    segments = all_segments[sensor]

    axes[i].plot(signal)

    for start, end in segments:
        axes[i].axvline(start, linestyle="--", alpha=0.4)

    axes[i].set_title(f"Segmentation of {sensor} (Segments: {len(segments)})")
    axes[i].set_xlabel("Time Index")
    axes[i].set_ylabel("Sensor Value")

plt.tight_layout()
plt.show()

# =========================
# 7. PRINT COMPLEXITY SCORES
# =========================

print("\nSegmentation Complexity Scores:")
for sensor, score in complexity_scores.items():
    print(f"{sensor}: {score}")