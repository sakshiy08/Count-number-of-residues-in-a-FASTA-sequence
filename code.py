# Function to count occurrences of a specific alphabet in each line of a given file
def count_alphabet_in_file(alphabet, filename):
    counts = []
    with open(filename, 'r') as file:
        for line in file:
            # Count the occurrences of the specified alphabet in the current line
            count = line.count(str(alphabet))
            counts.append(count)
    return counts

import numpy as np

# Specify the filename containing fasta sequences
filename = 'fastaSeq.txt'

# Create a numpy array with the amino acids of interest
arr = np.array(['G', 'A', 'V', 'L', 'I', 'P', 'F', 'M', 'W'])

# Initialize pointer for indexing
ptr = -1

# Create a numpy array to hold the counts with shape (39, 9)
tot = np.arange(351).reshape(39, 9)

# Loop through each amino acid in the array
for x in arr:
    ptr += 1  # Increment the pointer
    print("****Result for " + x + " ******\n")
    
    # Get the counts of the current amino acid in each line of the file
    counts = count_alphabet_in_file(x, filename)
    
    # Loop through the counts and store them in the 'tot' array
    for i, count in enumerate(counts):
        tot[i][ptr] = count
        print(f" {count}")

# Print the total counts for each line
print("Totals are \n")
for j in range(39):
    s = 0  # Initialize sum for the current line
    for k in range(9):
        s += tot[j][k]  # Sum up the counts for the current line
    print(s, "\n")

sfsjdfhskljll;cs
