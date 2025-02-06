# Write your solution here

def longest(string_list: list):
  longest_string = string_list[0]

  for string in string_list:
    if (  len(string) > len(longest_string)):
      longest_string = string
  
  return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))