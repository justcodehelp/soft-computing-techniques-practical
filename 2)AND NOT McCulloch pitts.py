num_ip=int(input("Enter the number of inputs:"))
w1=1
w2=1
x1=[]
x2=[]
for j in range(0,num_ip):
    ele1=int(input("x1="))
    ele2=int(input("x2="))
    x1.append(ele1)
    x2.append(ele2)
print("x1=",x1)
print("x2=",x2)
n=x1*w1
m=x2*w2

Yin=[]
for i in range(0,num_ip):
    Yin.append(n[i]+m[i])
print("After assuming one weight is excitatory and the other is inibibitory Yin=",Yin)
Y=[]
for i in range(0,num_ip):
    if(Yin[i]>=1):
        ele=1
        Y.append(ele)
    if(Yin[i]<1):
        ele=0
        Y.append(ele)
    print("Y=",Y)
