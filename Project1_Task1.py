'''
    Task 1:
    Implement a recursive segmentation algorithm on one selected sensor signal (e.g., sensor_00)
    or an engineered composite signal (e.g., average of all sensors).

    Algorithm steps

    Compute variance of the current segment.
    If variance > threshold:
    recursively split into left and right halves
    Else:
    mark the segment as “stable”
'''

import numpy as np
import random
import matplotlib.pyplot as plt

def segmentation(signal, threshold = 1.0, minSize = 50):
    segments = []
    segmentSignal(signal, 0, len(signal), threshold, minSize, segments)
    return segments

def segmentSignal(signal, start, end, threshold, min_size, segments):
    segment = signal[start:end]

    # Veirfy Size
    if (end - start) <= min_size:
        segments.append((start, end))
        return

    variance = np.var(segment)

    if variance > threshold:
        mid = (start + end) // 2
        segmentSignal(segment, start, mid, threshold, min_size, segments)
        segmentSignal(segment, mid, end, threshold, min_size, segments)
    else:
        segments.append((start, end))

def runTask1(df, sensor_cols):

    selectedSensors = random.sample(sensor_cols, 10)

    complexity_scores = {}
    all_segments = {}

    for sensor in selectedSensors:

        signal = df[sensor].values

        threshold = np.var(signal) * 0.5

        segments = segmentation(signal, threshold)

        all_segments[sensor] = segments
        complexity_scores[sensor] = len(segments)

    # Visualization
    fig, axes = plt.subplots(5, 2, figsize=(15, 18))
    axes = axes.flatten()

    for i, sensor in enumerate(selectedSensors):

        signal = df[sensor].values
        segments = all_segments[sensor]

        axes[i].plot(signal)

        for start, end in segments:
            axes[i].axvline(start, linestyle="--")

        axes[i].set_title(sensor)

    plt.tight_layout()
    plt.show()

    # Complexity scores
    print("\nSegmentation Complexity Scores:")

    for sensor, score in complexity_scores.items():
        print(sensor, ":", score)