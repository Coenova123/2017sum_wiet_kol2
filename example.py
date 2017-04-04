#!/usr/bin/env python
from kol2 import *

#Test Students Init:
student1 = Student("Adam","Kot",1234)
student2 = Student("Tomek","Nowak",5678)
#Subject Init:
przyra = Subject("przyra")
religia = Subject("religia")

#Add students to classes
przyra.add_students(student1)
przyra.add_students(student2)
religia.add_students(student1)
religia.add_students(student2)

#Subject 1 set grades
przyra.set_student_grade(student1,4)
przyra.set_student_grade(student1,5)
przyra.set_student_grade(student2,1)
przyra.set_student_grade(student2,1)
przyra.set_student_grade(student2,1)


#Subject 2 set grades
religia.set_student_grade(student1,1)
religia.set_student_grade(student1,2)
religia.set_student_grade(student2,5)
print student1.get_grades(przyra)
print student1.get_avg(przyra)
print student1.get_all_avg()
przyra.add_presence(student1)
przyra.add_presence(student1)
przyra.add_presence(student1)
print "OBECENOSC:"
print przyra.get_presence(student1)
print "Religia avg:"
print religia.get_students_avg()
print "Przyra avg:"
print przyra.get_students_avg()
