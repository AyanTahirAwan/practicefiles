from math import *
def calc():
    
    while True:
            select_op= str(input("Select operation:"))

            if select_op == 'Q':
                 print("Goodbye.")
                 break

            if select_op not in {'+', '-', '*', '/', '%'}:
                 print("Invalid operation. Try again.")
                 continue
            try:
               first_num=float(input("Enter first number:"))
               sec_num=float(input("Enter second number:"))
            except ValueError:
                 print("Please enter valid numbers.")
                 continue
            if select_op == '+':
                sum=first_num + sec_num
                print(sum) 
            elif select_op == '-':
                diff= first_num - sec_num
                print(diff)

            elif select_op =='*':
                product=first_num * sec_num
                print (product)

            elif select_op == '/':
                if sec_num==0:
                    print(" Division with 0 not allowed.")
                    continue
                divide= first_num/sec_num
                print(divide) 

            elif select_op == '%':
                if sec_num==0:
                    print(" Division with 0 not allowed.")
                    continue
                remainders= first_num % sec_num
                print(remainders) 

            
calc()