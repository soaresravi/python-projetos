# -*- coding: utf-8 -*-
"""for e while

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qxD2f7jHqDDpmD8cjnxmAuA56aidJtqQ
"""

soma= 0
for x in range(7):
  num= float(input("digite um número: "))
  soma+=num
print ("a soma dos números é ",soma)

x=1
maior= 0
soma= 0
menor= 10000000

while x <= 5:
  nome= str(input("digite o nome: \n"))
  sal= float(input("digite o salário: "))
  soma= soma + sal
  if (sal > maior):
    maior= sal
  if (sal < menor):
    menor= sal
  x+=1

print ("a soma de todos os salários é de R$",soma,"\n")
print ("a média de todos os salários é de R$",(soma/5),"\n")
print ("o maior salário é de R$",maior,"\n")
print ("o menor salário é de R$",menor)

pares= 0
impar= 0
for x in range(6):
  num= int(input("digite um número: "))
  if (num % 2 == 0):
    pares= pares + 1
  else:
    impar= impar + 1
print ("pares: ",pares)
print ("ímpares: ",impar)

import random

sorteado= random.randint(0,100)

num=0
tentativas=0
while (num != sorteado):
  num= int(input("digite um número sorteado sendo de 0 a 100: "))
  tentativas+=1

  if (num > sorteado):
    print ("o número sorteado é menor")
  elif (num < sorteado):
    print ("o número sorteado é maior")
  else:
    print ("parabéns! você acertou o número sorteado em ",tentativas," tentativas")

import random

cinco=0
tres=0

for x in range(1,21):
  sorteados= random.randint(0,10)
  print (x,"° número sorteado: ",sorteados)
  if sorteados > 5:
    cinco+=1
  if (sorteados % 3) == 0:
    tres+=1
print ("há ",cinco," números maiores que 5 dentre os sorteados")
print ("há ",tres," números divisíveis por 3 dentre os sorteados")

maior=0
menor=0

for x in range(1,8):
  produto= float(input("digite o preço do produto: "))
  if produto > maior:
    maior=produto
  if menor == 0:
    menor= produto
  if menor > produto:
    menor=produto
print ("o produto mais caro custa R$",maior)
print ("o produto mais barato custa R$",menor)

soma=0
mais_d_18=0
menos_d_5=0
maior=0

for x in range(1,10):
  idade= int(input("digite sua idade: "))
  soma+=idade
  if idade > 18:
    mais_d_18+=1
  if idade < 5:
    menos_d_5+=1
  if idade > maior:
    maior=idade
print ("a média das idades é de ",(soma/10)," anos")
print ("há ",mais_d_18," pessoas com mais de 18 no grupo")
print ("há ",menos_d_5," pessoas com menos de 5 no grupo")
print ("a pessoa mais velha tem ",maior," anos")

masc=0
fem=0
nb=0
media=0
vinte_m=0
quinze_nb=0
media_h=0

for x in range(5):
  idade= int(input("digite sua idade: "))
  gen= str(input("digite seu gênero: "))

  if gen == "masculino":
    masc+=1
    media_h+=idade
  elif gen == "feminino":
    fem+=1
    if idade > 20:
      vinte_m+=1
  else:
    nb+=1
    if idade > 15:
      quinze_nb+=1

  media+=idade
print (masc," homens foram cadastrados")
print (fem," mulheres foram cadastradas")
print (nb," não binários foram cadastrades")
print ("a média da idade do grupo é de ",(media/5)," anos")
print ("a média de idade dos homens é de ",(media_h/masc)," anos")
print ("no grupo tem ",vinte_m," mulheres com mais de 20 anos")
print ("no grupo tem ",quinze_nb," não binários com mais de 15 anos")

media=0
mais_d_90=0
osdois=0
osdois2=0

for x in range(7):
  peso= float(input("digite seu peso em KG: "))
  altura= float(input("digite sua altura em M: "))

  media+=altura

  if peso > 90:
    mais_d_90+=1
  if (peso < 50 and altura < 1.6):
    osdois+=1
  if (altura > 1.9 and peso > 90):
    osdois2+=1

print ("a média da altura do grupo é de ",(media/7)," metro")
print (mais_d_90," pessoas pesam mais de 90KG no grupo")
print (osdois," pessoas pesam menos de 50KG e medem menos de 1.6 metro no grupo")
print (osdois2," pessoas medem menos de 1.9 metro e pesam mais de 90KG no grupo")