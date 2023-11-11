import numpy as np


def get_problem_input():
    """Gets the input for the transportation problem.

    Returns:
        A tuple of the transportation problem table, the number of sources, and the number of destinations.
    """
    # Get the number of sources
    ns = int(input("Enter the number of sources: "))
    # Check if the number of sources is valid
    if ns <= 0:
        print("The method is not applicable! Number of sources should be greater than zero.")
        exit(1)

    # Get the number of destinations
    nd = int(input("Enter the number of destinations: "))
    # Check if the number of destinations is valid
    if nd <= 0:
        print("The method is not applicable! Number of destinations should be greater than zero.")
        exit(1)

    # Get the supply vector
    S = list(map(float, input("Enter the vector of supply coefficients (S) separated by spaces: ").split()))
    # Check if the supply vector is valid
    if len(S) != ns:
        print("The method is not applicable! Supply vector is incorrect.")
        exit(1)

    # Get the demand vector
    D = list(map(float, input("Enter the vector of demand coefficients (D) separated by spaces: ").split()))
    # Check if the demand vector is valid
    if len(D) != nd:
        print("The method is not applicable! Demand vector is incorrect.")
        exit(1)

    # Check if the problem is balanced
    if sum(S) != sum(D):
        print("The problem is not balanced!")
        exit(1)

    # Get the cost matrix
    print("Enter the cost matrix (C) row by row costs separated by spaces:")
    C = []
    for i in range(ns):
        row = list(map(float, input(
            f"Enter the costs for transportation from source {i + 1} to destinations separated by spaces: ").split()))
        # Check if the cost matrix is valid
        if len(row) != nd:
            print("The method is not applicable! Cost matrix is incorrect.")
            exit(1)
        for elem in row:
            # Check if the cost is valid
            if elem <= 0:
                print("The method is not applicable! Cost is incorrect.")
                exit(1)
        C.append(row)

    # Convert lists to NumPy arrays
    S = np.array(S)
    D = np.array(D)
    C = np.array(C)

    # Create the transportation problem table
    table = np.zeros((ns + 1, nd + 1))
    table[:ns, :nd] = C
    table[:ns, -1] = S
    table[-1, :nd] = D

    return table, ns, nd


def print_table_with_headers(table, ns, nd):
    """Prints the transportation problem table with headers.

    Args:
        table: The transportation problem table.
        ns: The number of sources.
        nd: The number of destinations.
    """
    # Print table header
    print("-----------------------------")
    print("Transportation problem table")
    print("-----------------------------")
    # Calculate cell width for formatting
    cell_width = max(
        len(str(int(np.max(table)))), len("Supply"), len("Demand"), len(f"Source{ns}"), len(f"Dest{nd}")) + 1

    def format_cell(cell):
        return str(cell).rjust(cell_width)

    # Print destination headers
    print(" " * cell_width, end="")
    for i in range(nd):
        print(f"Dest{i + 1}".rjust(cell_width), end="")
    print("Supply".rjust(cell_width))

    # Print table with values
    for i in range(ns):
        print(f"Source{i + 1}".rjust(cell_width), end="")
        for j in range(nd):
            print(format_cell(table[i, j]), end="")
        print(format_cell(table[i, -1]))

    # Print demand row
    print("Demand".rjust(cell_width), end="")
    for j in range(nd):
        print(format_cell(table[-1, j]), end="")
    print("\n")


def print_solution(x0, table, ns, nd):
    """Prints the solution to the transportation problem.

    Args:
        x0: The initial basic feasible solution.
        table: The transportation problem table.
        ns: The number of sources.
        nd: The number of destinations.
    """
    # Print the initial basic feasible solution
    print("x0 = [", end="\n")
    print("\n".join([f"x{i + 1}{j + 1} = {str(x0[i, j])}" for i in range(ns) for j in range(nd)]))
    # Calculate and print the total initial cost
    total_cost = 0
    for i in range(ns):
        for j in range(nd):
            total_cost += x0[i, j] * table[i, j]
    print("]")
    print(f"Total initial cost: {total_cost} \n")


def north_west_corner_method(table, ns, nd):
    """
    Implements the North-West Corner Method for solving the transportation problem.

    Args:
        table: The transportation problem table.
        ns: The number of sources.
        nd: The number of destinations.

    Returns:
        The initial basic feasible solution obtained by the method.
    """
    # Initialize the initial basic feasible solution matrix
    x0 = np.zeros((ns, nd))
    i, j = 0, 0
    # Fill the matrix based on the North-West Corner Method
    while i < ns and j < nd:
        # Check if supply from the current source is less than demand from the current destination
        if table[i, -1] < table[-1, j]:
            # Allocate the entire supply
            x0[i, j] = table[i, -1]
            table[i, -1] = 0
            table[-1, j] -= x0[i, j]
            i += 1
        else:
            # Allocate the entire demand
            x0[i, j] = table[-1, j]
            table[i, -1] -= x0[i, j]
            table[-1, j] = 0
            j += 1
    return x0


