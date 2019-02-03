name = input("Enter file:")
handle = open(name)
dict = {}

# Here basically time occurs in the file in the format hh:mm:ss for example :- 
# 09:02:13 which gets extracted through position of ':' a.k.a frequency of '09' is then put into dict

for line in handle:
    if line[line.find(":")-2:line.find(":")] not in dict:
        dict[line[line.find(":")-2:line.find(":")]]=0
    dict[line[line.find(":")-2:line.find(":")]]+=1
#print(dict)
keylist = dict.keys()
#print(keylist)
keylist.sort()
#print(keylist)
for key in keylist:
    print(key,dict[key])
