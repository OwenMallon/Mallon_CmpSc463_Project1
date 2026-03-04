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