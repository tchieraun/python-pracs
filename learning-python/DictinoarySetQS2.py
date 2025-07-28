# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key and marks as a value.

marks = {}
x= int(input("enter physics: "))
marks.update({ "physics" : x })

x= int(input("enter math: "))
marks.update({ "math" : x })
             
x= int(input("enter chemistry: "))
marks.update({ "chemistry" : x })

print(marks)