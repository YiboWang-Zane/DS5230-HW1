#!/usr/bin/env python3
"""
normalize.py - Feature scaling/normalization program
Usage: python normalize.py <input_file> <lower_bound> <upper_bound> <precision>
"""

import sys
import os

def normalize_data(file_path, lower_bound, upper_bound, precision):
    """
    Normalize data from a file within specified bounds.
    """
    
    # Read the data file
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Parse the data into a 2D list
    data = []
    for line in lines:
        # Split by spaces and convert to floats
        row = [float(x) for x in line.strip().split()]
        if row:
            data.append(row)
    
    if not data:
        print("Error: No data found in file")
        return
    num_features = len(data[0])
    feature_mins = []
    feature_maxs = []
    
    for col_idx in range(num_features):
        col_values = [row[col_idx] for row in data]
        feature_mins.append(min(col_values))
        feature_maxs.append(max(col_values))
    
    # Normalize each data point
    normalized_data = []
    
    for row in data:
        normalized_row = []
        for col_idx, value in enumerate(row):
            min_val = feature_mins[col_idx]
            max_val = feature_maxs[col_idx]
            
            if max_val == min_val:
                # Set to midpoint of the range
                normalized_val = (lower_bound + upper_bound) / 2
            else:
                normalized_val = lower_bound + ((value - min_val) / (max_val - min_val)) * (upper_bound - lower_bound)
            normalized_row.append(round(normalized_val, precision))
        
        normalized_data.append(normalized_row)
    
    # Output the normalized data
    for row in normalized_data:
        formatted_values = []
        for val in row:
            if precision == 0:
                formatted_values.append(str(int(val)))
            else:
                # Use format string to ensure exact decimal places
                format_str = f"{{:.{precision}f}}"
                formatted_values.append(format_str.format(val))
        
        print(' '.join(formatted_values))

def main():
    if len(sys.argv) == 5:
        # Command line arguments provided
        input_file = sys.argv[1]
        lower_bound = float(sys.argv[2])
        upper_bound = float(sys.argv[3])
        precision = int(sys.argv[4])
        
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found")
            sys.exit(1)
        
        normalize_data(input_file, lower_bound, upper_bound, precision)
    
    elif len(sys.argv) == 1:
        
        possible_paths = [
            '2_data/',
            './',
            '/Users/zane/Desktop/DS5230-HW1/2_data/',
        ]
        
        data_path = None
        for path in possible_paths:
            test_file = os.path.join(path, '2_in.txt')
            if os.path.exists(test_file):
                data_path = path
                break
        
        if data_path is None:
            print("Error: Could not find data directory with 2_in.txt")
            sys.exit(1)
        
        input_file = os.path.join(data_path, '2_in.txt')
        
        # Test case 1: bounds -1 to 1, precision 4
        print("\n" + "="*60)
        print("Test 1: Bounds [-1, 1], Precision: 4")
        print("Output (compare with 2_out_-1_1_4.txt):")
        print("="*60)
        normalize_data(input_file, -1, 1, 4)
        
        # Test case 2: bounds 0 to 1, precision 2
        print("\n" + "="*60)
        print("Test 2: Bounds [0, 1], Precision: 2")
        print("Output (compare with 2_out_0_1_2.txt):")
        print("="*60)
        normalize_data(input_file, 0, 1, 2)
        
        # Test case 3: bounds 0 to 1, precision 4
        print("\n" + "="*60)
        print("Test 3: Bounds [0, 1], Precision: 4")
        print("Output (compare with 2_out_0_1_4.txt):")
        print("="*60)
        normalize_data(input_file, 0, 1, 4)
        
    else:
        print("Usage: python normalize.py <input_file> <lower_bound> <upper_bound> <precision>")
        print("Example: python normalize.py 2_in.txt -1 1 4")
        print("\nOr run without arguments to test hardcoded examples")
        sys.exit(1)

if __name__ == "__main__":
    main()