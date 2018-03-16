score = int(input("enter the score:"))


if score>= 0 and score<= 100:
    if (90 <= score <= 100 ):
        print("Grade is A")
    elif (80 <= score <= 89 ):
        print("Grade is B")
    elif (70 <= score <= 79):
        print("Grade is C")
    elif (60 <= score <= 69):
        print("Grade is D")
    else:
        print("Grade is F")
else:
    print("Bad input")
