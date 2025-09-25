# DS5230 Homework 1: Data Mining and Association Rules

This repository contains solutions for DS5230 (Data Science) Homework 1, focusing on data preprocessing, association rule mining, and academic network analysis using various datasets and algorithms.

## Repository Structure

```
DS5230-HW1/
├── README.md                    # This file
├── dataset_analysis.ipynb       # Main analysis notebook for academic network data
├── csv2arff.py                 # CSV to ARFF format converter utility
├── itemsets2sparsearff.py      # Itemset to sparse ARFF converter
├── normalize.py                # Data normalization utility
├── kosarak.dat                 # Market basket dataset
├── kosarak.arff               # Converted ARFF format of kosarak data
├── Question 4.txt             # Theoretical analysis of lift measure
├── Question 5.pdf             # Problem statement/results (PDF)
├── Question 6.pdf             # Problem statement/results (PDF) 
├── Question 7.txt             # FP-Growth algorithm results and timing
├── 1_data/                    # Weather and voting datasets
│   ├── 1_vote.arff           # Congressional voting records (ARFF)
│   ├── 1_vote.csv            # Congressional voting records (CSV)
│   ├── 1_weather-nominal.arff # Weather data with nominal attributes
│   ├── 1_weather-nominal.csv  # Weather data with nominal attributes (CSV)
│   ├── 1_weather-numeric.arff # Weather data with numeric attributes
│   └── 1_weather-numeric.csv  # Weather data with numeric attributes (CSV)
├── 2_data/                    # Input/output files for data processing
│   ├── 2_in.txt              # Input data file
│   ├── 2_out_-1_1_4.txt      # Processed output (-1,1,4 normalization)
│   ├── 2_out_0_1_2.txt       # Processed output (0,1,2 normalization)
│   └── 2_out_0_1_4.txt       # Processed output (0,1,4 normalization)
└── 3_data/                    # Academic network dataset
    ├── readme.txt            # Format description for academic papers
    └── AP_train.txt          # ArnetMiner academic paper citation network
```

## Assignment Overview

This homework covers several key data mining concepts and techniques:

### 1. Data Format Conversion and Preprocessing
- **CSV to ARFF Conversion**: Converting standard CSV files to Weka's ARFF format
- **Itemset Processing**: Converting transaction data to sparse ARFF format for association rule mining
- **Data Normalization**: Implementing various normalization schemes for numerical data

### 2. Association Rule Mining
- **Market Basket Analysis**: Using the Kosarak dataset for frequent pattern mining
- **FP-Growth Algorithm**: Applying FP-Growth with different parameters in Weka
- **Rule Evaluation**: Analyzing confidence, lift, leverage, and conviction measures

### 3. Academic Network Analysis
- **Citation Network Processing**: Working with ArnetMiner academic paper dataset
- **Publication Analysis**: Extracting patterns from research publications and citations
- **Author and Venue Analytics**: Understanding academic collaboration networks

### 4. Theoretical Analysis
- **Association Rule Metrics**: Mathematical derivation and interpretation of lift measure
- **Statistical Independence**: Proving the relationship between lift=1 and statistical independence

## Key Features

### Data Processing Utilities

#### `csv2arff.py`
Converts CSV files to ARFF format with automatic type detection:
```bash
python csv2arff.py input.csv
```

#### `itemsets2sparsearff.py` 
Converts itemset format data (like Kosarak) to sparse ARFF format:
```bash
python itemsets2sparsearff.py kosarak.dat kosarak.arff
```

#### `normalize.py`
Provides various data normalization methods for preprocessing.

### Analysis Components

#### `dataset_analysis.ipynb`
Comprehensive Jupyter notebook containing:
- Academic paper dataset exploration and visualization
- Citation network analysis
- Author collaboration patterns
- Publication venue analysis
- Statistical summaries and insights

## Datasets Used

1. **Weather Dataset**: Classic weather prediction dataset with both nominal and numeric versions
2. **Congressional Voting Records**: US Congress voting patterns dataset
3. **Kosarak Dataset**: Market basket data from Hungarian online news portal
4. **ArnetMiner Academic Network**: Research paper citation network with metadata

## Key Algorithms and Techniques

- **FP-Growth Algorithm**: Frequent pattern mining for association rules
- **Data Normalization**: Multiple normalization schemes (0-1, z-score, etc.)
- **Network Analysis**: Citation and collaboration network exploration
- **Statistical Analysis**: Computing support, confidence, lift, and other metrics

## Results and Findings

### Association Rule Mining (Question 7)
- Processed 990,002 transactions with 41,270 unique items
- Generated 14 association rules using FP-Growth
- Achieved sub-second execution times for rule mining
- Top rules showed strong associations between items i3, i6, and i11

### Theoretical Analysis (Question 4)
Proved that lift = 1 mathematically implies statistical independence:
- When lift(X ⇒ Y) = 1, then P(X ∩ Y) = P(X) × P(Y)
- This is the fundamental definition of statistical independence
- Demonstrates that lift measure effectively captures item relationships

## Requirements

- Python 3.x
- Jupyter Notebook
- pandas, numpy, matplotlib, seaborn
- Weka (for association rule mining)
- tqdm (for progress bars)

## Usage

1. **Data Conversion**:
   ```bash
   python csv2arff.py 1_data/1_weather-nominal.csv
   python itemsets2sparsearff.py kosarak.dat kosarak.arff
   ```

2. **Analysis**:
   - Open `dataset_analysis.ipynb` in Jupyter Notebook
   - Run all cells to perform complete analysis

3. **Association Rule Mining**:
   - Use Weka Explorer with the generated ARFF files
   - Apply FP-Growth algorithm with specified parameters
---
*DS5230 - Data Science Course*
