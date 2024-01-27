def decor(uskor):
    def wrapper(v0,v,t):
        S=(v0*t)+((uskor(v0,v,t)*t*t)/2)
        print('S: ',S)
    return wrapper

@decor
def uskor(v0,v,t):
    a=(v-v0)/t
    print('a: ',a)
    return a

try:
    v0=int(input())
    v=int(input())
    t=int(input())
    uskor(v0,v,t)
except ValueError:
    print("Нельзя вводить строки")
except ZeroDivisionError:
    print("Время не может быть равным нулю")





