# Write your solution here
def transpose(matrix: list):
  copy_matrix = []

  for row in matrix:
    new_row = row[:]
    copy_matrix.append(new_row)

  for row_no in range(len(matrix)):
    for col_no in range(len(matrix)):
      matrix[row_no][col_no] = copy_matrix[col_no][row_no]

  print(matrix)

if __name__ == "__main__":
  mat = [ [1, 2, 3] , [ 4, 5, 6] , [ 7, 8, 9] ]
  transpose(mat)