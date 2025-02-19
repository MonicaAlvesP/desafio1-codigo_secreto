"""
  Missão 4: Restaurando a Identificação de Números ⚖️
  
  Os robôs da escola precisam identificar padrões numéricos para 
  resolver cálculos e otimizar os sistemas. No entanto, o vírus 
  bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
  
  - Crie um programa que peça dois números e exiba a soma deles.
"""

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

soma = numero1 + numero2

print(f"A soma dos números é: \033[1;34m{soma}\033[m")