limite = int(input('Digite um número limite para sequência Fibonacci: '))

# 0, 1, 1, 2, 3, 5 ...
count = 0
numAnt = 0
numPost = 1
print(numAnt, numPost)

while count <= limite:
    soma = numAnt + numPost
    numAnt = numPost
    numPost = soma
    print(soma)
    count += 1
