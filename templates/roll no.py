file = open(r"Roll_number.txt","w")
print("Enter the static format (like CSB19)")
string=input()
print("Enter the starting roll number :")
s=int(input())
print("Enter the ending roll number :")
e=int(input())
for i in range(s,e+1):
    if i<10:
        file.write(string+"00"+str(i)+"\n")
    elif i<100:
        file.write(string+"0"+str(i)+"\n")
    elif i<1000:
        file.write(string+str(i)+"\n")