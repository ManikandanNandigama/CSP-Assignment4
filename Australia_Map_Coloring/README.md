# Australia Map Coloring using CSP

This project implements the Map Coloring Problem for the seven principal states and territories of Australia using a Constraint Satisfaction Problem (CSP) approach.

---

## Problem Description

The objective is to assign colors to each region such that:

- Each state is assigned one color  
- No two adjacent states share the same color  

States considered:
WA, NT, QLD, SA, NSW, V, T  

---

## Approach

The problem is modeled as a CSP with:

- **Variables:** WA, NT, QLD, SA, NSW, V, T  
- **Domains:** {Red, Green, Blue}  
- **Constraints:** Adjacent states must have different colors  

A backtracking algorithm is used to find a valid solution.

---

## Constraints (Adjacency)

- WA → NT, SA  
- NT → WA, SA, QLD  
- QLD → NT, SA, NSW  
- SA → WA, NT, QLD, NSW, V  
- NSW → QLD, SA, V  
- V → SA, NSW  
- T → No neighbors  

---

## Features

- Simple CSP modeling  
- Efficient backtracking solution  
- Minimal number of colors used (3)  
- Easy to understand implementation  

---

## Example Output
# Australia Map Coloring using CSP

This project implements the Map Coloring Problem for the seven principal states and territories of Australia using a Constraint Satisfaction Problem (CSP) approach.

---

## Problem Description

The objective is to assign colors to each region such that:

- Each state is assigned one color  
- No two adjacent states share the same color  

States considered:
WA, NT, QLD, SA, NSW, V, T  

---

## Approach

The problem is modeled as a CSP with:

- **Variables:** WA, NT, QLD, SA, NSW, V, T  
- **Domains:** {Red, Green, Blue}  
- **Constraints:** Adjacent states must have different colors  

A backtracking algorithm is used to find a valid solution.

---

## Constraints (Adjacency)

- WA → NT, SA  
- NT → WA, SA, QLD  
- QLD → NT, SA, NSW  
- SA → WA, NT, QLD, NSW, V  
- NSW → QLD, SA, V  
- V → SA, NSW  
- T → No neighbors  

---

## Features

- Simple CSP modeling  
- Efficient backtracking solution  
- Minimal number of colors used (3)  
- Easy to understand implementation  

---

## Example Output
WA -> Red
NT -> Green
SA -> Blue
...

---

## Concepts Used

- Constraint Satisfaction Problems (CSP)  
- Backtracking Search  
- Graph Representation  
