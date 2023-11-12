# Transportation Problem Solver

This Python code solves the transportation problem using the North-West Corner Method, Vogel’s Approximation Method, and Russell’s Approximation Method.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [North-West Corner Method](#north-west-corner-method)
  - [Vogel’s Approximation Method](#vogels-approximation-method)
  - [Russell’s Approximation Method](#russels-approximation-method)
- [Input and Output](#input-and-output)
- [Testing](#testing)
- [Usage](#usage)

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

An [online calculator](https://cbom.atozmath.com/CBOM/Transportation.aspx?q=vam&q1=3%2c2%2c7%2c6%3b7%2c5%2c2%2c3%3b2%2c5%2c4%2c5%6050%2c60%2c25%6060%2c40%2c20%2c15%60S1%2cS2%2cS3%60D1%2cD2%2cD3%2cD4%60ram%60false%60false%60MIN%60false&do=1#PrevPart) was used to check the code results during testing.

## Usage

To use the code, run it in a Python environment and follow the screenshots to input the transportation problem details. The code will display the transportation problem table, the initial basic feasible solution obtained by different methods, and the total initial cost.

```bash
python main.py
