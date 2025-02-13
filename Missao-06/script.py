"""
  Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
  
  O vírus está comprometendo o sistema de segurança e a contagem 
  de registros! Para restaurar o funcionamento correto, você precisa 
  reforçar as verificações e garantir que os dados sejam processados 
  corretamente.
  
  - Exiba os números de 1 a 10 usando um loop while. 
"""

import time

contador = 1

print('Contagem iniciada:')

while contador <= 10:
  print(contador)
  time.sleep(1)
  contador += 1
  
print('Contagem finalizada.')