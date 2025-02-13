"""
  Missão 2: O Sistema Eleitoral Secreto 📝
  
  - O grêmio estudantil da escola realiza votações para decidir melhorias e inovações,
  mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar 
  um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).
"""
print("\033[1;34mBem-vindo ao Sistema Eleitoral do Grêmio Estudantil!\033[m")
idade_do_usuario = int(
    input("Por Favor, informe sua idade e veja se esta apto para votar: "))

if idade_do_usuario > 48:
  print("Você já passou da idade de votar! Mas não se preocupe, você ainda pode ajudar com ideias de melhorias. 😊")
elif idade_do_usuario >= 16:
  print("Você está apto para votar! Escolha com sabedoria. 🗳️")
else:
  print("Você ainda não pode votar! Mas não se preocupe, em breve você poderá participar das votações. ⏳")
