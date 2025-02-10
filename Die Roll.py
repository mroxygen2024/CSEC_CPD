import math

def die_roll_probability(Y, W):
    min_win = max(Y, W)  
    favorable_outcomes = 6 - min_win + 1 
    gcd = math.gcd(favorable_outcomes, 6)
    numerator = favorable_outcomes // gcd
    denominator = 6 // gcd
    
    return f"{numerator}/{denominator}"
Y, W = map(int, input().split())
print(die_roll_probability(Y, W))
