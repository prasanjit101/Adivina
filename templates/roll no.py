file = open(r"Roll_number.txt","w")
print("Enter the static format (like CSB190)")
string=input()
print("Enter the starting roll number :")
s=int(input())
print("Enter the ending roll number :")
e=int(input())
for i in range(s,e+1):
    file.write(string+str(i)+"\n")