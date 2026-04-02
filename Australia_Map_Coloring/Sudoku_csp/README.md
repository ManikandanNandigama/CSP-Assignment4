Sudoku Solver using CSP
This project implements a Sudoku solver using the Constraint Satisfaction Problem (CSP) approach with backtracking.

Problem Description
Solve a 9×9 Sudoku grid such that:

Each row contains digits 1–9 exactly once
Each column contains digits 1–9 exactly once
Each 3×3 subgrid contains digits 1–9 exactly once
Approach
The Sudoku is modeled as a CSP:

Variables: 81 cells (grid positions)
Domain: {1–9}
Constraints:
Row constraint
Column constraint
3×3 subgrid constraint
Backtracking is used to fill empty cells.

Features
Solves standard 9×9 Sudoku
Ensures all constraints are satisfied
Uses recursive backtracking
Efficient and simple implementation
Example Output
[5, 3, 4, 6, 7, 8, 9, 1, 2] [6, 7, 2, 1, 9, 5, 3, 4, 8] ...

Concepts Used
Constraint Satisfaction Problems (CSP)
Backtracking Search
Recursive Algorithms
