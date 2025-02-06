# Write your solution here
def invert(dictionary: dict):
  new_dictionary = {}

  for key in dictionary:
    new_dictionary[dictionary[key]] = key

  dictionary.clear() 

  for item in new_dictionary:
    dictionary[item] = new_dictionary[item]


if __name__ == "__main__":
  s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
  invert(s)
  print(s)