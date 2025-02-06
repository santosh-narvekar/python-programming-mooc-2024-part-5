# Write your solution here
def create_tuple(x: int, y: int, z: int):
  list = [x,y,z]
  min_val = min(list)
  max_val = max(list)
  sum = x + y + z 
  tup = (min_val,max_val,sum)
  return tup

if __name__ == "__main__":
  print(create_tuple(5, 3, -1))