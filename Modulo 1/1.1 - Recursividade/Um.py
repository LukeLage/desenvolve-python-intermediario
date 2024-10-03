def intervalo(a, b):
    if a > b:
        return 'Valores inválidos'
    if a == b: 
        return [b]
    return [b] + intervalo(a, b - 1)  

print(intervalo(-5, 5)) 

