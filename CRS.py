######### NO LONGER USED ####################
######### SAVED FOR HISTORY ####################

import numpy as N
import matplotlib.pyplot as plt
#import faculty

################################USER INPUT######################################
#facFile is input file for faculty
facFile = open('c:/Users/midfi_000/Desktop/faculty.txt', 'r')
#scheduleFile is input file for CSS schedule
scheduleFile = open('c:/Users/midfi_000/Desktop/schedule.txt', 'r')
################################USER INPUT######################################

class Faculty(object):
    """
    Faculty class contains all the information that makes up a faculty member.
    Class contains init method and a display method
    """
    def __init__(self, name, fullTime, classes,expertise1, expertise2, expertise3):
        self.name = name
        self.fullTime = fullTime
        self.classes = classes
        self.expertise1 = expertise1
        self.expertise2 = expertise2
        self.expertise3 = expertise3
        
    def display(self):
        return 'Faculty Name: ' + self.name \
        + ', Full Time? ' + self.fullTime \
        + ', Faculty member can teach ' + self.classes  + ' class(es)'\
        + ' with expertise in ' + self.expertise1 + ', ' \
        + self.expertise2 + ' and ' + self.expertise3

class Course(object):
    """
    Course class contains all information that makes up a course.
    Class contains init method and a display method
    """
    def __init__(self, courseNumber, time, day, cap, typeOfClass):
        self.courseNumber = courseNumber
        self.time = time
        self.day = day
        self.cap = cap
        self.typeOfClass = typeOfClass
        
    def display(self):
        return 'Course Number: ' + self.courseNumber + '\nTime: ' + \
        self.time + '\nDay: ' + self.day + '\nCap: ' + self.cap + \
        '\nTypeOfClass: ' + self.typeOfClass
    
    

################################# PART ONE #####################################
"""
Part one uses faculty input file to creat list of faculty members
"""        
data = facFile.readlines()            #read in faculty file
facFile.close()
dataSplit = []                 #list for individual faculty members from file
Facultylist = []           #list of Faculty objects

"""for loop to split individual faculty members from file"""
for i in range(len(data)):
    dataSplit.append(data[i].split())
del dataSplit[0]                #delete headings from file

"""for loop to create individual faculty objects and store them in list"""
for i in range(len(dataSplit)):
    dataSplit2 = dataSplit[i]
    facName = dataSplit2[0]
    facFullTime =  dataSplit2[1]
    facClasses = dataSplit2[2]
    facExpertise1 = dataSplit2[4]
    facExpertise2 = dataSplit2[5]
    facExpertise3 = dataSplit2[6]
    Facultylist.append(Faculty(facName,facFullTime,facClasses ,facExpertise1,facExpertise2,facExpertise3)) 

"""Displays all faculty member objects"""
for i in range(len(Facultylist)):
    print Facultylist[i].display()
    print

################################# PART TWO #####################################
"""
Part two uses schedule input file to fill lists of schedules by quarter
"""  

data2 = scheduleFile.readlines()        #read schedule file
scheduleFile.close()    
dataSplit3 = []                 #list to split inFile into individual courses
summerIndex = 0             # index for where summer schedule starts
autumnIndex = 0             # index for where autumn schedule starts
winterIndex = 0             # index for where winter schedule starts
springIndex = 0             # index for where spring schedule starts

""" loop that splits infile into individual courses"""
for i in range(len(data2)):
    dataSplit3.append(data2[i].split())

"""Loop to determine where each quarter starts"""
for i in xrange(len(dataSplit3)):
    if (dataSplit3[i] == ['Summer']):
        summerIndex = i
    if (dataSplit3[i] == ['Autumn']):
        autumnIndex = i
    if(dataSplit3[i] == ['Winter']):
        winterIndex = i
    if (dataSplit3[i] == ['Spring']):
        springIndex = i

"""Following four lines split annual schedule into quarterly schedules """  
summerSchedule = dataSplit3[summerIndex:autumnIndex]
autumnSchedule = dataSplit3[autumnIndex:winterIndex]
winterSchedule = dataSplit3[winterIndex:springIndex]
springSchedule = dataSplit3[springIndex:-1]

summerList = []             # list for summer classes
autumnList = []             # list for autumn classes          
winterList = []             # list for winter classes
springList = []             # list for spring classes

"""
Following sections split each quarters classes into objects that fill the 
Course class variables.
"""
#-----------------------------------SUMMER-------------------------------------#
for i in range(2,len(summerSchedule)):
    summerSplit = summerSchedule[i]
    #print summerSplit
    scheduleCourse = summerSplit[0]
    scheduleTime =  summerSplit[1]
    scheduleDay = summerSplit[2]
    scheduleCap = summerSplit[3]
    scheduleType = summerSplit[4]
    summerList.append(Course(scheduleCourse,scheduleTime,scheduleDay,scheduleCap,scheduleType))
""" 
for i in range(len(summerList)):
    print 'Summer Quarter:'
    print summerList[i].display()
    print  
"""
#-----------------------------------AUTUMN-------------------------------------#
for i in range(2,len(autumnSchedule)):
    autumnSplit = autumnSchedule[i]
    #print autumnSplit
    scheduleCourse = autumnSplit[0]
    scheduleTime =  autumnSplit[1]
    scheduleDay = autumnSplit[2]
    scheduleCap = autumnSplit[3]
    scheduleType = autumnSplit[4]
    autumnList.append(Course(scheduleCourse,scheduleTime,scheduleDay,scheduleCap,scheduleType))
"""  
for i in range(len(autumnList)):
    print 'Autumn Quarter:'
    print autumnList[i].display()
    print  
""" 
#-----------------------------------WINTER-------------------------------------#   
for i in range(2,len(winterSchedule)):
    winterSplit = winterSchedule[i]
    #print winterSplit
    scheduleCourse = winterSplit[0]
    scheduleTime =  winterSplit[1]
    scheduleDay = winterSplit[2]
    scheduleCap = winterSplit[3]
    scheduleType = winterSplit[4]
    winterList.append(Course(scheduleCourse,scheduleTime,scheduleDay,scheduleCap,scheduleType))

""" 
for i in range(len(winterList)):
    print 'Winter Quarter:'
    print winterList[i].display()
    print  
"""
#-----------------------------------SPRING-------------------------------------#    
for i in range(2,len(springSchedule)):
    springSplit = springSchedule[i]
    #print springSplit
    scheduleCourse = springSplit[0]
    scheduleTime =  springSplit[1]
    scheduleDay = springSplit[2]
    scheduleCap = springSplit[3]
    scheduleType = springSplit[4]
    springList.append(Course(scheduleCourse,scheduleTime,scheduleDay,scheduleCap,scheduleType))

"""
for i in range(len(springList)):
    print 'Spring Quarter:'
    print springList[i].display()
    print 
"""


def displayAll(list):
    for i in range(len(list)):
        print list[i].display()
        print  
            
print displayAll(winterList)    #display all summer courses
print springList[-1].courseNumber
print springList[-1].day

total = len(winterList) + len(summerList) + len(autumnList) + len(springList)

print total
