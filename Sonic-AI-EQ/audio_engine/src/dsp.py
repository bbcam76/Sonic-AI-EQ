# Audio Signal Processing Module

This module contains functions and classes for digital signal processing (DSP) used in the Sonic AI EQ project. It includes methods for filtering, transforming, and analyzing audio signals.

import numpy as np
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def apply_gain(signal, gain_db):
    gain = 10 ** (gain_db / 20)
    return signal * gain

def normalize(signal):
    max_val = np.max(np.abs(signal))
    if max_val > 0:
        return signal / max_val
    return signal

def split_bands(signal, fs, bands):
    band_signals = []
    for lowcut, highcut in bands:
        band_signal = bandpass_filter(signal, lowcut, highcut, fs)
        band_signals.append(band_signal)
    return band_signals

def mix_bands(band_signals):
    return np.sum(band_signals, axis=0)