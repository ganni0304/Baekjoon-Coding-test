H, M = map(int,input().split())
C = int(input())

total = H*60+M
done_time = total+C

real_h = ( done_time // 60 ) % 24
real_m = done_time % 60



print(real_h, real_m)