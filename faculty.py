import numpy as N

class Faculty(object):
    """
    Faculty class contains all the information that makes up a faculty member.
    Class contains init method and a display method
    """
    def __init__(self, name, fullTime, numClasses,expertise1, expertise2, expertise3):
        self.name = name
        self.fullTime = fullTime
        self.numClasses = numClasses
        self.expertise1 = expertise1
        self.expertise2 = expertise2
        self.expertise3 = expertise3
        self.courses = [] 
        
    def display(self):
        return 'Faculty Name: ' + self.name \
            + ', Full Time? ' + self.fullTime \
            + ', Faculty member can teach ' + self.numClasses  + ' class(es)'\
            + ' with expertise in ' + self.expertise1 + ', ' \
            + self.expertise2 + ' and ' + self.expertise3

    def addCourse(self, newCourse):
        """ Attempts to add a course to be taught for the quarter

            Input:
                newCourse = the course to be added to the faculty's schedule

            Output:
                Returns True on successful conditions to add the course,
                        False on failure due to space limits or time clash
        """

        # check that the faculty is able to teach another class this quarter
        filled = float(len(self.courses)) + 1.0
        total = float(self.numClasses)
        if (filled <= total):
            print ((str(filled)) + ' ' + str(total) + '\n')
            # TODO: Check to confirm no two courses overlap time, and handle
            #       appropriately if it could be scheduled better
            self.courses.append(newCourse)
            return True
        else:
            # return false on failed addition to this faculty's schedule
            return False

    def showClassSchedule(self, quarter):
        """ Prints the faculty's name and courses teaching for the given
            quarter

            Output:
                Currently lists the course data for any courses assigned to 
                the faculty
                TODO: Add visualization of this schedule to show a weekly
                      schedule
        """

        for s in self.courses:
            if (s.quarter == quarter):
                print s.display()

        # loop through all courses assigned to the faculty
        # for course in self.courses:
        #     # then call their display method
        #     print course.display()










