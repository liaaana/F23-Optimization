# Transportation Problem Solver

This Python code solves the transportation problem using various methods, including the North-West Corner Method, Vogel’s Approximation Method, and Russell’s Approximation Method.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [North-West Corner Method](#north-west-corner-method)
  - [Vogel’s Approximation Method](#vogels-approximation-method)
  - [Russell’s Approximation Method](#russels-approximation-method)
- [Input and Output](#input-and-output)
- [Testing](#testing)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The transportation problem involves minimizing the cost of transporting goods from multiple sources to multiple destinations while satisfying supply and demand constraints. This Python script provides solutions to the transportation problem using different algorithms.

## Algorithms

### North-West Corner Method

The North-West Corner Method is a simple heuristic for obtaining an initial basic feasible solution. It starts from the top-left (north-west) corner of the cost matrix and allocates as much as possible until the supply or demand of a source or destination is exhausted.

### Vogel’s Approximation Method

Vogel’s Approximation Method is an improvement over the North-West Corner Method. It considers the differences between the two smallest costs in each row and column, allocating to the cell with the maximum difference. This method aims to balance the assignment more efficiently.

### Russell’s Approximation Method

Russell’s Approximation Method is another heuristic for solving the transportation problem. It iteratively selects the cell with the minimum value, considering row and column maxima. This method often provides more balanced allocations.

## Input and Output

The code takes input for the transportation problem, including the number of sources and destinations, supply and demand vectors, and the cost matrix. It then outputs the transportation problem table, the initial basic feasible solution obtained by different methods, and the total initial cost.

## Testing

Here are the outcomes from running the code and an online calculator on three distinct tests.

## Usage

To use the code, run it in a Python environment and follow the screenshots to input the transportation problem details. The code will display the transportation problem table, the initial basic feasible solution obtained by different methods, and the total initial cost.

```bash
python script_name.py