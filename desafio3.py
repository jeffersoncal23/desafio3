from Estatistica import media, moda, desvio_padrao, mediana, maior, menor, amplitude, variancia
produtos = {
    "Mesa de Escritório": 499.90,
    "Cadeira Gamer": 899.99,
    "Monitor LED": 1299.50,
    "Teclado Mecânico": 349.90,
    "Mouse sem Fio": 129.90,
    "Smartphone 5G": 3499.00,
    "Notebook Ultrafino": 4999.99,
    "Tablet Android": 1499.50,
    "Fone de Ouvido Bluetooth": 299.90,
    "Caixa de Som Portátil": 199.90,
    "Geladeira Duplex": 2999.90,
    "Fogão 4 Bocas": 1249.90,
    "Micro-ondas Inox": 599.90,
    "Cafeteira Elétrica": 349.90,
    "Aspirador de Pó": 899.90,
    "Ventilador de Mesa": 199.90,
    "Ar-condicionado Split": 2499.90,
    "Lâmpada Inteligente": 89.90,
    "Câmera de Segurança": 399.90,
    "Relógio de Parede": 59.90,
    "Jogo de Panelas": 499.90,
    "Copo Térmico": 89.90,
    "Caneca Personalizada": 29.90,
    "Mochila Escolar": 149.90,
    "Bolsa Feminina": 249.90,
    "Sapato Social": 199.90,
    "Tênis Esportivo": 299.90,
    "Livro de Ficção": 49.90,
    "Quadro Decorativo": 99.90,
    "Bola de Futebol": 79.90
}

print(media(produtos))
print(mediana(produtos))
print(moda(produtos))
print(variancia(produtos))
print(desvio_padrao(produtos))
print(amplitude(produtos))

print("""
1. Qual é a diferença entre média e mediana?

A média é uma medida de tendência central que representa o valor que cada elemento do conjunto teria se todos os valores fossem iguais.
A mediana, assim como a média, é uma medida de tendência centra, mas serve para representar o valor central de um conjunto de dados ordenados.

2. Por que a moda é importante?

A moda é importante porque mostra qual é o valor que mais se repete em um conjunto de dados, ou seja, é o valor que mais aparece.

3. Qual é o significado da variância?

A variância é uma medida de dispersão que mostra o quão distantes os valores de um conjunto de dados estão da média do conjunto.

4. Como o desvio padrão relaciona-se com a variância?

O desvio padrão, assim como a variância, é uma medida de dispersão. O desvio padrão e calculado extraindo a raiz quadrada da variância.
Isso ocorre pois, para cada parcela do cálculo da variância, é elevado ao quadrado a diferença entre  o elemento de um conjunto com a média (para que não haja valores negativos).
Assim, para normalizar a dimenção original, se extrai a raiz quadrada.
"""
)