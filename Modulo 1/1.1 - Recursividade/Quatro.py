def primo(n, i=2):
    if n <= 1:
        return 'Não é primo'
    if i > n**0.5:
        return 'É primo'
    if n % i == 0:
        return 'Não é primo'
    return primo(n, i + 1)  

print(primo(4))  
