#error handling

try:
    divisionbyzero= 10/0
    number= int(input("Enter a number:"))
    print(number)

except ZeroDivisionError as err:
    print(err)
    #print("You can not divide by zero")
except ValueError:
    print("invalid input") 

#readingfiles
employee_file= open("/home/afraz/Downloads/jetsetgo/THE GRIND/employees.txt","r")
print(employee_file.readable()) #to check if its readable
#print(employee_file.read) 
#you get an error if you read 
#the entire file then read a 
# specific line because the pointer is already 
# at the end so i put it in the comments
print(employee_file.readline())#reads the first line 
print(employee_file.readline()) # if written again consectively reads again
#print(employee_file.readlines()) 
#reads all the lines, its in comment because of the reason mention above
print(employee_file.readlines()[1])#reads specific line in the file
#you can also use readlines func with a for loop
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


#writefiles
                                                                            #if you use w instead of a only the line you write will be written    
employee_file= open("/home/afraz/Downloads/jetsetgo/THE GRIND/employees.txt","a")
employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file.close()

#importing another file to use its functions
import calculatorself

print(calculatorself.calc())


#external modules
#make sure pip is installed
#pip -- version to check
#pip install to install pip
#pip install module name and it will install the module
#it will be installed in folder called site packages
# to import it u just use import name without python word in the start
#if you write modulename. it will stop there 


