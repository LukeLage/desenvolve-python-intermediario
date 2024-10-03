def decimal_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_binario(n // 2) + str(n % 2)

def conversao(n):
    if n == 0:
        return '0'
    return decimal_binario(n)

print(conversao(37))  

