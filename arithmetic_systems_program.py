def make_matrix(matrix_elements, matrix_rows, matrix_columns):
    if matrix_rows * matrix_columns == len(matrix_elements):
        matrix = []
        matrix_next_row = []
        for i in range(matrix_rows):
            matrix_next_row = matrix_elements[i * matrix_columns : (i + 1) * matrix_columns] 
            matrix.append(matrix_next_row)
        return matrix
    else:
        return

def matrices_elements_precision(matrix, precision):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if abs(matrix[i][j]) % 1 < 1e-10 or 1 - (abs(matrix[i][j]) % 1) < 1e-10:
                matrix[i][j] = int(matrix[i][j] + 0.5)
            else:
                matrix[i][j] = round(matrix[i][j], precision)
    return matrix
    
def submatrix(matrix, list_deleted_rows, list_deleted_columns):
    submatrix = []
    for row in matrix:
        for column in row:
            submatrix.append(column)
    submatrix = make_matrix(submatrix, len(matrix), len(matrix[0]))
    for i in range(len(list_deleted_rows)):
        submatrix.pop(list_deleted_rows[i] - 1)
        if i != len(list_deleted_rows) - 1:
            for i in range(len(list_deleted_rows)):
                list_deleted_rows[i] = list_deleted_rows[i] - 1
    list_deleted_columns2 = list_deleted_columns[:]
    for row in submatrix:
        for i in range(len(list_deleted_columns)):
            row.pop(list_deleted_columns[i] - 1)
            if i != len(list_deleted_columns) - 1:
                for i in range(len(list_deleted_columns)):
                    list_deleted_columns[i] = list_deleted_columns[i] - 1
        list_deleted_columns = list_deleted_columns2
    return submatrix

def transpose_matrix(matrix):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    transpose_matrix = []
    for row in matrix:
        for column in row:
            transpose_matrix.append(0)
    transpose_matrix = make_matrix(transpose_matrix, matrix_columns, matrix_rows)
    for i in range(matrix_columns): 
        for j in range(matrix_rows):
            transpose_matrix[i][j] = matrix[j][i]
    return transpose_matrix

def inverse_matrix(matrix):
##    det_matrix = matrix_determinant(matrix)
    product = 1
    B = Gauss_elimination(matrix)[0]
    for i in range(len(matrix)):
        product = product * B[i][i]
    det_matrix = (- 1) ** (Gauss_elimination(matrix)[1] % 2) * product
    if is_square_matrix(matrix) and det_matrix != 0:        
        adjoint_matrix = []
        for row in matrix:
            for column in row:
                adjoint_matrix.append(0)
        adjoint_matrix = make_matrix(adjoint_matrix, len(matrix), len(matrix[0]))
        matrix_rows = len(matrix)
        matrix_columns = len(matrix[0])
        for i in range(matrix_rows):
            for j in range(matrix_columns):
                product = 1
                submatrix2 = submatrix(matrix, [i + 1], [j + 1])
                B = Gauss_elimination(submatrix2)[0]
                for k in range(len(B)):
                    product = product * B[k][k]
                det_submatrix2 = (-1) ** (Gauss_elimination(submatrix2)[1] % 2) * product
##                submatrix2 = submatrix(matrix, [i + 1], [j + 1])
##                det_submatrix2 = matrix_determinant(submatrix2)
                if (i + j) % 2 == 0:
                    adjoint_matrix[i][j] = det_submatrix2
                else:
                    adjoint_matrix[i][j] = -1 * det_submatrix2
        adjoint_matrix = transpose_matrix(adjoint_matrix)
        inverse_matrix = number_matrix_multiplication(det_matrix ** (-1), adjoint_matrix)
        return inverse_matrix
    else:
        return

def is_square_matrix(matrix):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    if matrix_rows == matrix_columns:
        return True
    else:
        return False
    
def matrices_sum(matrix_A, matrix_B):
    matrix_C_elements = []
    matrix_A_rows = len(matrix_A)
    matrix_A_columns = len(matrix_A[0])
    matrix_B_rows = len(matrix_B)
    matrix_B_columns = len(matrix_B[0]) 
    if matrix_A_rows == matrix_B_rows and matrix_A_columns == matrix_B_columns:
        for i in range(matrix_A_rows):
            for j in range(matrix_A_columns):
                matrix_C_elements.append(matrix_A[i][j] + matrix_B[i][j])
        matrix_C = make_matrix(matrix_C_elements, matrix_A_rows, matrix_A_columns)
        return matrix_C
    else:
        return

def matrices_multiplication(matrix_A, matrix_B):
    matrix_C_elements = []
    matrix_A_rows = len(matrix_A)
    matrix_A_columns = len(matrix_A[0])
    matrix_B_rows = len(matrix_B)
    matrix_B_columns = len(matrix_B[0])
    if matrix_A_columns == matrix_B_rows:
        for i in range(matrix_A_rows): 
            for j in range(matrix_B_columns):
                C_next_element = 0
                for k in range(matrix_B_rows):
                    C_next_element = C_next_element + matrix_A[i][k] * matrix_B[k][j]
                matrix_C_elements.append(C_next_element)
        matrix_C = make_matrix(matrix_C_elements, matrix_A_rows, matrix_B_columns)
        return matrix_C
    else:
        return

