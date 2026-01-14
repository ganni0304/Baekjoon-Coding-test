H, M = map(int,input().split())

total = H*60 + M
new_total = total -45

if new_total >= 0:
    alh = new_total //60
    alm = new_total % 60
else:
    alh = 23
    alm = 60 + new_total
    
print(alh, alm)
