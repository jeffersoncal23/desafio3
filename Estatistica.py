import statistics

def moda(dicionario):
    frequencia = []
    for valor in dicionario.values():
        frequencia.append(valor)
    moda = statistics.mode(frequencia)
    return moda

def mediana(dicionario):
    frequencia = []
    for valor in dicionario.values():
        frequencia.append(valor)
    med = statistics.median(frequencia)
    return med

def desvio_padrao(dicionario):
    frequencia = []
    for valor in dicionario.values():
        frequencia.append(valor)
    desv_pad = statistics.stdev(frequencia)
    return desv_pad

def media(dicionario):
    frequencia = []
    for valor in dicionario.values():
        frequencia.append(valor)
    medi = statistics.mean(frequencia)
    return medi

def maior(dicionario):
    frequencia = []
    for valor in dicionario.values():
        frequencia.append(valor)
    maior = max(frequencia)
    return maior

def menor(dicionario):
    frequencia = []
    for valor in dicionario.values():
        frequencia.append(valor)
    menor = min(frequencia)
    return menor

def variancia(dicionario):
    frequencia = []
    for valor in dicionario.values():
        frequencia.append(valor)
    varianc = statistics.variance(frequencia)
    return varianc

def amplitude(dicionario):
    amplitude = maior(dicionario) - menor(dicionario)
    return amplitude