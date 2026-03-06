'''
    Task 3:
    Implement Kadane algorithm to find the maximum subset sum and corresponding segment for a given time series.

    Step 1 — Preprocess a Sensor Signal and compute the absolute first‑difference:
        d[i] = | sensor_k[i] − sensor_k[i−1] |
        Then subtract the average of these absolute differences
        x[i] = d[i] − mean(d)
    Step 2 — Apply Kadane’s Algorithm
        Run Kadane’s algorithm on x[i] to find the maximum‑sum subarray, i.e., the interval with the most intense sustained deviation.
        This gives the start index, end index, and the total deviation.
    Step 3 — Compare With RUL Categories
        For each time index in the max‑deviation interval, check the RUL category assigned from the dataset’s rul field (transformed into 4 groups based on quantiles).
        Discuss whether this high‑deviation interval falls mostly in one of 4 RUL categoris
    Step 4 — Repeat for All 52 Sensors
    Step 5 — Discuss which sensors are good early indicators of low RUL, based on where their maximum‑deviation intervals appear.
'''

import numpy as np


def maxSubarray(arr):

    max_sum = arr[0]
    current_sum = arr[0]

    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return start, end, max_sum

def runTask3(df, sensor_cols):
    for sensor in sensor_cols:
        signal = df[sensor].values
        d = np.abs(np.diff(signal))
        x = d - np.mean(d)
        start, end, score = maxSubarray(x)
        rul_segment = df["rul_category"].iloc[start:end]
        counts = rul_segment.value_counts()
        print("\nSensor:", sensor)
        print("Max Deviation Interval:", start, "-", end)
        print("Deviation Score:", score)
        print("RUL Category Distribution:")
        print(counts)