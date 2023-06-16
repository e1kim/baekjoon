#55-50+40+43-234-4241+3545
s = input()
s = list(s)

total = 0
digit = 1
new = list()
num = 0
for i in reversed(s):
    if i.isdigit() :
       num += int(i) * digit
       digit *= 10
    elif i == '-':
        new.insert(0,num)
        new.insert(0,i)
        digit = 1
        num = 0
        pass
    elif i == '+':
        new.insert(0,num)
        new.insert(0,i)
        digit = 1
        num = 0
        pass
new.insert(0,num)


minus = 0
for i in new:
    if i == '-':
        minus = 1
    elif i == '+':
        pass
    else:
        if minus == 1:
            total += i * -1
        else:
            total += i
print(total)    
        
