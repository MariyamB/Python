
def isLeap(year):

        if y % 400 == 0:
            return True
        if y % 100 == 0:
            return False
        if y % 4 == 0:
            return True
        else:
            return False

y = int(input("Enter the year:"))
print(isLeap(y))