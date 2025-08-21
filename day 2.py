listofnum = [1,2,3,4,5]
listofpeople= ["Ayan" , "zain", "Jamal"]

friends= ["Kevin", 1, False]

print (friends)
print(friends[0])

print(friends(-1))
print(friends[1:])
print(friends[1:3])
friends[1]= "Mike"
print(friends)

friends.extend(listofnum)
friends.append("CREED")
friends.insert(1, "Kelly")
friends.remove("Zain")
friends.pop("Zain")
print(friends.index("Mike"))
friends.sort()
listofnum.sort()
listofnum.reverse()
friends2 = friends.copy()

#tuple
coordinates=(4,5)
print (coordinates[1])

#funcions

def sayhi(name, age):
    print("Hey you"+name+"your age is"+str(age))
sayhi("Mike",18)

#return
def cube (num):
     return num*num*num
print(cube(4))

#if else statements
is_male = True
is_tall = False
if is_male or is_tall:
     print("Youre a man or tall or both")
elif is_male and not (is_tall):
     print("You are a short man")    
elif not is_male and (is_tall):
     print("You are tall but not a man")
else:
     print("Youre not a man nor tall")

def max(num1 , num2 ,num3):
     if num1 >= num2 and num1>= num3:
          return num1
     elif  num2 >= num1 and num2>= num3:
            return num2
     else:
        return num3
     
