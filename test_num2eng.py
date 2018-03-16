def test_47():
    assert num_to_english(47) == 'Fourty Seven'
def test_27():
    assert num_to_english(27) == 'Twenty Seven'
def test_7():
    assert num_to_english(7) == 'Seven'
def test_17():
    assert num_to_english(17) == 'Seventeen'
def test_33():
    assert num_to_english(33) == 'Thirty Three'
def test_50():
    assert num_to_english(50) == 'Fifty'
def test_10():
     assert num_to_english(10) == 'Ten'
def test_27():
    assert num_to_english(27) == 'Twenty Seven'
def test_99():
    assert num_to_english(99) == 'Ninety Nine'
def test_54():
    assert num_to_english(54) == 'Fifty Four'
def test_32():
    assert num_to_english(32) == 'Thirty Two'
def test_21():
    assert num_to_english(21) == 'Twenty One'
def test_22():
    assert num_to_english(22) == 'Twenty Two'
def test_43():
    assert num_to_english(43) == 'Fourty Three'
def test_56():
    assert num_to_english(56) == 'Fifty Six'
def test_12():
    assert num_to_english(12) == 'Twelve'
def test_13():
    assert num_to_english(13) == 'Thirteen'
def test_19():
    assert num_to_english(19) == 'Nineteen'
def test_90():
    assert num_to_english(90) == 'Ninety'
def test_100():
    assert num_to_english(15) == 'Fifteen'
def test_101():
    assert num_to_english(1) == 'One'

def num_to_english(N):
    words1 = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
              6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', \
              11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
              15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    words2 = ['Ten','Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if 0 <= N < 9:
        return(words1[N])
    elif 11 <= N <= 19 :
        tens, below_ten = divmod(N, 10)
        return (words1[N])
    elif 21 <= N <= 29 :
        tens, below_ten = divmod(N, 10)
        return(words2[tens - 1] + ' ' + words1[below_ten])
    elif 31 <= N <= 39:
        tens, below_ten = divmod (N, 10)
        return (words2[tens - 1] + ' ' + words1[below_ten])
    elif 41 <= N <= 49:
        tens, below_ten = divmod (N, 10)
        return (words2[tens - 1] + ' ' + words1[below_ten])
    elif 51 <= N <= 59:
        tens, below_ten = divmod (N, 10)
        return (words2[tens - 1] + ' ' + words1[below_ten])
    elif 61 <= N <= 69:
        tens, below_ten = divmod (N, 10)
        return (words2[tens - 1] + ' ' + words1[below_ten])
    elif 71 <= N <= 79:
        tens, below_ten = divmod (N, 10)
        return (words2[tens - 1] + ' ' + words1[below_ten])
    elif 81 <= N <= 89:
        tens, below_ten = divmod (N, 10)
        return (words2[tens - 1] + ' ' + words1[below_ten])
    elif 91 <= N <= 99:
        tens, below_ten = divmod (N, 10)
        return (words2[tens - 1] + ' ' + words1[below_ten])
    elif N%10 == 0:
        tens=int(N/10)
        return (words2[tens-1])
    else:
        return("Invalid")