def number_matrix_multiplication(number, matrix):
    product = []
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    for row in matrix:
        for column in row:
            product.append(0)
    product = make_matrix(product, len(matrix), len(matrix[0]))
    for i in range(matrix_rows): 
        for j in range(matrix_columns):
            product[i][j] = number * matrix[i][j]
    return product
    
def matrix_determinant(matrix):
    if is_square_matrix(matrix):
        if len(matrix) == 1:
            determinant1 = matrix[0][0]
            return determinant1
        elif len(matrix) == 2:
            determinant2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return determinant2
        elif len(matrix) > 2:
            determinant = 0
            for i in range(len(matrix)):
                cofactor = 0
                submatrix2 = submatrix(matrix, [1], [i + 1])
                if i % 2 == 0:
                    cofactor = matrix[0][i] * matrix_determinant(submatrix2)
                else:
                    cofactor = -1 * matrix[0][i] * matrix_determinant(submatrix2)
                determinant = determinant + cofactor
            return determinant
    else:
        return

def switch_rows(matrix, ri, rj):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    if ri * rj <= matrix_rows ** 2:
        if is_square_matrix(matrix):
            permutation_matrix_elements = []
            for i in range(matrix_rows):
                for j in range(matrix_columns):
                    permutation_matrix_elements.append(0)
            matrix_P = make_matrix(permutation_matrix_elements, matrix_rows, matrix_columns)
            for i in range(matrix_rows):
                if i + 1 == ri:
                    matrix_P[i][rj - 1] = 1
                elif i + 1 == rj:
                    matrix_P[i][ri - 1] = 1
                else:
                    matrix_P[i][i] = 1
            new_matrix = matrices_multiplication(matrix_P, matrix)
            return new_matrix
        else:
            new_matrix_elements = []
            for i in range(matrix_rows):
                for j in range(matrix_columns):
                    new_matrix_elements.append(0)
            new_matrix = make_matrix(new_matrix_elements, matrix_rows, matrix_columns)
            for i in range(matrix_rows):
                if i + 1 == ri:
                    new_matrix[i] = matrix[rj - 1]
                elif i + 1 == rj:
                    new_matrix[i] = matrix[ri - 1]
                else:
                    new_matrix[i] = matrix[i]
            return new_matrix
    else:
        return

def Gauss_elimination(matrix):
    Gauss_matrix = []
    times_switch_rows = 0
    for row in matrix:
        for column in row:
            Gauss_matrix.append(column)
    Gauss_matrix = make_matrix(Gauss_matrix, len(matrix), len(matrix[0]))
    Gauss_matrix_rows = len(Gauss_matrix)
    Gauss_matrix_columns = len(Gauss_matrix[0])
    pivot = 0
    for c in range(Gauss_matrix_columns):
        for i in range(pivot + 1, Gauss_matrix_rows):
            if Gauss_matrix[pivot][pivot] != 0:
                pivot_row = make_matrix(Gauss_matrix[pivot], 1, Gauss_matrix_columns)
                for j in range(pivot + 1, Gauss_matrix_rows):
                    elimination_coefficient = -1 * Gauss_matrix[j][pivot] / Gauss_matrix[pivot][pivot]
                    elimination_row = number_matrix_multiplication(elimination_coefficient, pivot_row)
                    changeable_row = make_matrix(Gauss_matrix[j], 1, Gauss_matrix_columns)
                    Gauss_matrix[j] = matrices_sum(changeable_row, elimination_row)[0]
            else:
                Gauss_matrix = switch_rows(Gauss_matrix, pivot + 1, i + 1)
                times_switch_rows = times_switch_rows + 1
        pivot = pivot + 1
    return [Gauss_matrix, times_switch_rows]

def solve_linear_systems_with_one_solution(coefficients_matrix, stable_terms_matrix):
    inverse_matrix2 = inverse_matrix(coefficients_matrix)
    matrix_X = matrices_multiplication(inverse_matrix2, stable_terms_matrix)
    return matrix_X

print('\nThis program solves arithmetic systems.\n')
while True:
    print('\nGive the dimension of the coefficients_matrix:\n')
    n = int(input())
    print('\nGive the elements of the coefficients_matrix:\n')
    matrix_elements = []
    for i in range(n ** 2):
        a = complex(input())
        matrix_elements.append(a)
    A = make_matrix(matrix_elements, n, n)
    print(A)
    print('\nGive the elements of the stable_terms_matrix:\n')
    matrix_elements = []
    for i in range(n):
        a = complex(input())
        matrix_elements.append(a)
    B = make_matrix(matrix_elements, n, 1)
    print('\nCoefficients_matrix:\n')
    for row in A:
        print(row)
    print('\nStable_terms_matrix:\n')
    for row in B:
        print(row)
    print('\nHere is the solution:\n')
    X = solve_linear_systems_with_one_solution(A, B)
    for row in X:
        print(row)
##    det_A = matrix_determinant(A)
##    print(det_A)
##    B = Gauss_elimination(A)
##    for row in B:
##        print(row)
##    det_B = matrix_determinant(B)
##    print(det_B)