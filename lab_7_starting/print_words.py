#
#   print_words.py:
#
#       Starting code for Lab 7-1 (Th)
#

FILENAME = 'words_2.txt'
# FILENAME = 'alice.txt'

def split_into_words(bstring):
    pass

def print_longest_1(all):
    longest_so_far = ''
    len_longest_so_far = 0

    # finish this

    print("Longest word is %s" % longest_so_far)  # b

def print_longest_2(all):
    len_list=[]
    for word in all:
        len_list.append((len(word),word))
    len_list.sort()
    print(len_list[-10:])
def print_longest_3(all):
    len_list=[(len(word),word)for word in all]
    len_list.sort ()
    print (len_list[-1:])
def print_first_last_equals (all,N):
    for word in all:
        if word[:N-1] ==word[-N:] and len(word )>N:
         print(word)
def main():

    fvar = open(FILENAME, 'r')  # open file for reading

    big_string = fvar.read()

    all_words = split_into_words(big_string)

    print_longest_1(all_words)
    print_longest_2(all_words)
    print_longest_3(all_words)

    print_first_last_equals(all_words,5)

    fvar.close()

main()