import numpy as N
import matplotlib as plt
import random

class Schedule(object):
	"""

	"""
	def __init__(self, quarters, instructors):
		self.quarters = quarters
		self.instructors = instructors

	def showStatistics(self):
		""" Prints informative statistics of the annual schedule

			Output:
				Prints statistics to console 
		"""
		print 'Faculty members qualified to be considered an expert in a field'
		skills = self.expertiseAvailability()
		for skill in skills:
			print str(skill[0]) + ' ' + skill[1]
		disp = N.array(self.expertiseAvailability(), dtype='O')
		print disp
		self.allocateFacultyTime()

	def allocateFacultyTime(self):
		""" sets the number of courses each member of the faculty should teach
			per quarter
		"""
		# get faculty skill prevalence
		# [(2, 'Databases'), (2, 'Graphics')]
		order = self.expertiseAvailability()
		
		springNeeds = self.quarters['Spring'].getExpertiseNeeds()
		# print springNeeds


		# for experTuple in range(len(order)):
			# if the quarter has classes needing this skill
			# if (needs.has_key(order[experTuple][1])):



	def visualize(self):
		pass

	def getExperts(self, expertise):
		""" Returns a list of all current faculty with the given expertise

			Input:
				expertise = the string literal of the desired expertise

			Output:
				Returns a list that is a sublist of self.instructors 
				of all instructors who meet the expected criteria in
				no particular order
		"""
		# initialize empty list for return value
		fitFaculty = []

		# loop through schedule instructors for faculty who meet the criteria
		for faculty in self.instructors:
			if (expertise == faculty.expertise1 or \
				expertise == faculty.expertise2 or \
				expertise == faculty.expertise3):
				# when found, add a reference to that faculty to the new list
				fitFaculty.append(faculty)
		# return the list of faculty, empty or not
		return fitFaculty

	def getRandomExpert(self, expertise):
		""" Returns a random faculty member with the given expertise

			Input:
				expertise = the string literal of the desired expertise

			Output:
				Returns a random qualified member of the faculty as a faculty
				object
		"""
		pool = self.getExperts(expertise)
		index = random.randint(0,len(pool))
		return pool[index]

	def getExpertCommitment(self, expertise):
		""" returns a generated prediction of the number of courses available
			to be taught in one quarter for an expertise
		"""
		experts = self.getExperts(expertise)
		totalClasses = 0

		if (len(experts) != 0):
			for expert in experts:
				totalClasses += 1
				# TODO: account for full-time or not




	def expertiseAvailability(self):
		""" A list of available faculty expertise ordered least to most common

			Output: 
				Returns a list of tuples, with the first index being the
				number of faculty with an expertise, and the second index
				being the string name of the expertise
		"""
		# initialize an empty dictionary to store the occurring expertises
		expertiseFrequency = {}
		# loop through all instructors, keeping track of all expertise
		for instructor in self.instructors:
			
			# need to first check if the expertise has been added
			if expertiseFrequency.has_key(instructor.expertise1):
				# if so, increment its appearance count
				expertiseFrequency[instructor.expertise1] += 1
			else:
				# otherwise add it and set it at one appearance
				expertiseFrequency[instructor.expertise1] = 1
			
			# need to first check if the expertise has been added
			if expertiseFrequency.has_key(instructor.expertise2):
				# if so, increment its appearance count
				expertiseFrequency[instructor.expertise2] += 1
			else:
				# otherwise add it and set it at one appearance
				expertiseFrequency[instructor.expertise2] = 1
			
			# need to first check if the expertise has been added
			if expertiseFrequency.has_key(instructor.expertise3):
				# if so, increment its appearance count
				expertiseFrequency[instructor.expertise3] += 1
			else:
				# otherwise add it and set it at one appearance
				expertiseFrequency[instructor.expertise3] = 1

			# remove occurrences of 'None' expertise as it is irrelevant
			if (expertiseFrequency.has_key('None')):
				expertiseFrequency.pop('None')

			# convert the dictionary into a list of tuples, reverse the order
			expertiseFrequency.items()
			priorities = [(val, key) for key, val in expertiseFrequency.iteritems()]
		# sort the list by occurrences and return
		return sorted(priorities)


	def optimalSchedule(self, quarter):
		""" Determines and sets the values of the schedule instance to form
			a schedule that best utilizes faculty expertise

			Input: 
				quarter = the specific quarter of the annual schedule you want to
						  generate the schedule for

			Output:

		"""
		# initialize the availability list of expertises
		availability = self.expertiseAvailability()
		# loop through the expertises, beginning with the least common
		for expertiseTuple in range(len(availability)):
			# for each expertise, find the list of courses that require it
			for course in quarter.getPreferredExpertise(availability[expertiseTuple][1]):
				
				# attempt to assign the course to each qualified professor 
				# TODO: Randomize and distribute the classes among more faculty
				isAssigned = False
				potentialProfs = self.getExperts(availability[expertiseTuple][1])
				profIndex = N.random.randint(0, (len(potentialProfs) -1))
				while isAssigned == False:
					# create a list of professors with the specific expertise
					potentialProfs = self.getExperts(availability[expertiseTuple][1])
					# attempt to add the assign the course to the first 
					# qualified faculty
					if (potentialProfs[profIndex].addCourse(course)):
						# addCourse(course) == True means that the professor had 
						# room in their schedule to take the course
						course.isAssigned = True
						isAssigned = True
						break
					else:
						# addCourse(course) == False means that the professor 
						# was unable to teach the class due to space or time
						# conflicts, continue searching
						options = len(potentialProfs)
						# if there are no more options, ignore for now
						if (options > (profIndex + 1)):
							profIndex += 1
							# leave marked as unassigned for later
							isAssigned = False
							continue
						else:
							break
		# go back over courses left unassigned and assign to whoever has time
		c = 0
		for rest in quarter.courses:
			if (rest.isAssigned != True):
				# for now, simply go through all potentially available faculty
				# for free in self.instructors:
				print rest.courseNumber + ' ' + rest.prefExpertise
				c += 1
					# if (free.addCourse(rest)):
					# 	# mark as assigned and end search
					# 	rest.isAssigned = True
					# 	break
		print c


















