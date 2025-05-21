# Sparse Matrix Operations in Python

This project implements basic operations (Addition, Subtraction, and Multiplication) on sparse matrices using Python.

Sparse matrices are loaded from plain text files in a custom format, processed efficiently, and the results are saved in the same format.

---

## 📁 Project Structure

dsa/
└── sparse_matrix/
├── code/
│ └── src/
│ └── matrix.py # Main program
├── sample_inputs/ # Input matrix files
└── sample_outputs/ # Output result files



## 🧾 Input File Format

Each matrix file must follow this format:

rows=3
cols=3
(0, 0, 5)
(1, 2, 7)
(2, 1, 9)



- First two lines indicate matrix dimensions.
- Each subsequent line is a non-zero element: `(row_index, col_index, value)`.

---

## ▶️ How to Run

1. **Navigate to the source directory**:

```bash
cd dsa/sparse_matrix/code/src
Run the script:

python matrix.py
Provide input when prompted:


Path of first file: ../../sample_inputs/matrixfile1.txt
Path of second file: ../../sample_inputs/matrixfile2.txt
Operation [add, subtract, multiply]: multiply
Output file name: ../../sample_outputs/result_multiply.txt

Sample Operations
 Addition

Operation: add
Input: matrixfile1.txt, matrixfile2.txt
Output: additions.txt

Subtraction

Operation: subtract
Input: matrixfile1.txt, matrixfile2.txt
Output: subtractions.txt


Operation: multiply

Input: matrixfile1.txt, matrixfile3.txt
Output: multiplications.txt

✅ Features
Efficient sparse representation using dictionaries

Input validation and error handling

Custom file format for compatibility

Works with large matrices (memory-efficient)

 Requirements
Python 3.x (no external libraries required)

 Output Format
Matches input format, e.g.:


rows=3
cols=2
(0, 1, 14)
(2, 0, 45)
Only non-zero values are stored.

 Author
Name: Bonae Ineza

Course: Data Structures and Algorithms

Assignment: Sparse Matrix Operations – Homework 