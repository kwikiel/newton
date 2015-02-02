#init
total = 0
with open('euler13.txt') as f:
    lines = list(f)

for number in lines:
    total = total + long(number)

print total
