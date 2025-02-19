"""
  Missão 5: Recuperando o Cofre de Segurança 🔒
  
  O cofre da biblioteca guarda códigos raros de programação, 
  mas o vírus resetou a senha! Agora, apenas quem souber a 
  combinação correta poderá acessá-lo.

  - Crie um programa que solicite ao usuário uma senha e verifique
  se ela está correta. A senha correta é "Python123"
"""

print("Vocë tem 5 tentativas para acertar a senha do cofre da biblioteca.")
tentativas = 5

while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == "Python123":
        print("🎉 Parabéns! Você acertou a senha e acessou o cofre da biblioteca!")
        break
    else:
        tentativas -= 1
        if tentativas == 0:
            print("😢 Infelizmente, você excedeu o número de tentativas permitidas.")
        else:
            print(
                f"😢 Infelizmente, a senha está incorreta. Você ainda tem {tentativas} tentativas restantes.")
print("Obrigado por tentar acessar o cofre da biblioteca. Até a próxima!")