def julian(day,month,year):
        daynum = 31 * (month - 1) + day
        if (month <= 2):
            print(daynum)
        elif (year % 400 == 0) and month >2:
            daynum = daynum - ((4 * month + 23) // 10)+1
            print(daynum)
        elif (year % 100) == 0 and month >2:
            daynum = daynum - ((4 * month + 23) // 10)
            print(daynum)
        elif (year % 4) == 0 and month >2:
            daynum = daynum - ((4 * month + 23) // 10) + 1
            print(daynum)
        else:
            daynum = daynum - ((4 * month + 23) // 10)
            print(daynum)


def main():

   day = int(input("Enter the day between 1 and 31:"))
   month = int(input("enter month between 1 and 12:"))
   year = int(input("Enter the year:"))
   julian(day,month,year)


if __name__ == '__main__':
        main()
