import numpy as N
import matplotlib.pyplot as plt
import csv
import faculty
import course
import quarter
import schedule

################################USER INPUT######################################
#facFile is input file for faculty
facFile = open('faculty.txt', 'r')
#scheduleFile is input file for CSS schedule
scheduleFile = open('classes.csv', 'r')
################################USER INPUT######################################    
    

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
    Facultylist.append(faculty.Faculty(facName,facFullTime,facClasses, \
        facExpertise1,facExpertise2,facExpertise3)) 

# """Displays all faculty member objects"""
# for i in range(len(Facultylist)):
#     print Facultylist[i].display()
#     print


################################# PART TWO #####################################
"""
Part two uses schedule input file to fill lists of schedules by quarter
"""  
annualList = []

try:
    reader = csv.reader(scheduleFile)
    for row in reader:
        annualList.append(row)
finally:
    scheduleFile.close()

summerCourses = []
autumnCourses = []
winterCourses = []
springCourses = []

for i in annualList:
    if (i[4] == 'Summer'):
        sumCo = course.Course(i[0],i[1],i[2], i[3], i[4], i[5].replace(" ", ""), 'CSS')
        summerCourses.append(sumCo)

    if (i[4] == 'Autumn'):
        autCo = course.Course(i[0],i[1],i[2], i[3], i[4], i[5].replace(" ", ""), 'CSS')
        autumnCourses.append(autCo)

    if (i[4] == 'Winter'):
        winCo = course.Course(i[0],i[1],i[2], i[3], i[4], i[5].replace(" ", ""), 'CSS')
        winterCourses.append(winCo)

    if (i[4] == 'Spring'):
        sprCo = course.Course(i[0],i[1],i[2], i[3], i[4], i[5].replace(" ", ""), 'CSS')
        springCourses.append(sprCo)

summer = quarter.Quarter(2016, 'Summer', summerCourses)
autumn = quarter.Quarter(2016, 'Autumn', autumnCourses)
winter = quarter.Quarter(2016, 'Winter', winterCourses)
spring = quarter.Quarter(2016, 'Spring', springCourses)

print summer.display()
print autumn.display()
print winter.display()
print spring.display()

nextYear = schedule.Schedule([autumn, winter, spring, summer], Facultylist)

############################### PART THREE ####################################
"""
Part two uses schedule input file to fill lists of schedules by quarter
"""  

nextYear.showStatistics()
nextYear.optimalSchedule(nextYear.quarters[0])
print nextYear.quarters[0].season
for prof in nextYear.instructors:
    prof.showClassSchedule(nextYear.quarters[0].season)

            
