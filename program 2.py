import json ;
filename= open("file.txt")
data= filename.read()
file=open("sample Json2.json","w")
json.dump(data, file)
file.close()
print("JSON file Created Sussefully")
      
        
