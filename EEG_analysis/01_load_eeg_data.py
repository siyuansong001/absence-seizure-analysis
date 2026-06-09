import mne

file_path = "EEG_data.edf"
raw = mne.io.read_raw_edf(file_path, preload=True)

print(raw)
