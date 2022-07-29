n1= 0
n2= 0
resultado = 0
operacao= ''

n1= int(input('Digite o n1:'))
operacao= input(int('Digite a operacao:'))
n2= int(input('Digite o n2:'))

if operacao == '+':
    resultado = n1+n2
elif operacao =='-':
    resultado = n1 - n2
elif operacao == '/':
    resultado = n1/n2
elif operacao == '*':
    resultado = n1*n2
else:
    resultado = 'Operação inválida'

print(str(n1) + '' + str(operacao) + '' + str(n2) + '=' + str(resultado) )
