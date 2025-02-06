# Write your solution here
def histogram(string: str):
  string_checker = [] 

  for element in string: 
    if element not in string_checker:  
      print(element,"*" * string.count(element))
    string_checker.append(element) 

if __name__ == "__main__":
  #histogram("abba")
  histogram("statistically")