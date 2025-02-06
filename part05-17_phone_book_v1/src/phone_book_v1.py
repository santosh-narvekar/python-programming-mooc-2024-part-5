# Write your solution here
user_dictionary = {}

while True:
  user_input = int((input("command (1 search,2 add,3 quit):")))

  if ( user_input == 2 ):
    user_name = input("name: ")
    user_number = input("number: ")
    user_dictionary[user_name] = user_number
    print("ok!")

  if (user_input == 1):
    user_search_name = input("name: ")
    if user_search_name in user_dictionary.keys():
      print(user_dictionary[user_search_name])
    else:
      print("no number")
  
  if (user_input == 3):
    print("quitting...")
    break
