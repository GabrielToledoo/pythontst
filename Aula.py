
'''
Exercicio 14 - Crie um código utilizando função para criar
'''
# importa modulo sys
import sys
    
    # definição de função
    
    # inicializa a sequência de Fibonacci com os dois primeiros números
def fibonacci(n):
        Sequencia_Fibonacci = [1, 1]
        
        while len(Sequencia_Fibonacci) < n:
            proximo_numero = Sequencia_Fibonacci[-1] + Sequencia_Fibonacci[-2]
            Sequencia_Fibonacci.append(proximo_numero) #Adiciona um número na lista
            
        return Sequencia_Fibonacci

def eh_primo(numero):
        if numero <=1:
            return False
        elif numero ==2:
            return True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
            
        return True
    
n = int(input("Digite o valor de 'n': "))
Sequencia_Fibonacci = fibonacci(n)

print("Sequência de Fibonacci: ")  
print(Sequencia_Fibonacci)

primos = [numero for numero in Sequencia_Fibonacci if eh_primo(numero)]    
print("números primos na sequência de fibonacci: ")
print(primos)      

# Ex 15 - Entendendo parametros, argumentos, *args e *kwargs

# Ex 16 - Calculadora avançacada: Crie uma função chamada calculadora que aceite argumentos              
    
 
    
    
    