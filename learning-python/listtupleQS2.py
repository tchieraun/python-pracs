#QS2: WAP to check if a list contain palindrome of element. (Hint: use copy() method.

list1 = [1, 2 , 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT pelidrome")

