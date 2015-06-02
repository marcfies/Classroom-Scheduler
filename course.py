import numpy as N

class Course(object):
    """
    Course class contains all information that makes up a course.
    Class contains init method and a display method
    """

    def __init__(self, courseNumber, time, day, cap, quarter, prefExpertise, \
        typeOfClass):
        self.courseNumber = courseNumber
        self.time = time
        self.day = day
        self.cap = cap
        self.quarter = quarter
        self.prefExpertise = prefExpertise
        self.typeOfClass = typeOfClass
        self.isAssigned = False

        duration = self.parse_time(self.time)
        self.startTime = duration[0]
        self.endTime = duration[1]

    def display(self):
        """ Displays the formatted relevant information for the course

            Output:
            
        """
        return 'Course Number: ' + self.courseNumber + '\nTime: ' + \
            self.time + '\nDay: ' + self.day + '\nCap: ' + self.cap + \
            '\nTypeOfClass: ' + self.typeOfClass + '\nRelated Expertise: ' + \
            self.prefExpertise

    def resetCourse(self):
        self.isAssigned = False

    def parse_time(self, timeString):
        """ returns an int tuple of military start and end times
        """
        if (timeString != ''):
            times = timeString.split('-')
            return times
        else:
            return [0000,0000]    