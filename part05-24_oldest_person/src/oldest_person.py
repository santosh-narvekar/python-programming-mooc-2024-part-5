# Write your solution here
def oldest_person(people: list):
  min_age = people[0][1]
  min_age_name = people[0][0]

  for person in people:
    if ( person[1] < min_age ):
      min_age = person[1]
      min_age_name = person[0] 

  return min_age_name

if __name__ == "__main__":
  p1 = ("Emily", 2014)
  p2 = ("Arthur", 1977)
  p3 = ("Ernest", 1985)
  p4 = ("Mary", 1953)
  p5 = ('Ellen', 1997)
  people = [p1, p2, p3, p4,p5]

  print(oldest_person(people))