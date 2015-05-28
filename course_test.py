import course
import quarter
import csv

courses_file = open('test_courses.csv', 'r')

"""
Part two uses schedule input file to fill lists of schedules by quarter
"""  

annualList = []

try:
    reader = csv.reader(courses_file)
    for row in reader:
        annualList.append(row)
finally:
    courses_file.close()

autumnCourses = []
springCourses = []

for i in annualList:

    if (i[4] == 'Autumn'):
        autCo = course.Course(i[0],i[1],i[2], i[3], i[4], i[5].replace(" ", ""), 'CSS')
        autumnCourses.append(autCo)

    if (i[4] == 'Spring'):
        sprCo = course.Course(i[0],i[1],i[2], i[3], i[4], i[5].replace(" ", ""), 'CSS')
        springCourses.append(sprCo)

autumn = quarter.Quarter(2016, 'Autumn', autumnCourses)
spring = quarter.Quarter(2016, 'Spring', springCourses)

print autumn.display()
print spring.display()

class Tests(object):
	def test_displaying_a_course():
		pass






