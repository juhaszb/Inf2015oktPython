import random
import linecache


randomszam=random.randrange(1,3)
if randomszam==1 :
    fvi="I"
else:
    fvi="F"

tipp=input("Kerek egy tippet:")

if tipp==fvi :
    print("Eltalalta")
else :
    print("Nem talalta el")

k=0
with open("kiserlet.txt") as infile:
    for line in infile:
        k+=1
print(k)
fej=0
with open("kiserlet.txt") as infile:
    for line in infile:
        if line=="F\n":
            fej+=1
print(round((fej/k)*100,2))
van=0
szamol=0
i=0
file = open("kiserlet.txt")

for i, line in enumerate(file):
    if linecache.getline("kiserlet.txt",i)=="F\n" and linecache.getline("kiserlet.txt",i+1)=="F\n" and linecache.getline("kiserlet.txt",i+2)!="F\n" and linecache.getline("kiserlet.txt",i-1)!="F\n":
        van+=1
    linecache.clearcache()
file.close()
        
print(van)

fileuj= open("kiserlet.txt")
hosszu=1
T=[]
for i, line in enumerate(fileuj):
    if linecache.getline("kiserlet.txt",i)=="F\n" and linecache.getline("kiserlet.txt",i+1)=="F\n":
        hosszu+=1
    if linecache.getline("kiserlet.txt",i)=="I\n":
        T+=[hosszu]
        hosszu=1
    linecache.clearcache()

print(max(T))

