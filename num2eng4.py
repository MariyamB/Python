def num_to_english(N):
    words1 = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
              6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', \
              11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
              15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    words2 = ['Ten','Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if 0 <= N < 9:
        print("The ouput is :",words1[N])
    elif 11 <= N <= 19 :
        tens, below_ten = divmod(N, 10)
        print ( "The output is :",words1[N])
    elif 21 <= N <= 29 :
        tens, below_ten = divmod(N, 10)
        print("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
    elif 31 <= N <= 39:
        tens, below_ten = divmod (N, 10)
        print ("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
    elif 41 <= N <= 49:
        tens, below_ten = divmod (N, 10)
        print ("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
        print (words2[tens - 2] + '' + words1[below_ten])
    elif 51 <= N <= 59:
        tens, below_ten = divmod (N, 10)
        print ("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
    elif 61 <= N <= 69:
        tens, below_ten = divmod (N, 10)
        print ("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
    elif 71 <= N <= 79:
        tens, below_ten = divmod (N, 10)
        print ("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
    elif 81 <= N <= 89:
        tens, below_ten = divmod (N, 10)
        print ("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
    elif 91 <= N <= 99:
        tens, below_ten = divmod (N, 10)
        print ("The output is :", words2[tens - 1] + ' ' + words1[below_ten])
    elif N%10 == 0:
        tens=int(N/10)
        print ("The output is :", words2[tens-1])
    else:
        print("Invalid")


def main():
   num =int(input("please enter any number to be converted to words between 0-100:"))
   num_to_english(num)

if __name__ == '__main__':
   main()
