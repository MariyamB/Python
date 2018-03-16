def tens_to_english(N):
    if (2 <=N < 10):
        N = N*10
        print("The ouput is :",words[N])
        if(N<0):
            abs(N)
            print("Invalid number")
    else:
        print("Invalid number")
        main()


words = {20:'Twenty',30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',80: 'Eighty', 90: 'Ninety'}


def main():
    num =int(input("please enter any number to be converted to words between 0-9:"))
    tens_to_english(num)
main()