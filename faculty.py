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
        self.courses = {'Summer':[],'Autumn':[],'Winter':[],'Spring':[]}
        self.maxClasses = 4
        if (self.fullTime == 'Y'):
            self.maxClasses = 4
        elif (self.fullTime == 'N'):
            self.maxClasses = 2
        
    def display(self):
        return 'Faculty Name: ' + self.name \
            + ', Full Time? ' + self.fullTime \
            + ', Faculty member can teach ' + self.numClasses  + ' class(es)'\
            + ' with expertise in ' + self.expertise1 + ', ' \
            + self.expertise2 + ' and ' + self.expertise3

    def clearFaculty(self):
        for quart in self.courses:
            del quart[:]

    def totalCourses(self):
        """ returns the number of classes currently assigned to for the year
        """
        count = 0.0
        for season in self.courses:
            count += len(self.courses[season])

        return count

    def addCourse(self, newCourse):
        """ Attempts to add a course to be taught for the quarter

            Input:
                newCourse = the course to be added to the faculty's schedule

            Output:
                Returns True on successful conditions to add the course,
                        False on failure due to space limits or time clash
        """

        # check that the faculty is able to teach another class this year
        yearFilled = float(self.totalCourses()) + 1.0
        # check that the quarter is filled
        quarterFilled = float(len(self.courses[newCourse.quarter]))
        if quarterFilled >= self.maxClasses:
            return False

        total = float(self.numClasses)
        if (yearFilled <= total):
            # print ((str(filled)) + ' ' + str(total) + '\n')
            # TODO: Check to confirm no two courses overlap time, and handle
            #       appropriately if it could be scheduled better

            # go through currently assigned courses for the quarter
            for t in self.courses[newCourse.quarter]:
                if ((newCourse.startTime >= t.startTime) & (newCourse.startTime <= t.endTime)):
                
                # if (newCourse.startTime == t.startTime):
                    tdays = t.day.lower().split('/')
                    newdays = newCourse.day.lower().split('/')
                    for n in tdays:
                        for p in newdays:
                            if (str(n) == str(p)):
                                return False

                else:
                    self.courses[newCourse.quarter].append(newCourse)
                    return True
            
            self.courses[newCourse.quarter] = [newCourse]
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
        
        if (len(self.courses[quarter]) > 0):
            print '-----------------------------------------------------------'
            print self.name + '\n' + str(self.fullTime)
            if (self.courses.has_key(quarter)):
                for s in self.courses[quarter]:
                    if (s.quarter == quarter):
                        print str(s.courseNumber) +': '+ str(s.startTime) + ' '+ str(s.endTime) + ' ' + str(s.day)
                print
        else:
            print '-----------------------------------------------------------'
            print self.name + '\n' + str(self.fullTime) 
            print self.expertise1
            print self.expertise2
            print self.expertise3
            print self.maxClasses
            print self.totalCourses()
            print










