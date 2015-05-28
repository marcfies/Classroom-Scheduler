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
        
    def display(self):
        return 'Course Number: ' + self.courseNumber + '\nTime: ' + \
            self.time + '\nDay: ' + self.day + '\nCap: ' + self.cap + \
            '\nTypeOfClass: ' + self.typeOfClass + '\nRelated Expertise: ' + \
            self.prefExpertise

                           