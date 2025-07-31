# Waterflow Data Preparation Pipeline

## Overview
This repository contains a data preparation pipeline for processing water flow billing data. The pipeline consists of several Jupyter notebooks and utility scripts that clean, transform, and prepare raw billing data for analysis.

## Directory Structure
```
data_preparation/
└── v1/
    ├── record_cleaning.ipynb     # Cleans and preprocesses raw billing data
    ├── record_compilation.ipynb  # Compiles cleaned records into a master dataset
    ├── record_splitting.ipynb    # Splits combined monthly records into individual files
    └── utilities.py              # Helper functions for file I/O and common operations
```

## File Descriptions

### 1. `record_cleaning.ipynb`
**Purpose**: Cleans and preprocesses raw billing data by:
- Handling missing values and anomalies
- Standardizing address formats
- Validating meter readings
- Flagging data quality issues

**Key Features**:
- Handles various data anomalies and edge cases
- Standardizes connection types and statuses
- Validates consumption calculations
- Exports cleaned data in a consistent format

### 2. `record_compilation.ipynb`
**Purpose**: Compiles cleaned monthly records into a consolidated dataset.

**Key Features**:
- Merges data from multiple time periods
- Handles duplicate records
- Standardizes data formats
- Creates a master dataset for analysis

### 3. `record_splitting.ipynb`
**Purpose**: Processes files containing multiple months of data by:
- Identifying and separating records by month
- Validating data consistency
- Exporting split files in a standardized format

### 4. `utilities.py`
**Purpose**: Provides helper functions used across the pipeline.

**Key Functions**:
- `read_csv(file_path)`: Reads CSV files with automatic encoding detection
- `save_csv(df, file_path)`: Saves DataFrames to CSV with proper encoding

## Workflow

1. **Data Cleaning** (`record_cleaning.ipynb`)
   - Process raw billing data
   - Clean and standardize fields
   - Export cleaned monthly files

2. **Data Splitting** (`record_splitting.ipynb`)
   - Process files with multiple months of data
   - Split into individual monthly files
   - Validate data consistency

3. **Data Compilation** (`record_compilation.ipynb`)
   - Combine all cleaned monthly files
   - Handle duplicates and inconsistencies
   - Create master dataset

## Prerequisites

- Python 3.6+
- Required packages (install with `pip install -r requirements.txt`):
  - pandas
  - numpy
  - chardet
  - matplotlib
  - seaborn

## Usage

1. Place raw data files in the appropriate directory structure
2. Run notebooks in order:
   - `record_cleaning.ipynb`
   - `record_splitting.ipynb` (if needed)
   - `record_compilation.ipynb`

## Data Dictionary

### Core Fields
- `Control Number`: Unique identifier for each account
- `Account Name`: Name of the account holder
- `Service Address`: Physical address of the service
- `District`: Service district
- `Street`: Street name
- `Previous Reading`: Previous meter reading
- `Present Reading`: Current meter reading
- `Cleaned Consumption`: Calculated consumption
- `Record Status`: Status of the record (e.g., Corrected, Unchanged)
- `Connection Status`: Status of the service connection

## Notes

- The pipeline is designed to handle various data quality issues commonly found in billing data
- Customize the address standardization in `record_cleaning.ipynb` as needed
- Review and adjust the data validation rules based on your specific requirements

## Author
Mark June E. Almojuela

## License
[Specify License]