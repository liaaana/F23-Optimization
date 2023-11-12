# Transportation Problem

## About the Project
This program implements the search of initial basic feasible solution for Transporation Problem.
Transportation problem is another kind of linear programming problem in which commodity
is distributed from a set of sources to a set of destinations subject to the supply and demand
of the sources and destination respectively such that the total cost of transportation is minimized.\
This program uses North-West corner method, Vogel's approximation method, and Russell's approximation method
to find the initial basic feasible solution. 

## Run

1. Clone the repository using `git clone https://github.com/liaaana/F23-Optimization-Task3`
2. Run the program using `python main.py`

## Testing
An [online calculator](https://cbom.atozmath.com/CBOM/Transportation.aspx?q=vam&q1=3%2c2%2c7%2c6%3b7%2c5%2c2%2c3%3b2%2c5%2c4%2c5%6050%2c60%2c25%6060%2c40%2c20%2c15%60S1%2cS2%2cS3%60D1%2cD2%2cD3%2cD4%60ram%60false%60false%60MIN%60false&do=1#PrevPart) was used to check the code results during testing.

### Input
The program input contains:
- `S` — vector of coefficients of supply
- `D` — vector of coefficients of demand
- `C` — matrix of coefficients of costs

### Output
The program output contains:
- input parameter table (which was constructed using matrix `C`, vectors `S` and `D`)
- 3 vectors of initial basic feasible solution - `x0` using North-West corner method, Vogel's approximation method, and Russell's approximation method
- total initial costs for each solution

![image](https://github.com/liaaana/F23-Optimization-Task3/assets/71718152/58db528c-7f76-4a96-9f6c-8877657dd76d)
![image](https://github.com/liaaana/F23-Optimization-Task3/assets/71718152/773117c8-78d3-4887-8e1c-b0e19e46129d)

