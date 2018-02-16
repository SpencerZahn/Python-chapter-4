#Spencer Zahn - Python lesson 2 - Chapter 4 - Exercise 6 - 013118

# 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
def computePay():
    y = float(input("Enter Rate: "))
    x = float(input("Enter time worked: "))
    if x > 40:
        z = y * x * 1.5 - 200
    else:
        z = y * x
    print ("Pay: " + str(z))
    
computePay()
