def digit_to_english(N):
    if (N >= 0 and  N <10):
        print("The ouput is :",words[N])
        if(N<0):
            abs(N)
            print("Invalid number")
    else:
        print("Invalid number")
        main()


words = {0:'Zero',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}


def main():
    num =int(input("please enter any number to be converted to words between 0-9:"))
    digit_to_english(num)
main()