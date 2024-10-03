def intervalo(a, b):
    if a > b:
        return 'Valores inválidos' 
    return [b] + intervalo(a, b - 1)  

print(intervalo(5, -5))  
