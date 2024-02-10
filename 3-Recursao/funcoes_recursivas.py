def regressiva(i):
    print(i)
    if(i <= 0): # caso-base
        return 
    else: # caso recursivo
        regressiva(i-1)

def fatorial(n):
    if(n == 1):
        return 1
    else:
        return n * fatorial(n - 1)

regressiva(10)
print(fatorial(5))