# Count-number-of-residues-in-a-FASTA-sequence


## Description

This script counts occurrences of specific amino acids in each line of a fasta file and stores the counts in a 2D numpy array

### How It Works

1. **Function Definition**:
   - `count_alphabet_in_file(alphabet, filename)`: Counts occurrences of the specified amino acid in each line of the given file

2. **Main Script**:
   - **Input**:
     - `filename`: Path to the fasta file
     - `arr`: Numpy array of amino acids to count
   - **Processing**:
     - Iterates through each amino acid in `arr`
     - Counts occurrences in each line and stores in `tot` array
   - **Output**:
     - Prints counts for each amino acid
     - Prints total counts per line
