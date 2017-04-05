def soma(s, n):
    if n == 0:
        return s
    return soma(s+n, n-1)

n = int(input("Informe um número:\n"))

print(soma(0, n))
