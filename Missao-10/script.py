"""
  Missão 10: Contando Letras 🔄
  
  O sistema precisa contar quantas letras há em um nome.
  
  ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
  ➡️ Exemplo: contar_letras("Ana")
  ➡️ Saída:" O nome Ana tem 3 letras"
"""
print("\033[35mVamos contar quantas letras tem seu nome?\033[m")

def contar_letras(nome):
  return len(nome.replace(" ", ""))

nome = str(input("Digite seu nome completo: "))

nome_formatado = nome.title()

print(f"O nome {nome_formatado} tem {contar_letras(nome)} letras!")