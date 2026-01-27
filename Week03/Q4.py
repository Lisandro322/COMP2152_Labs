#Question 4
mondayClass = {"Alice", "Bob", "Charlie", "Diana"}
wednesdayClass = {"Bob", "Diana", "Eve", "Frank"}

mondayClass.add("Grace")
print("Monday Class: ", mondayClass)
print("Wednesday Class: ", wednesdayClass)
bothClasses = mondayClass & wednesdayClass
print("Attended both class: ", bothClasses)
allStudent = mondayClass | wednesdayClass
print("All the students: ", allStudent)
onlyOne = mondayClass ^ wednesdayClass
print("Attended only one class: ", onlyOne)
print("Is Monday subset of all students?: ", mondayClass <= allStudent)