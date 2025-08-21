from day_5 import student

student1= student("Jim","Business",3.1,False)
student2= student("Pam","Arts",3.5, False)
print(student1.name)
print(student1.gpa)
print(student2.name)
print(student2.gpa)

print(student2.on_honor_roll())