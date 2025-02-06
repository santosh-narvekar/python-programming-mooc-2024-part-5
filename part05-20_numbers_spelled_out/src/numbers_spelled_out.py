# Write your solution here
def number_to_word(number: int) -> str:
  ones_teen = ["zero","one","two","three","four","five","six","seven","eight","nine","ten",
               "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

  if ( number >= 0 and number <= 19 ): 
    return ones_teen[number]
  elif ( number >= 20 and number <= 99 ):
    if ( number % 10 == 0 ):
      return tens[int(str(number)[0])]
    else:
      return tens[int(str(number)[0])] + "-" + ones_teen[int(str(number)[1])]


def dict_of_numbers():
  numbers_dict = {}
  for key in range(0,100):
    numbers_dict[key] = number_to_word(key)

  return numbers_dict

if __name__ == "__main__":
  numbers = dict_of_numbers()
  print(numbers[2])
  print(numbers[11])
  print(numbers[45])
  print(numbers[99])
  print(numbers[0])