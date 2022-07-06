#(n, m) = map(int, input().split())

n, m = (15, 45)

pattern = '.|.'
line = ''
for i in range(n):
    if i*2+1 == n:
        print('CHAEWON and MoM'.center(m, '-'))
    elif i*2 < n:
        print((pattern*(1+i*2)).center(m, '-'))
    else:
        print((pattern*((n-i)*2-1)).center(m,'-')) 