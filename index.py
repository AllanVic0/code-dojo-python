dic = {}

i = int(input('Digite quantos pares de calçados tem: '))
for _ in range(0,i):
    calc = input("Digite o tamanho e o lado do calçado: ")
    tamanho, lado = calc.split()
    if lado not in dic:
        dic[lado] = [tamanho]
    else:
        dic[lado].append(tamanho)
        
print(i)
print(dic)


