# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
  if ( y >= len(game_board) or y < 0): return False
  
  cur_list = game_board[y] 
  
  if( x >= len(cur_list) or x < 0 ): return False
  
  if (cur_list[x] == "X" and piece != "X"): cur_list[x]=piece
  if (cur_list[x] == "O" and piece != "O"): cur_list[x]=piece

  if( cur_list[x] == "" ): 
    cur_list[x] = piece
    return True    
  else:
    return False
  
if __name__ == "__main__":
  game_board = [["", "", ""], ["", "", ""], ["", "", ""]]

  print(play_turn(game_board, 2, -1, "X"))
  
  print(game_board)