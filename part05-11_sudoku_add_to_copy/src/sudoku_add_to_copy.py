# Write your solution here
def print_sudoku(sudoku: list):
 
  for row_no in range(0,len(sudoku),3):
    # first looping over all rows till length of rows 
    # incrementing by 3 in every step i.e 0,3,6
    for column_row in range(row_no,row_no + 3):
      # targeting first 3 rows i.e 0 to 2 3 to 5 6 to 8
      for col_no in range(0,len(sudoku),3):
        # looping over all columns till length 
        # incrementing by 3 i.e 0,3,6 
        for row_column in range(col_no,col_no + 3):
          # targeting first 3 columns i.e 0 to 2 3 to 5 6 to 8
          if( sudoku[column_row][row_column] == 0 ):
            # checking for 0 
            print("_ ",end="")
          else: 
            print(f"{sudoku[column_row][row_column]} ",end="")
        print(" ",end="")    
        # adding space after 3 columns finish on same row
      # adding print to jump to next row
      print()

    # Adding extra print after one loop is completed of 3 rows
    print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  new_sudoku = []
  for row in sudoku:
    new_row = row[:]
    new_sudoku.append(new_row)
    
  new_sudoku[row_no][column_no] = number
  return new_sudoku

if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)