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