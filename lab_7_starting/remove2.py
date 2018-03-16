#
# Lab 7-3:
#
#   HTT9 Exercise 8, but for lists and elements
#

def squeeze_list(alist, elt):
    pass

def main():

    alist_str = input("Enter a list using [] and literal string: ")
    alist = eval(alist_str)
    elt = input("Enter a string to remove: ")

    print (squeeze_list(alist,elt))
main()
