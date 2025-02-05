n=int(input())
sum=0
for i in range(n):
   l = list(map(int, input().split()))
   if l.count(1)==2 or l.count(1)==3:
        sum=sum+1
print(sum)
