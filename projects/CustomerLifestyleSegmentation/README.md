# Customer Lifestyle Segmentation Using Credit Card Transactions

## Overview

This project develops interpretable customer lifestyle segments from credit card transaction behavior using unsupervised machine learning. Two customer representations are compared—aggregate behavioral features (PCA) and transaction-level behavioral features (Truncated SVD + RFM)—to identify meaningful customer groups for customer profiling and personalization.

## Dataset

The analysis uses the IBM Synthetic Credit Card Transaction Dataset, containing multi-year transaction records with customer IDs, timestamps, transaction amounts, merchant information, MCC codes, and geographic attributes. Merchant category descriptions were joined from an MCC reference table to improve interpretability.

## Data Preparation

The raw data were preprocessed by removing fraudulent transactions, standardizing timestamps and transaction amounts, and enriching records with merchant category descriptions. Data cleaning and integration were performed in a separate preprocessing notebook. This notebook focuses on feature engineering, clustering, and behavioral analysis.

## Methodology

- Aggregate customer features with PCA
- Transaction-level behavioral features with Truncated SVD and RFM metrics
- K-Means, Gaussian Mixture Models, and Spectral Clustering
- Cluster evaluation using interpretability and stability

## Key Findings

- Identified five interpretable customer lifestyle segments.
- Transaction-level behavioral features produced more meaningful segmentation than aggregate features.
- Customer segments exhibited distinct spending, merchant diversity, geographic, and engagement patterns.
- Extended the analysis with temporal tracking to examine behavioral changes across consecutive five-year windows.

## Technologies

Python • Pandas • NumPy • Scikit-learn • SciPy • Matplotlib • Seaborn • Plotly
