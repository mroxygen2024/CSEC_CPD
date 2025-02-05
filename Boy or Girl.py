s=input()
l=[]
for i in s:
	l.append(i)
s=set(l)
count=0
for _ in s:
  count=count+1
if count%2==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
