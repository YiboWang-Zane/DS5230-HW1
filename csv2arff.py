#!/usr/bin/env python3
"""
csv2arff.py - Convert CSV files to ARFF format
"""

import csv
import os

def is_numeric(value):
    """Check if a value can be interpreted as numeric."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def csv2arff(csv_path):
    """Convert a CSV file to ARFF format and print to console."""
    
    print(f"\n{'='*60}")
    print(f"Converting: {csv_path}")
    print(f"{'='*60}\n")
    if not os.path.exists(csv_path):
        print(f"Error: File '{csv_path}' not found")
        return

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        data = list(reader)
        
        if not data:
            print("Error: Empty CSV file")
            return
        
        # First row contains attribute names
        attributes = data[0]
        rows = data[1:]
        
        # Get relation name from filename
        relation_name = os.path.splitext(os.path.basename(csv_path))[0]
        attr_types = []
        nominal_values = []
        
        for col_idx in range(len(attributes)):
            # Check if all non-missing values in this column are numeric
            is_numeric_col = True
            unique_values = set()
            has_non_missing = False
            
            for row in rows:
                if col_idx < len(row):
                    val = row[col_idx].strip()
                    # Check if value is not missing
                    if val and val != '?':
                        has_non_missing = True
                        unique_values.add(val)
                        if not is_numeric(val):
                            is_numeric_col = False
            
            # If no non-missing values found, assume numeric
            if not has_non_missing:
                is_numeric_col = True
            
            if is_numeric_col:
                attr_types.append('numeric')
                nominal_values.append(None)
            else:
                attr_types.append('nominal')
                # Sort the unique values for nominal attributes
                nominal_values.append(sorted(unique_values))
        
        print(f"@relation {relation_name}")
        print()
        
        # Print attribute declarations
        for i, attr in enumerate(attributes):
            if attr_types[i] == 'numeric':
                print(f"@attribute {attr} numeric")
            else:
                if nominal_values[i]:
                    values_str = ','.join(nominal_values[i])
                    print(f"@attribute {attr} {{{values_str}}}")
                else:
                    print(f"@attribute {attr} {{}}")
        
        print()
        print("@data")

        for row in rows:
            row_values = []
            for i in range(len(attributes)):
                if i < len(row):
                    val = row[i].strip()
                    # Convert empty values to missing value marker
                    if val:
                        row_values.append(val)
                    else:
                        row_values.append('?')
                else:
                    # Handle rows with fewer columns than headers
                    row_values.append('?')
            print(','.join(row_values))

def main():
    possible_paths = [
        '1_data/',
        './',
        '/Users/zane/Desktop/DS5230-HW1/1_data/',
    ]

    csv_files = [
        '1_vote.csv',
        '1_weather-nominal.csv',
        '1_weather-numeric.csv'
    ]

    data_path = None
    for path in possible_paths:
        test_file = os.path.join(path, csv_files[0])
        if os.path.exists(test_file):
            data_path = path
            break
    
    if data_path is None:
        print("Error: Could not find data directory. Please run from the correct location.")
        print("Looking for files:", csv_files)
        return
    
    print(f"Found data directory: {os.path.abspath(data_path)}")
    
    # Process each CSV file
    for csv_file in csv_files:
        csv_path = os.path.join(data_path, csv_file)
        try:
            csv2arff(csv_path)
        except Exception as e:
            print(f"Error processing {csv_file}: {e}")
    
    print(f"\n{'='*60}")
    print("Conversion complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()