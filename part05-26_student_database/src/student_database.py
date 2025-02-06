# Write your solution herd

def add_student(students:dict,student_name:str):
  students[student_name] = { 
    "completed courses":[],
    "avg":0.0
  }

def add_course(students:dict,student_name:str,course:tuple):
  completed_courses = students[student_name]["completed courses"]
  if ( course[1] == 0 ): return False

  # if course already exists check the grade
  # if new grade less than old course, set new course to old course
  # else remove old course and use new course

  for cur_course in completed_courses:
    if ( course[0] == cur_course[0]  ):
      if course[1] < cur_course[1]:
        course = cur_course
      else:
        completed_courses.remove(cur_course)

  # check if the course doesn't exist already
  if (course not in completed_courses):
    completed_courses.append(course)
  
  sum = 0

  for course in completed_courses:
    sum += course[1]

  students[student_name]["avg"] = sum / len(completed_courses) 

def print_student(students:dict,student_name:str):

  if ( student_name in students ) :
    completed_courses = students[student_name]["completed courses"]
    average = students[student_name]["avg"]
    print(f"{student_name}:")
    
    if ( completed_courses == [] ):
      print(f" no completed courses")
    else:
      print(f" {len(completed_courses)} completed courses:")
      for course in completed_courses:
        print(f"  {course[0]} {course[1]}")
      print(f" average grade {average}")
      
  else:
    print(f"{student_name}: no such person in the database")

def summary(students:dict):
  print(f"students {len(students.keys())}")
  
  student_course_data = []
  student_avg_data = []

  for student_name,student_data in students.items():
    student_course_data.append((student_name,len(student_data["completed courses"])))
    student_avg_data.append((student_name,student_data["avg"]))  
  
  max_courses_done_by = student_course_data[0][0]
  max_courses_done_length = student_course_data[0][1]

  for student_detail in student_course_data:
    if student_detail[1] > max_courses_done_length:
      max_courses_done_length = student_detail[1]
      max_courses_done_by = student_detail[0]
  
  best_avg_student = student_avg_data[0][0]
  best_avg = student_avg_data[0][1]

  for student_avg_detail in student_avg_data:
    if student_avg_detail[1] > best_avg:
      best_avg = student_avg_detail[1]
      best_avg_student = student_avg_detail[0]

  print(f"most courses completed {max_courses_done_length} {max_courses_done_by}")
  print(f"best average grade {best_avg} {best_avg_student}")


if __name__ == "__main__":
  students = {} 
  
  add_student(students, "Peter")
  add_student(students, "Eliza")
  add_course(students, "Peter", ("Data Structures and Algorithms", 1))
  add_course(students, "Peter", ("Introduction to Programming", 1))
  add_course(students, "Peter", ("Advanced Course in Programming", 1))
  add_course(students, "Eliza", ("Introduction to Programming", 5))
  add_course(students, "Eliza", ("Introduction to Computer Science", 4))
  print_student(students,"Peter")
  
  #add_student(students, "Peter")
  #add_course(students, "Peter", ("Software Development Methods", 5))
  #add_course(students, "Peter", ("Software Development Methods", 1))
  #print_student(students, "Peter")