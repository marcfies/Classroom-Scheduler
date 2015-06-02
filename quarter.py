import numpy as N

class Quarter(object):
	"""
	Quarter class represents a given academic quarter at UWB. The courses
	offered during a quarter are stored as instances corresponding to one
	instance of the course in a quarter
	"""

	def __init__(self, year, season, courses):
		self.year = year
		self.season = season
		self.courses = courses

	def display(self):
		""" Displays the relevant information about this Quarter object

			Output:
				Currently displays the timing of the quarter and the 
				number of CSS courses being offered.
				TODO: Expand this display method to display more informative
					  stats and a visual representation of the offered courses
		"""
		return str(self.year) + ' ' + self.season + " Quarter:\n" + \
			str(len(self.courses)) + ' Courses \n'

	def resetQuarter(self):
		for al in self.courses:
			al.resetCourse()

	def getPreferredExpertise(self, expertise):
		""" Returns a list of all courses that rely on a given expertise

			Input:
				expertise = the string literal of the desired expertise

			Output:
				Returns a list that is a sublist of self.courses 
				of all courses who meet the expected criteria,
				currently in no particular order
		"""
		# initialize empty list for return value
		matchingCourses = []

		# loop through scheduled courses for those that meet the criteria
		for courseInst in self.courses:
			# course found when the desired expertise is present
			if (expertise == courseInst.prefExpertise):
				# add a reference to that course to the return list
				matchingCourses.append(courseInst)
		# return the list of courses, empty or not
		return matchingCourses



	def getExpertiseNeeds(self):
		""" returns a dictionary of all the expertises needed this quarter and
			their frequency
		"""
		exNeeds = {}

		for cour in self.courses:
			if (exNeeds.has_key(cour.prefExpertise)):
				exNeeds[cour.prefExpertise] += 1
			else:
				exNeeds[cour.prefExpertise] = 1

		return exNeeds






		