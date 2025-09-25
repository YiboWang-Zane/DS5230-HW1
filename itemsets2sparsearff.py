#!/usr/bin/env python3
"""
itemsets2sparsearff.py
Converts itemset format data to sparse ARFF format for Weka Explorer.
Usage: python itemsets2sparsearff.py kosarak.dat kosarak.arff
"""

import sys
import time

def itemsets2sparsearff(filepath, output_file=None):
    """
    Convert itemset format to sparse ARFF format.
    
    Args:
        filepath: Path to input file in itemset format
        output_file: Optional output file path (if None, prints to stdout)
    
    Returns:
        Tuple of (num_transactions, num_unique_items, elapsed_time)
    """
    start_time = time.time()
    
    # Read the file and collect all unique items
    transactions = []
    unique_items = set()
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                items = line.split()
                transactions.append(items)
                unique_items.update(items)
                
    sorted_items = sorted(unique_items, key=lambda x: int(x))
    item_to_index = {item: idx for idx, item in enumerate(sorted_items)}
    output_lines = []
    
    # Header
    relation_name = filepath.split('/')[-1].split('.')[0]
    output_lines.append(f"@RELATION {relation_name}")
    for item in sorted_items:
        output_lines.append(f"@ATTRIBUTE i{item} {{0, 1}}")
    
    # Data section
    output_lines.append("@DATA")
    
    # Convert each transaction to sparse format
    for transaction in transactions:
        if transaction:
            unique_transaction_items = set(transaction)
            indices = sorted([item_to_index[item] for item in unique_transaction_items])
            sparse_pairs = [f"{idx} 1" for idx in indices]
            sparse_repr = ", ".join(sparse_pairs)
            output_lines.append(f"{{{sparse_repr}}}")
        else:
            # Empty transaction
            output_lines.append("{}")
    
    # Write output
    if output_file:
        with open(output_file, 'w') as f:
            for line in output_lines:
                f.write(line + '\n')
    else:
        for line in output_lines:
            print(line)
    
    elapsed_time = time.time() - start_time
    
    return len(transactions), len(unique_items), elapsed_time


def main():
    if len(sys.argv) < 2:
        print("Usage: python itemsets2sparsearff.py <input_file> [output_file]", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        num_trans, num_items, elapsed = itemsets2sparsearff(input_file, output_file)
        print(f"\n--- Conversion Statistics ---", file=sys.stderr)
        print(f"Input file: {input_file}", file=sys.stderr)
        if output_file:
            print(f"Output file: {output_file}", file=sys.stderr)
        print(f"Transactions processed: {num_trans:,}", file=sys.stderr)
        print(f"Unique items found: {num_items:,}", file=sys.stderr)
        print(f"Conversion time: {elapsed:.2f} seconds", file=sys.stderr)
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()