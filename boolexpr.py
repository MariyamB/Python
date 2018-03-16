#source code:boolexpr.py
#name:Sai Ratnam Peri

def is_in_semester(month,day):

    while month==1 and (day>=29 and day<=31):
        return True
    while month==2 and (day>=1 and day<=28):
        return True
    while month == 3 and (day >=1 and day <= 31):
        return True
    while month == 4 and (day >=1 and day <= 30):
        return True
    while month == 5 and (day >=1 and day <= 31):
        return True

    return False


def main():
    month = int(input("input month 1-12:"))
    day =int(input("input day: "))
    print (is_in_semester(month,day))

if __name__ == '__main__':
    main()
