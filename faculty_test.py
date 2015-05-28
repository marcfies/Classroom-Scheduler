import faculty
import csv

faculty_file = open('test_faculty.txt', 'r')

################################# PART ONE #####################################
"""
Part one uses faculty input file to creat list of faculty members
"""        
data = faculty_file.readlines()            #read in faculty file
faculty_file.close()
dataSplit = []                 #list for individual faculty members from file
Facultylist = []           #list of Faculty objects

# """for loop to split individual faculty members from file"""
for i in range(len(data)):
    dataSplit.append(data[i].split())
del dataSplit[0]                #delete headings from file

# """for loop to create individual faculty objects and store them in list"""
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
for i in range(len(Facultylist)):
    print Facultylist[i].display()
    print

class Tests(object):
	def test_adding_a_course():
		pass
	def test_showing_a_schedule():
		pass
