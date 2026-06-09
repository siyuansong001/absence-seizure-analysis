# %%
# Import packages

import os

import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d


# %%
# User-defined paths and parameters

# EDF file name
edf_file = "EEG_data.edf"

# Output folder
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Frequency range for power analysis
fmin = 0
fmax = 55

# Welch PSD parameters
n_fft = 100000

# Segment length for analysis
segment_duration = 1000  # seconds

# Smooth PSD curve for visualization
smooth_sigma = 2


# %%
# Load EDF file using MNE

raw = mne.io.read_raw_edf(edf_file, preload=True)

print(raw)
print("Channel names:")
print(raw.ch_names)
print(f"Sampling frequency: {raw.info['sfreq']} Hz")
print(f"Recording duration: {raw.times[-1]:.2f} seconds")


# %%
# Define segment information

sample_rate = raw.info["sfreq"]

segment_samples = int(segment_duration * sample_rate)
total_samples = len(raw.times)

total_segments = int(np.ceil(total_samples / segment_samples))

print(f"Segment duration: {segment_duration} seconds")
print(f"Samples per segment: {segment_samples}")
print(f"Total number of segments: {total_segments}")


# %%
# Calculate and plot power spectrum for each segment

for segment_idx in range(total_segments):

    # Determine start and end samples for the current segment
    start_sample = segment_idx * segment_samples
    end_sample = min((segment_idx + 1) * segment_samples, total_samples)

    # Extract data segment
    data_segment = raw[:, start_sample:end_sample][0]

    # Create RawArray for the segment
    segment_info = mne.create_info(
        ch_names=raw.ch_names,
        sfreq=sample_rate,
        ch_types="eeg",
    )

    segment_raw = mne.io.RawArray(data_segment, segment_info)

    # Compute power spectral density
    psds, freqs = mne.time_frequency.psd_welch(
        segment_raw,
        fmin=fmin,
        fmax=fmax,
        n_fft=n_fft,
        average="mean",
    )

    # Plot PSD for each channel
    fig, ax = plt.subplots(figsize=(8, 5))

    for channel_idx, channel_psd in enumerate(psds):

        # Smooth PSD for visualization
        smoothed_psd = gaussian_filter1d(channel_psd, sigma=smooth_sigma)

        ax.plot(
            freqs,
            smoothed_psd,
            label=raw.ch_names[channel_idx],
        )

    ax.set_yscale("log")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Power spectral density")
    ax.set_title(f"Power spectrum, segment {segment_idx + 1}")
    ax.legend(frameon=False)

    fig.tight_layout()

    figure_name = f"power_spectrum_segment_{segment_idx + 1}.svg"
    fig.savefig(output_dir + "/" + figure_name)

    plt.show()


# %%
# End

print("Finished power spectrum analysis.")
