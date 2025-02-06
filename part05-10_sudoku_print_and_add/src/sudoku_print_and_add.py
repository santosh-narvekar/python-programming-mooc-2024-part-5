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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
  if( row_no < len(sudoku) or column_no< len(sudoku)):
    sudoku[row_no][column_no] = number

if __name__== "__main__":
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

  print_sudoku(sudoku)
  add_number(sudoku, 0, 0, 2)
  add_number(sudoku, 1, 2, 7)
  add_number(sudoku, 5, 7, 3)
  print()
  print("Three numbers added:")
  print()
  print_sudoku(sudoku)