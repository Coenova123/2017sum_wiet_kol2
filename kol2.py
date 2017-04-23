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
import json
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--load', metavar='filename', help='load JSON from file')
group.add_argument('--save', metavar='filename', help='save JSON to file')
group.add_argument('--show', action="store_true", help='show loaded database')
group.add_argument('--add_student', metavar='student_name', help='add new student to database')
group.add_argument('--add_subject', nargs=2, metavar=('student_name', 'subject_name'),
                    help='match subject to student')
group.add_argument('--add_grade', nargs=3, metavar=('student_name', 'subject_name', 'grade'),
                    help='add new grade to students subject')
group.add_argument('--get_avg', nargs=2, metavar=('student_name', 'subject_name'),
                    help='return student average from selected subject')
group.add_argument('--get_avg_global', metavar='student_name', help='return total student average across subjects')
group.add_argument('--increase_attendance', nargs=2, metavar=('student_name', 'subject_name'),
                    help='increase student attendance at subject')
group.add_argument('--decrease_attendance', nargs=2, metavar=('student_name', 'subject_name'),
                    help='decrease student attendance at subject')
group.add_argument('--increase_absence', nargs=2, metavar=('student_name', 'subject_name'),
                    help='increase student absence at subject')
group.add_argument('--decrease_absence', nargs=2, metavar=('student_name', 'subject_name'),
                    help='decrease student absence at subject')

args = parser.parse_args()


class Diary(object):
	def __init__(self):
		self.students = {}

	def add_student(self, name):
		self.students.update({name: {}})  # {"subject": "", "Grades": []}

	def add_subject_to_student(self, name, subject_name):
		self.students[name].update({subject_name: {'Absence': 0, 'Attendance': 0, 'Grades': []}})

	def add_grade_to_subject_to_student(self, name, subject_name, grade):
		self.students[name][subject_name]['Grades'].append(grade)

	def get_student_avg_from_subject(self, name, subject_name):
		return float(sum(self.students[name][subject_name]['Grades'])) / len(self.students[name][subject_name]['Grades'])

	def get_student_avg_global(self, name):
		avg = []
		for key in self.students[name]:
			if len(self.students[name][key]['Grades']) != 0:
				avg.append(float(sum(self.students[name][key]['Grades']))/len(self.students[name][key]['Grades']))
		return float(sum(avg))/len(avg)

	def increase_student_attendance(self, name, subject_name):
		self.students[name][subject_name]['Attendance']+=1

	def decrease_student_attendance(self, name, subject_name):
		self.students[name][subject_name]['Attendance'] -= 1

	def increase_student_absence(self, name, subject_name):
		self.students[name][subject_name]['Absence']+=1

	def decrease_student_absence(self, name, subject_name):
		self.students[name][subject_name]['Absence'] -= 1

	def get_diary(self):
		return json.dumps(self.students)

	def save_json_dump(self, filename):
		json_file_dump = json.dumps(self.students, indent=4)
		f = open(filename, 'w')
		print >> f, json_file_dump
		f.close()

	def import_json(self,filename):
		json_data = open(filename).read()
		self.students = json.loads(json_data)


diary = Diary()
if args.load:
	diary.import_json(args.load)
if args.show:
	print diary.get_diary()
if args.add_student:
	diary.add_student(args.add_student)
if args.add_subject:
	diary.add_subject_to_student(args.add_subject[0], args.add_subject[1])
if args.add_grade:
	diary.add_grade_to_subject_to_student(args.add_grade[0], args.add_grade[1], float(args.add_grade[2]))
if args.get_avg:
	print diary.get_student_avg_from_subject(args.get_avg[0], args.get_avg[1])
if args.get_avg_global:
	print diary.get_student_avg_global(args.get_avg_global)
if args.increase_attendance:
	diary.increase_student_attendance(args.increase_attendance[0], args.increase_attendance[1])
if args.decrease_attendance:
	diary.decrease_student_attendance(args.decrease_attendance[0], args.decrease_attendance[1])
if args.increase_absence:
	diary.increase_student_absence(args.increase_absence[0], args.increase_absence[1])
if args.decrease_absence:
	diary.decrease_student_absence(args.decrease_absence[0], args.decrease_absence[1])

if args.save:
	diary.save_json_dump(args.save)
