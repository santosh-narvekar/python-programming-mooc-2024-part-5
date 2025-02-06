# Write your solution here
def factorials(n: int): 
  fact_dictionary = {}
  fact = 1

  for num in range(1, n + 1 ):
    fact +=  fact * (num - 1)
    fact_dictionary[num] = fact  

  return fact_dictionary

if __name__ == "__main__":
  k = factorials(5)
  print(k[1])
  print(k[3])
  print(k[5])