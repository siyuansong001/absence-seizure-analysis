# %%
# Import packages

import mne


# %%
# User-defined paths and parameters

# Path to the EDF file.
# Replace "EEG_data.edf" with your EDF file name.
edf_file = "EEG_data.edf"

# Output folder for figures.
# The folder should already exist, or you can create it manually.
output_dir = "output"

# Time window for plotting.
# Change start_time to plot a different 10-s EEG segment.
start_time = 0      # seconds
duration = 10       # seconds

# Scaling for EEG traces in the MNE browser.
scalings = {"eeg": 2005e-6}


# %%
# Load EDF file using MNE

raw = mne.io.read_raw_edf(edf_file, preload=True)

print(raw)
print("Channel names:")
print(raw.ch_names)
print(f"Sampling frequency: {raw.info['sfreq']} Hz")
print(f"Recording duration: {raw.times[-1]:.2f} seconds")


# %%
# Extract and plot 5-9 Hz EEG activity

raw_5_9Hz = raw.copy().filter(5.0, 9.0)

fig_5_9Hz = raw_5_9Hz.plot(
    start=start_time,
    duration=duration,
    scalings=scalings,
    n_channels=len(raw_5_9Hz.ch_names),
    title=f"5-9 Hz filtered EEG, {start_time}-{start_time + duration} s",
    show=False,
)

fig_5_9Hz.savefig(output_dir + "/EEG_5_9Hz_10s_segment.svg")


# %%
# Extract and plot 35-55 Hz EEG activity

raw_35_55Hz = raw.copy().filter(35.0, 55.0)

fig_35_55Hz = raw_35_55Hz.plot(
    start=start_time,
    duration=duration,
    scalings=scalings,
    n_channels=len(raw_35_55Hz.ch_names),
    title=f"35-55 Hz filtered EEG, {start_time}-{start_time + duration} s",
    show=False,
)

fig_35_55Hz.savefig(output_dir + "/EEG_35_55Hz_10s_segment.svg")


# %%
# End

print("Finished loading EDF, filtering EEG, and plotting 10-s EEG traces.")
