#!/usr/bin/env python
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

'''
Adding new student:
student_ID = Student("Name","Surname",Index)

Adding new subject:
subject_ID = Subject("Subject Name")

Connect student to subject:
subject_ID.add_students(student_ID)

Add new grade:
subject_ID.set_student_grade(student_ID,Grade)

Get student grades from subject:
student_ID.get_grades(subject_ID)

Get average grade from subject:
student_ID.get_avg(subject)

Get all student average across subjects:
student_ID.get_all_avg()

Add presence (attendance):
subject_ID.add_presence(student_ID)

Get student presence:
subject_ID.get_presence(student_ID)

'''

'''Grade class is responsible for storing grades and students attendance per student/subject'''
class Grade:
	def __init__(self,student,subject):
		self.student = student
		self.subject = subject
		self.grades = []
		self.attendance = 0
	def add_grade(self,grade):
		self.grades.append(grade)
	def get_grades(self):
		return self.grades
	def get_avg(self):
		return sum(self.grades)/float(len(self.grades))
	def add_presence(self):
		self.attendance+=1
	def get_presence(self):
		return self.attendance
'''Student class is responsible for storing student data and connection between subject and grades'''
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
			avg+=self.grades[subject].get_avg()
		return avg/float(len(self.grades))
	def add_presence(self,subject):
		self.grades[subject.get_subject_name()].add_presence()
	def get_presence(self,subject):
		return self.grades[subject.get_subject_name()].get_presence()
'''Subject class is responsible for storing information about subject and students signed for classes'''
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
	def get_students_avg(self):
		avg=0
		for student in self.student_list:
			avg+=student.get_avg(self)
		return avg/float(len(self.student_list))
	def add_presence(self,student):
		student.add_presence(self)
	def get_presence(self,student):
		return student.get_presence(self)


