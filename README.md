# Constraint Satisfaction Problems (CSP)

This repository contains implementations of four classical Constraint Satisfaction Problems (CSPs) from Artificial Intelligence:

- Australia Map Coloring Problem
- Telangana District Map Coloring Problem
- Sudoku Solver using CSP
- Cryptarithmetic Puzzle (TWO + TWO = FOUR)

Each problem is solved using Backtracking Search with constraints.

---

## 1: Australia Map Coloring CSP

### Problem Description
Color the seven principal states and territories of Australia:

WA, NT, QLD, SA, NSW, V, T

such that no two adjacent regions share the same color.

### CSP Formulation
- Variables: WA, NT, QLD, SA, NSW, V, T  
- Domain: {Red, Green, Blue}  
- Constraints: Adjacent states must not have the same color  

Example:
WA ≠ NT, WA ≠ SA, NT ≠ QLD, SA ≠ NSW, NSW ≠ V  

### Output
- Valid color assignment  

---

## 2: Telangana District Map Coloring CSP

### Problem Description
Color all 33 districts of Telangana such that neighboring districts do not share the same color.

### CSP Formulation
- Variables: 33 Telangana districts  
- Domain: {Red, Green, Blue, Yellow}  
- Constraints: Adjacent districts must have different colors  

### Output
- Valid district coloring solution  

---

## 3: Sudoku Solver using CSP

### Problem Description
Solve a 9×9 Sudoku puzzle such that:
- Each row contains digits 1–9 exactly once  
- Each column contains digits 1–9 exactly once  
- Each 3×3 subgrid contains digits 1–9 exactly once  

### CSP Formulation
- Variables: 81 cells  
- Domain: {1–9}  
- Constraints: AllDiff across rows, columns, and subgrids  

### Output
- Solved Sudoku grid  

---

## 4: Cryptarithmetic Puzzle (TWO + TWO = FOUR)

### Problem Description
Solve the cryptarithmetic puzzle:

  T W O
+ T W O
-------
F O U R

Each letter represents a unique digit.

### CSP Formulation
- Variables: T, W, O, F, U, R  
- Domain: {0–9}  

### Constraints:
- All letters must have different digits  
- Leading digits cannot be zero  
- Arithmetic correctness must be satisfied  

### Output
- Correct digit substitution  

---

## Technologies Used
- Python 3  

---

## Conclusion
These implementations demonstrate how CSP techniques such as:
- Variable assignment  
- Domain restriction  
- Constraint checking  
- Backtracking search  

can be applied to solve AI problems effectively.
