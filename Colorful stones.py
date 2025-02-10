s = input().strip()  
t = input().strip()  

moves = 0 

for i in range(len(t)):
    if moves < len(s) and s[moves] == t[i]:  
        moves += 1  

print(moves + 1)  