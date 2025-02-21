"""
  Missão 1: Restaurando as Regras Escolares 📝
  
  - O vírus apagou os critérios de aprovação dos alunos! Para ajudar o 
  Professor Byte a organizar o sistema, sua tarefa é criar um programa
  que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou 
  reprovado (nota menor ou igual à 5).
"""

nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if media >= 6:
    print('🎉 Parabéns! Vocë foi \033[1;32mAprovado(a)\033[m!')
else:
    print('😢 Infelizmente, você foi \033[1;31mReprovado(a)\033[m!')
