a,b,c = map(int,input().split()) 

money = 0 
if a == b and b == c: 
    money+= 10000 + a*1000 
elif a==b or b==c or a==c: 
    if a == b: 
        n = a 
    elif b == c: 
        n = b 
    elif a==c: 
        n = c 
    money += 1000+n*100 
else: 
    n = max(a,b,c) #내장함수 사용하기
    money += n*100 
    
print(money)