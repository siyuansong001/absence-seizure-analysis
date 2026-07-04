# Absence seizure analysis

This repository contains analysis scripts and notebooks associated with the manuscript:

**Convergent Inhibitory Cortical Circuit Disruption Drives Genetically Distinct Absence Seizures**

The code is provided as an example of the analysis workflow used for EEG, single-cell, and Patch-seq related analyses in the study.

## Repository structure

* `EEG_analysis/`
  Scripts for loading EEG data, filtering and plotting EEG traces, and analyzing EEG power spectra.

* `Single_cell_analysis/`
  Notebooks for single-cell and Patch-seq related analyses for selected main and supplementary figures.

## Data availability

Large raw data files are not included in this repository due to file size and data-sharing restrictions. The scripts and notebooks are provided to document the analysis workflow.

## Requirements

The code requires Python packages including:

* NumPy
* pandas
* scipy
* matplotlib
* scikit-learn
* Scanpy
* AnnData
* umap-learn
* seaborn
* MNE

Additional package requirements may depend on the specific analysis script or notebook.

## License

This repository is released under the MIT License.

## Installation

The analysis scripts were tested using Python 3.8. Required Python packages include numpy, pandas, scipy, matplotlib, scikit-learn, scanpy, anndata, umap-learn, seaborn and mne-python.

To install the required Python packages, run:

```bash
pip install numpy pandas scipy matplotlib scikit-learn scanpy anndata umap-learn seaborn mne
