s=input()
c=0
for i in s:
    if s.count(i)==1:
        c+=1
if c==len(s):
    print("Yes")
else:
    print("No")
