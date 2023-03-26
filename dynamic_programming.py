money=5
companies=3
F=[[0,3.22,3.57,4.12,4,4.85],[0,3.33,4.87,5.26,7.34,9.49],[0,4.27,7.64,10.25,15.93,16.12]]
x=[0,0,0]
z = [0, 0, 0, 0, 0, 0]
def fu(first_list,second_list,money):
    maximum=0
    j=0
    z = [0, 0, 0, 0, 0, 0,0]
    for i in range(money+1):
        while j+i<money+1:
            z[j+i]=max(first_list[i]+second_list[j],z[j+i])
            if first_list[i]+second_list[j]>maximum:
                maximum=first_list[i]+second_list[j]
                z[len(z)-1]=i
            j+=1
        j=0
    return z

while companies>0:
    for i in range(companies):
        z=fu(F[i],z,money)
    x[companies-1]=z[len(z)-1]
    money-=z[len(z)-1]
    z = [0, 0, 0, 0, 0, 0]
    companies-=1
print("Для максимально возможной прибыли нужно вложить",end="")
for i in range(len(x)):
    print(x[i]," единиц средств в ",i+1,"предприятие",end= ",")
maximum=0
for i in range(len(F)):
    maximum+=F[i][int(x[i])]
print("\nМаксимальная прибыль в таком случае  составит",maximum)

