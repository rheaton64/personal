# Ryan Heaton, myKingApp Server Test Code, 2019

# here's some super fun server code for interpreting assignment CSVs and turning them into dicts
# those dicts are then posted to the db as collections for future use
# don't get mad if it's bad code, I tried my best, I think it's spretty darn clever
import csv

class Assignment:
    
    def __init__(self, className, assType, assName,dateAss, weekdayDue):
        self.className = className
        self.assType = assType
        self.assName = assName
        self.dateAss = dateAss
        self.weekdayDue = weekdayDue

    def __str__(self):
        return "Class: " + self.className + " , Type: " + self.assType + " , Name: " + self.assName + " , Assign Date: " + self.dateAss + " , Due Date: " + str(self.weekdayDue)
    
    def toString(self):
        return self.className + ',,'+ self.assType + ',,' + self.assName + ',,' + self.dateAss + ',,' + str(self.weekdayDue)

# literally just declaring a bunch of variables fo use in the future
# if you enjoy the names, thank you, I did too, "assignments" have a conveniently fun abbreviation
name = ""
numAss = 0
week = ""
sunAss = []
monAss = []
tueAss = []
wedAss = []
thuAss = []
friAss = []
satAss = []
assForDay = [sunAss, monAss, tueAss, wedAss, thuAss, friAss, satAss]

def parseAssignments(startIndex, endIndex, arr, day):
    lenSect = endIndex - startIndex
    if lenSect < 5:
        assign = Assignment(arr[startIndex], "ERROR", "INVALID_DATA", "", day)
    else:
        if lenSect > 5:
            arr.pop(endIndex - 4)
            endIndex -= 1
        assign = Assignment(arr[startIndex], arr[startIndex+1], arr[startIndex+2], arr[endIndex-1], day)
    assForDay[day].append(assign.toString())
    if endIndex+1 != len(arr):
        parseAssignments(endIndex+1, arr.index('', endIndex+4), arr, day)

# now this is where the magic happens
# if you don't understand how this works, just google it, using the python "csv" library
with open('/Users/rheaton/Documents/code/personal/server/spencer_ass.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # first row, splitting it into an array of strings and pulling out the week because I'm too lazy to use substring
        if line_count == 0:
            splitStr = row[0].split()
            week = splitStr[8]
        # third row, holds the student name in there somewhere, pulling it out for future use
        if line_count == 2:
            name = row[0]
        # fourth row is the fun part, this has all the assingments held in it
        # The all have a bunch of different attributes that I am maticulously extracting and placing into an object
        # this object will be infinitely easier to use than the existing clump of string
        # ironic that I'm turning it right back into a clump of string later on, but such is life
        if line_count == 3:
            # if you're smart, you've already realized that "day" is a counter that keeps track of the working weekday
            day = 0
            for index in row:
                arr = index.split("\n")
                if len(arr) > 1:
                    parseAssignments(0, arr.index('', 4), arr, day)
                day += 1
        #else:
            #print(row)
        line_count += 1


# print(name)
# print(week)
# print("" + str(numAss) + " assignments this week")
# print("" + str(1 - len(assForDay[0])) + " assignements on Sunday")
# print(assForDay[0])
# print("")
# print("" + str(1 - len(assForDay[1])) + " assignements on Monday")
# print(assForDay[1])
# print("")
# print("" + str(1 - len(assForDay[2])) + " assignements on Tuesday")
# print(assForDay[2])
# print("")
# print("" + str(1 - len(assForDay[3])) + " assignements on Wednesday")
# print(assForDay[3])
# print("")
# print("" + str(1 - len(assForDay[4])) + " assignements on Thursday")
# print(assForDay[4])
# print("")
# print("" + str(1 - len(assForDay[5])) + " assignements on Friday")
# print(assForDay[5])
# print("")
# print("" + str(1 - len(assForDay[1])) + " assignements on Saturday")
# print(assForDay[6])

# turn each assignment into an assignemnt object, and look up python objects
# this way they can actually be properly organized and all that fun stuff
#organized like this:
# class, assType, assName, assDesc, dateAss, weekDayDue
# then, in the post, order them in that order with a string delimited by a ",,"

post = {
    "student_name": name,
    "date": week,
    "number_of_assignments": numAss,
    "assignmnets": assForDay
}

print(post)
print(assForDay[2][0])