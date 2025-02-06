# Write your solution here

def times_ten(start_index: int, end_index: int):
  times_ten_dictionary = {}
  for index in range(start_index,end_index + 1):
    times_ten_dictionary[index] = index * 10
  return times_ten_dictionary

if __name__ == "__main__":
  d = times_ten(3, 6)
  print(d)