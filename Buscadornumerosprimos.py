def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def lista_primos_en_rango(rango_inicio, rango_fin):
    primos = []
    for numero in range(max(2, rango_inicio), rango_fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

rango_inicio = 10
rango_fin = 50

primos_en_rango = lista_primos_en_rango(rango_inicio, rango_fin)
print(primos_en_rango)
