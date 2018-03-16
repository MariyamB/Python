def teens_to_english(N):
    if (N >= 10 and N<20):
        print("The ouput is :",words[N])
        if(N<0):
            abs(N)
            print("Invalid number")
    else:
        print("Invalid number")
        main()


words = {10:'Ten',11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}


def main():
    num =int(input("please enter any number to be converted to words between 10-19:"))
    teens_to_english(num)
main()