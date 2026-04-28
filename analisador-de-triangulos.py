print ('=-=' * 20)
print ('SEJA BEM-VINDO AO FORMANDO TRIÂNGULOS'.center(60))
print ('=-=' * 20)
print ()
print ('Bem-vindo ao programa "Formando Triângulos", onde dizemos se é possível ou não formar triângulos com os valores que você quiser, além de dizer seu tipo!')
print ('Para começar, por favor:')
print ()

n1 = float (input ('Primeiro valor: '))
n2 = float (input ('Segundo valor: '))
n3 = float (input ('Terceiro valor: '))

from time import sleep
print ('ANALISANDO VALORES..')
sleep(2)
print ()

if n1 < n2 +n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print ('Esses valores podem formar um triângulo!')
    if n1 == n2 == n3:
        print ('Esse triângulo é EQUILÁTERO!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print ('Esse triângulo é ISÓCELES!')
    else:
        print ('Esse triângulo é ESCALENO!')
else:
    print ('Esses valores não podem formar um triângulo!')
