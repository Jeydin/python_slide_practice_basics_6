# Slide 1

# Lists allow you to use one identifier (variable name)
# to group items together

students = ["Jason", "Jeydin", "Rohan"]

grades = [86, 89, 91]

# Slide 6

student_name1 = students[0] # Jason
student_grade1 = grades[0] # 86
student_grade3 = grades[2] # 89
print("Jasons grade is " + str(grades[0]))

# Slide 2-3

# Special list called an empty list
# Empty String
emp_string = ""
emp_list = []

myList = []
for char in "Mr. P's Computer Class":
	myList.append(char)

print(myList)

# Slide 4-5
# Indices

coworkers = ["Sarah", "Matt", "Sophie"]
coworkers[1] = "NEW EMPLOYEE"
print(coworkers)

print()

print(coworkers[int(18 / 9)])
print(coworkers[int(100 - 99)])
print(coworkers[int(22 % 2)])

# Slide 9
# FREQUENTLY USED METHODS
# list.append(x) = Adds x to the END of the list
# list.insert(i, x) = Inserts x at position in in list
# list.remove(x) = Removes the first item of the list whose values matches x
# list.pop(i) = Removes item at position i and returns it
# del list[i] = Removes item at position i
# len(list) = Length of list (counting items)

print()
coworkers = ["Sarah", "Matt", "Sophie"]

coworkers.append("Mr. P")
print(coworkers)

coworkers.insert(0, "Yo Momma")
print(coworkers)

coworkers.remove("Mr. P")
print(coworkers)

new_company = coworkers.pop(2)
print(new_company)
print(coworkers)

new_company_coworkers = [new_company, "Mr. P"]
print(new_company_coworkers)

del coworkers[2]
print()
print(new_company_coworkers)
print(coworkers)

new_company_coworkers.append(coworkers.pop(1))
print()
print(coworkers)
print(new_company_coworkers)

new_company_coworkers.append("Sophie")
print()
print(coworkers)
print(new_company_coworkers)

len_comp1 = len(coworkers)
len_comp2 = len(new_company_coworkers)

print("Yo Momma's company employees: " + str(len_comp1))
print("Matt's company employees: " + str(len_comp2))
