# Cryptarithmetic Puzzle (TWO + TWO = FOUR)

This project solves the cryptarithmetic puzzle using a Constraint Satisfaction Problem (CSP) approach.

---

## Problem Description

Solve the equation:

  T W O  
+ T W O  
--------  
F O U R  

Each letter represents a unique digit.

---

## Approach

The problem is modeled as a CSP:

- **Variables:** T, W, O, F, U, R  
- **Domain:** {0–9}  
- **Constraints:**  
  - All letters must have unique digits  
  - Leading digits (T and F) cannot be zero  
  - Arithmetic equation must be satisfied  

A brute-force backtracking approach is used.

---

## Constraints Explanation

Column-wise addition:

- O + O = R (with carry)  
- W + W + carry = U  
- T + T + carry = O  
- Final carry = F  

---

## Features

- Unique digit assignment  
- Handles carry logic  
- Backtracking with permutations  
- Simple and clear implementation  

---

## Example Output
TWO = 734
FOUR = 1468

---

## Concepts Used

- Constraint Satisfaction Problems (CSP)  
- Backtracking Search  
- Permutations  
- Arithmetic Constraints  
