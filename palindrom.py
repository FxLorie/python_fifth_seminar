## Задача на палиндром через срез

def pal(n):
    if len(n) == 0:
        return ''
    return n[-1:] + pal(n[:-1])
n = 'довод'
print(pal(n))

if n == pal(n):
    print('yes')
else: print('no')
