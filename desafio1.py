alturacx = float(input('Digite a altura da sua caixa: '))
comprimentocx = float(input('Digite o comprimento da sua caixa: '))
profundidadecx = float(input('Digite a profundidade da sua caixa: '))
Hjanela = float(input('Digite a altura da janela: '))
Ljanela = float(input('Digite a base da janela: '))

areacx = alturacx * comprimentocx 
areaJ = Hjanela * Ljanela

if areaJ > areacx:
    print('S')
else:
    print('N')

# invés de float poderia ser usado int, para menor alocação de memória