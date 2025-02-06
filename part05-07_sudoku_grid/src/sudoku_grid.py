# Write your solution here
def row_correct(sudoku: list, row_no:int):
  item_tracker = []
  for item in sudoku[row_no]:
    if ( item in item_tracker ):
      return False
    if ( item != 0 ): item_tracker.append(item)
  
  return True

def column_correct(sudoku: list, column_no: int):
  check_column_list = []

  for row in sudoku:

    if ( row[column_no] in check_column_list ):
      return False
    
    if( row[column_no] != 0 ):
      check_column_list.append(row[column_no])

  return True

def block_correct(sudoku: list, row_no: int, column_no: int):
  block_check_list = []
  
  for row in range(row_no,row_no + 3):
    for column in range(column_no, column_no + 3):
      if (sudoku[row][column] in block_check_list):
        return False
      
      if ( sudoku[row][column] != 0 ): block_check_list.append(sudoku[row][column])
    

  return True

def sudoku_grid_correct(sudoku: list):
  for row_no in range(len(sudoku)):
    
    row_check = row_correct(sudoku,row_no)
    if ( row_check == False ):
      return False
    
    col_check = column_correct(sudoku,row_no)
    if ( col_check == False ):
      return False
    
  for row_no in range( 0, len(sudoku) ,3 ):
    for col_no in range( 0 , len(sudoku) , 3 ):
      block_check = block_correct( sudoku, row_no, col_no )
     
      if block_check == False:
        return False

          
  return True

if __name__ == "__main__":
  sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
  ]

  print(sudoku_grid_correct(sudoku1))

  sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
  ]
  
  print(sudoku_grid_correct(sudoku2))

  sudoku3 = [
  [ 2, 0, 1, 9, 8, 0, 4, 0, 3 ],
  [ 8, 0, 0, 6, 3, 0, 0, 0, 0 ],
  [ 6, 4, 3, 0, 0, 0, 5, 9, 8 ],
  [ 3, 1, 6, 7, 5, 0, 0, 4, 0 ],
  [ 8, 4, 9, 3, 1, 6, 0, 7, 0 ],
  [ 0, 0, 0, 8, 4, 9, 0, 3, 0 ],
  [ 1, 0, 3, 0, 0, 0, 0, 4, 6 ],
  [ 5, 9, 7, 4, 0, 0, 3, 1, 2 ],
  [ 4, 6, 8, 1, 2, 0, 7, 0, 0 ],
  ]

  print(sudoku_grid_correct(sudoku3))
