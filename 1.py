from random import randrange
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67]
s = ""
for i in range(500):
    s += str(p[randrange(len(p))])
mx_cnt = 0
h = [0]*90
for i in range(1, len(s)):
    h[int(s[i-1:i+1]) - 10] += 1
print(max(h))
# Рабин-Карп
res = 0 
for a in range(10):
    for b in range(10):
        t = str(10*a+b)
        cnt = 0
        for i in range(len(s)-1):
            if t == s[i:i+2]:
                cnt += 1
        res = max(res, cnt)        
print(res)

# Бойер-Мур
res = 0
for el in range(10, 100):
    el = str(el)
    cnt = 0
    i = 1
    while i < len(s)-1:
        if s[i] != el[1]:
            if s[i] == el[0]:
                i += 1
                if s[i] == el[1]:
                    cnt += 1
            else:
                i += 2
                continue
        else:
            if s[i-1] == el[0]:
                cnt += 1
        i += 1
    if s[len(s)-2:len(s)] == el:
        cnt += 1
    res = max(res, cnt)  
print(res)
# Кнут-Моррис-Прат
res = 0
for el in range(10, 100):
    el = str(el)
    cnt = 0
    pref = [0, 0]
    if el[0] == el[1]:
        pref[1] = 1
    i = 0
    while i < len(s)-1:
        k = 0
        if s[i] == el[0]:
            k = 1
        if s[i:i+2] == el:
            cnt += 1
            i += 1
            continue
        if (k-pref[k]+1) == 2:
            k -= 1
        i += (k-pref[k]+1)
    res = max(res, cnt)    
print(res)        
            
