#Spencer Zahn - Python lesson 2 - Chapter 4 - Exercise 7 - 013118

#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
 
#Score   Grade
#> 0.9     A
#> 0.8     B
#> 0.7     C
#> 0.6     D
#<= 0.6    F
#Program Execution:
#Enter score: 0.95
#A
#Enter score: perfect
#Bad score
#Enter score: 10.0
#Bad score
#Enter score: 0.75
#C
#Enter score: 0.5
#F
#Run the program repeatedly to test the various different values for input.
def computegrade():
    try:
        grade = float(input("enter score: "))
        if grade <= 1.0 and grade >=0.9:
            print ("A")
        elif grade < 0.9 and grade >= 0.8:
            print ("B")
        elif grade < 0.8 and grade >= 0.7:
            print ("C")
        elif grade < 0.7 and grade >= 0.6:
            print ("D")
        elif grade < 0.6:
            print ("Fail")
        elif grade > 1.0:
            print ("Bad Score")
    except:
        print ("Bad Score")
        
computegrade()
