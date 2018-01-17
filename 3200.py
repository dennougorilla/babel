f = open('76-0.txt')
data1 = f.read()
f.close()
data2=[data1[i:i+3200] for i in range(0, len(data1), 3200)]

print data2[0]
aw=[]
for x in data2[0]:
    aw.append(ord(x))
    

print aw
print len(aw)
print len(data2)



