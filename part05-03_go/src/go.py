# Write your solution here

def who_won(game_board: list):
  count_player_1_pieces = 0
  count_player_2_pieces = 0

  for row in game_board:
    for column in row:
      if ( column == 1 ): count_player_1_pieces += 1
      elif ( column == 2): count_player_2_pieces += 1

  if count_player_1_pieces > count_player_2_pieces:
     return 1
  elif count_player_1_pieces < count_player_2_pieces:
     return 2
  elif count_player_1_pieces == count_player_2_pieces:
    return 0

if __name__ == "__main__":
  print(who_won([[2,1,2,1,2]]))