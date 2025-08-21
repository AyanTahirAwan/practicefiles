#dictionaries

monCon = {
    #key       #value
    #keys can be anything numbers or characters
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "June": "June",
    "July": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}
#             #key
print(monCon["Nov"])


#while loops

i =1
while i <= 10:
    print(i)
    i +=1
print("Done with loop") 

#forloops

for letter in "Girrafe":
    print (letter)

friends = ["Jim", "Karen","Kevin"]
for i in range(3,10):
    print(i) 

friends = ["Jim", "Karen","Kevin"]

for i in range(len(friends)):
    print(friends[i]) 

friends = ["Jim", "Karen","Kevin"]

for i in range(len(friends)):
    if i==0:
        print("First iteration")
    else:
        print("not first")


#exponent function
def power(base,pow):
    result= 1
    for i in range(pow):
        result= result*base
    return result
print(power(3,4))

#2D list

#normal list
nums= [1,2,3,4]

#2D
num_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num_grid[2][1])

#nested for loop
num_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
#normal forloop
for row in num_grid:
    print(row)


#nested
for row in num_grid:
    for col in row:
        print(col)