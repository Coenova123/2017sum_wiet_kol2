#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#TODO: total avg
#TODO: attendance


class Grade:
	def __init__(self,student,subject):
		self.student = student
		self.subject = subject
		self.grades = []
	def add_grade(self,grade):
		self.grades.append(grade)
	def get_grades(self):
		return self.grades
	def get_avg(self):
		return sum(self.grades)/float(len(self.grades))

class Student:
	def __init__(self,name,surname,index):
		self.name=name
		self.surname=surname
		self.index=index
		self.grades={}
	def get_student_name(self):
		return self.name
	def get_student_surname(self):
		return self.surname
	def get_student_index(self):
		return self.index	
	def set_subject(self,subject):
		self.grades[subject.get_subject_name()] = Grade(self,subject)
	def add_grade(self,subject,grade):
		self.grades[subject.get_subject_name()].add_grade(grade)
	def get_grades(self, subject):
		return self.grades[subject.get_subject_name()].get_grades()
	def get_avg(self, subject):
		return self.grades[subject.get_subject_name()].get_avg()
	def get_all_avg(self):
		avg = 0		
		for subject in self.grades:
			avg += subject.get_avg() ###REPAIR!!!
		avg=avg/float(len(grades))
class Subject:
	def __init__(self,subject_name):
		self.subject_name=subject_name
		self.student_list = [];
	def add_students(self,student):
		self.student_list.append(student)
		student.set_subject(self)
	def get_student_list(self):
		return self.student_list

	def get_subject_name(self):
		return self.subject_name
	def set_student_grade(self,student,grade):
		if student in self.student_list:
			student.add_grade(self,grade)
		

student1 = Student("Adam","Nowak",1234)
student2 = Student("Adam2","Nowak",1234)
przyra = Subject("przyra")
przyra.add_students(student1)
#przyra.set_student_grade(student2)
przyra.set_student_grade(student1,4)
przyra.set_student_grade(student1,5)

przyra1 = Subject("przyra")
przyra1.add_students(student1)
#przyra.set_student_grade(student2)
przyra1.set_student_grade(student1,1)
przyra1.set_student_grade(student1,2)
print student1.get_grades(przyra)
print student1.get_avg(przyra)
print student1.get_all_avg()