def vogels_approximation_method(table, ns, nd):
    """
    Implements Vogel’s Approximation Method for solving the transportation problem.

    Args:
        table: The transportation problem table.
        ns: The number of sources.
        nd: The number of destinations.

    Returns:
        The initial basic feasible solution obtained by the method.
    """
    # Initialize the initial basic feasible solution matrix
    x0 = np.zeros((ns, nd))

    # Iterate until either row or column requirements are satisfied
    while np.any(table[:-1, -1] > 0) and np.any(table[-1, :-1] > 0):

        # Calculate differences between the two smallest costs for each row
        row_differences = []
        for i in range(ns):
            if table[i, -1] > 0:
                min_values = [table[i, index] for index in range(nd) if table[-1, index] > 0]
                if len(min_values) >= 2:
                    min_values.sort()
                    row_differences.append(min_values[1] - min_values[0])
                elif len(min_values) == 1:
                    row_differences.append(min_values[0])
                else:
                    row_differences.append(-1)
            else:
                row_differences.append(-1)

        # Calculate differences between the two smallest costs for each column
        col_differences = []
        for j in range(nd):
            if table[-1, j] > 0:
                min_values = [table[index, j] for index in range(ns) if table[index, -1] > 0]
                if len(min_values) >= 2:
                    min_values.sort()
                    col_differences.append(min_values[1] - min_values[0])
                elif len(min_values) == 1:
                    col_differences.append(min_values[0])
                else:
                    col_differences.append(-1)
            else:
                col_differences.append(-1)

        # Find the maximum difference and corresponding indices
        max_row_difference = -1
        row_index = -1
        for i, value in enumerate(row_differences):
            if value != -1:
                if value > max_row_difference:
                    max_row_difference = value
                    row_index = i

        max_col_difference = -1
        col_index = -1
        for j, value in enumerate(col_differences):
            if value != -1:
                if value > max_col_difference:
                    max_col_difference = value
                    col_index = j

        # Determine the cell to be filled based on the differences
        if max_row_difference > max_col_difference:
            min_col_value = float("inf")
            col_index = -1
            for index in range(nd):
                if table[row_index, index] < min_col_value and table[-1, index] > 0:
                    min_col_value = table[row_index, index]
                    col_index = index
        else:
            min_row_value = float("inf")
            row_index = -1
            for index in range(ns):
                if table[index, col_index] < min_row_value and table[index, -1] > 0:
                    min_row_value = table[index, col_index]
                    row_index = index

        # Calculate the minimum supply and update the solution matrix and table
        min_supply = min(table[row_index, -1], table[-1, col_index])
        x0[row_index, col_index] = min_supply
        table[row_index, -1] -= min_supply
        table[-1, col_index] -= min_supply

    return x0


def russels_approximation_method(table, ns, nd):
    """
    Implements Russell’s Approximation Method for solving the transportation problem.

    Args:
        table: The transportation problem table.
        ns: The number of sources.
        nd: The number of destinations.

    Returns:
        The initial basic feasible solution obtained by the method.
    """
    # Initialize the initial basic feasible solution matrix
    x0 = np.zeros((ns, nd))

    # Iterate until either row or column requirements are satisfied
    while np.any(table[:-1, -1] > 0) and np.any(table[-1, :-1] > 0):
        # Calculate maximum values for each row considering non-negative supply
        row_max = []
        for i in range(ns):
            row_values = []
            if table[i, -1] <= 0:
                row_max.append(-1)
                continue
            for j in range(nd):
                if table[-1, j] <= 0:
                    continue
                row_values.append(table[i][j])
            row_max.append(max(row_values))

        # Calculate maximum values for each column considering non-negative demand
        col_max = []
        for j in range(nd):
            col_values = []
            if table[-1, j] <= 0:
                col_max.append(-1)
                continue
            for i in range(ns):
                if table[i, -1] <= 0:
                    continue
                col_values.append(table[i][j])
            col_max.append(max(col_values))

        # Find the cell with the minimum value considering row and column maxima
        row_index = -1
        col_index = -1
        min_val = 100000000
        for i in range(ns):
            if table[i, -1] <= 0:
                continue
            row_maxima = row_max[i]
            for j in range(nd):
                if table[-1, j] <= 0:
                    continue
                col_maxima = col_max[j]
                if table[i, j] - row_maxima - col_maxima < min_val:
                    min_val = table[i, j] - row_maxima - col_maxima
                    row_index = i
                    col_index = j
                elif (table[i, j] - row_maxima - col_maxima) == min_val and (table[i, j] * min(
                        table[i, -1], table[-1, j])) < (
                        table[row_index, col_index] * min(table[row_index, -1], table[-1, col_index])):
                    min_val = table[i, j] - row_maxima - col_maxima
                    row_index = i
                    col_index = j

        # Calculate the minimum supply and update the solution matrix and table
        min_supply = min(table[row_index, -1], table[-1, col_index])
        x0[row_index, col_index] = min_supply
        table[row_index, -1] -= min_supply
        table[-1, col_index] -= min_supply

    return x0


# The main part of the code
if __name__ == '__main__':
    # Get input for the transportation problem
    problem_table, num_sources, num_destinations = get_problem_input()

    # Print the transportation problem table with headers
    print_table_with_headers(problem_table, num_sources, num_destinations)

    # Apply North-West Corner Method and print the result
    north_west_corner_method_x0 = north_west_corner_method(problem_table.copy(), num_sources, num_destinations)
    print("Vector of initial basic feasible solution - x0 obtained by North-West corner method")
    print_solution(north_west_corner_method_x0, problem_table.copy(), num_sources, num_destinations)

    # Apply Vogel’s Approximation Method and print the result
    vogels_approximation_method_x0 = vogels_approximation_method(problem_table.copy(), num_sources, num_destinations)
    print("Vector of initial basic feasible solution - x0 obtained by Vogel’s approximation method")
    print_solution(vogels_approximation_method_x0, problem_table.copy(), num_sources, num_destinations)

    # Apply Russell’s Approximation Method and print the result
    russels_approximation_method_x0 = russels_approximation_method(problem_table.copy(), num_sources, num_destinations)
    print("Vector of initial basic feasible solution - x0 obtained by Russell’s approximation method")
    print_solution(russels_approximation_method_x0, problem_table.copy(), num_sources, num_destinations)
