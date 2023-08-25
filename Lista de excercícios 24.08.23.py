# -*- coding: utf-8 -*-
'''
Created on Wed july 10 2023

@author: Prof Eder Cassettari

Apostila do curso de Python - Computational Thinking with Python

FIAP - Engenharia de Software - resolucao da apostila

SEGUNDO SEMESTRE
EXERCICIOS DE FUNÇÃO
'''

#importação de bibliotecas
import math
import Numpy as np
import Pandas as pd
import matplotlib as plt




# Exemplo de definição de função no Python

def soma(a, b):
    resultado = a + b
    return resultado

s = soma (1,2)
print(s)


# Outro exemplo de definição de função no Python


# Outro exemplo ainda de definição de função no Python sem colocar parâmetros

print(' -'*30)
print('          Vinheria Agnello')
print(' -'*30)
print('')
print(' -'*30)
print('          Promoção de vinhos - queima de estoque')
print(' -'*30)


def linha_separacao():
    return print(' -'*30)

linha_separacao()

print('          Promoção de vinhos - queima de estoque')    

linha_separacao()

print('          Promoção de vinhos - Queima de Estoque')
linha_separacao()



# Exercicio 1 - Crie uma Função para calcular o dobro de um número


# Definição de função

def dobrar_numero():
    numero = float(input("Digite um número: "))
    resultado = numero * 2
    return resultado

print(' O dobro do número é:   ',dobrar_numero())



#  Exercicio 2 - Crie uma função que soma dois números inteiros 

# Definição de função
def somar_numeros():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    resultado = numero1 + numero2
    return resultado

print(' A soma dos numeros é:   ',somar_numeros())



#  Exercicio 3 - Crie uma função que forneça o módulo do número

# Definição de Função

def valor_absoluto():
    numero = float(input("Digite um número:  "))
    resultado = abs(numero)
    return resultado

print(' O modulo do número é:  ',valor_absoluto())



#  Exercicio 4 - Crie uma função que forneça o quadrado do número

# Definição de Função

def quadrado_de_n():
    numero = float(input("Digite um número: "))
    resultado = numero ** 2
    return resultado

print(' O módulo do número é:  ',quadrado_de_n())



 #  Exercicio 5 - Crie um código para calcular o Fatorial de um número

# Definição de função
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input('Digite o número que vc quer calcular o fatorial:  '))

print("O fatorial de", n, "é", fatorial(n))


#  Exercicio 6 - Crie uma função que retorna o maior entre dois números:

# Definição de função
    
def busca_maior():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if numero1 > numero2:
        return numero1
    else:
        return numero2

print(' O maior numero é:  ',busca_maior())



#  Exercicio 7 - Crie uma função que retorne o antecessor do número

# Definição de função
def buscar_antecessor():
    numero = float(input("Digite um número: "))
    antecessor = numero - 1
    return antecessor

print(' O antecessor é:  ',buscar_antecessor())



#  Exercicio 8 - Crie uma função que retorna o menor entre dois números

# Definição doe função

def buscar_menor():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if numero1 < numero2:
        return numero1
    else:
        return numero2

print('o número menor é: ', buscar_menor())



#  Exercicio 9 - Crie uma função que verifica se um número é par:

# Definição de Função

def verificar_par():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        return print('O numero é par!')
    else:
        return print('O numero é impar!')

print(verificar_par())



#  Exercicio 10 - Crie uma função para calcular a raiz quadrada de um número:

import math

    
# Definição de Função


def calcular_raiz_quadrada():
    numero = float(input("Digite um número: "))
    raiz_quadrada = math.sqrt(numero)
    return raiz_quadrada

print('A raiz quadrada é: ',calcular_raiz_quadrada())
      

# Exercicio 11 - Crie um código para somar dois números complexos

# Definição de Função

def somar_numeros_complexos(num1, num2):
    real = num1[0] + num2[0]
    imaginaria = num1[1] + num2[1]
    resultado = (real, imaginaria)
    return resultado

# Solicita as partes real e imaginária do primeiro número complexo ao usuário
real1 = float(input("Digite a parte real do primeiro número complexo: "))
imaginaria1 = float(input("Digite a parte imaginária do primeiro número complexo: "))

# Solicita as partes real e imaginária do segundo número complexo ao usuário
real2 = float(input("Digite a parte real do segundo número complexo: "))
imaginaria2 = float(input("Digite a parte imaginária do segundo número complexo: "))

# Cria as representações dos números complexos como tuplas (parte real, parte imaginária)
num1 = (real1, imaginaria1)
num2 = (real2, imaginaria2)

# Realiza a soma dos números complexos
soma = somar_numeros_complexos(num1, num2)

# Exibe o resultado
print("A soma dos números complexos é:", soma)



'''
 Exercicio 12 - Crie um codigo completo e detalhado que retorne as duas raizes de 
 uma equação de segundo grau usando a fórmula de báscara
'''

import math

# Definição de função

def calcular_raizes(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2

    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz, raiz

    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2

# Solicita os coeficientes da equação de segundo grau ao usuário
coeficiente_a = float(input("Digite o coeficiente a: "))
coeficiente_b = float(input("Digite o coeficiente b: "))
coeficiente_c = float(input("Digite o coeficiente c: "))

# Calcula as raí­zes
raiz1, raiz2 = calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c)

# Exibe as raí­zes
print("As raí­zes da equação são:")
print("Raiz 1:", raiz1)
print("Raiz 2:", raiz2)



#  Exercicio 13 - Crie um codigo para calcular o módulo de um vetor... em N dimensões

import math

#definição de função

def calcular_modulo_vetor(vetor):
    soma_quadrados = 0
    for componente in vetor:
        soma_quadrados += componente**2
    modulo = math.sqrt(soma_quadrados)
    return modulo

# Solicita as componentes do vetor ao usuÃ¡rio
dimensoes = int(input("Digite o número de dimensões do vetor: "))
vetor = []
for i in range(dimensoes):
    componente = float(input(f"Digite a componente {i+1} do vetor: "))
    vetor.append(componente)

# Calcula o mÃ³dulo do vetor
modulo = calcular_modulo_vetor(vetor)

# Exibe o resultado
print("O módulo do vetor é:", modulo)

'''
Crie um codigo utilizando função para criar a sequÊncia de Fibonacci para os 
primeiro n elementos. 
Apresente-os e a seguir informe quais desses são números primos

'''

# importa modulo sys
import sys

# Definição de função

 # Inicializa a sequência de Fibonacci com os dois primeiros números
def fibonacci(n):
    Sequencia_Fibonacci = [1, 1] 

    while len(Sequencia_Fibonacci) < n:
        proximo_numero = Sequencia_Fibonacci[-1] + Sequencia_Fibonacci[-2]  # Calcula o próximo número da sequência
        Sequencia_Fibonacci.append(proximo_numero)  # Adiciona o próximo número Ã  lista da sequência

    return Sequencia_Fibonacci


def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

n = int(input("Digite o valor de 'n': "))
fibonacci_seq = fibonacci(n)

# Mostra a sequência de Fibonacci
print("Sequência de Fibonacci:")
print(fibonacci_seq)

# Mostra quais números são primos
primos = [numero for numero in fibonacci_seq if eh_primo(numero)]
print("Números primos na sequência de Fibonacci:")
print(primos)