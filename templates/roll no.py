file = open(r"Roll_number.txt","a+")
print("Enter the static format (like CSB190)")
str=input()
print("Enter the starting roll number :")
s=int(input())
print("Enter the ending roll number :")
e=int(input())
for i in range(s,e+1):
    file.write(str+str(i)+"\n")