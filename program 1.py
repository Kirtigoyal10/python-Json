import json ;
filename= open("file.txt")
data= filename.read()
w=data.split()
Words=[]
for i in w:
    if len(i)>8:
        Words.append(i)
for j in Words:
    print(j)
file=open("sample Json.json","w")
json.dump(Words, file)
file.close()
print("JSON file Created Sussefully")
      
        
