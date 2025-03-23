"""
  Missão 3: Recuperando o Sistema de Notas 📊
  
  - As classificações das provas desapareceram! Agora os alunos não sabem 
  se tiraram um A, B, C, D ou F . 
  Antes que o pânico se espalhe, sua tarefa é criar um programa que peça 
  a nota do aluno e imprima sua classificação conforme a escala:

- A (90-100) - "Parabéns, você tirou A!"
- B (80-89) - "Muito bem, você tirou B."
- C (70-79) - "Bom trabalho, você tirou C."
- D (60-69) - "Fique atento, você tirou D."
- F (menos de 60) – "Estude um pouco mais, você tirou F."
"""

print("\033[1;35mSeja bem-vindo ao sistema de notas!\033[m")
nota_do_aluno = float(input("Digite a sua nota (0-100): "))

if nota_do_aluno >= 90 and nota_do_aluno <= 100:
    print("Parabéns, você tirou A! 🎉")
elif nota_do_aluno >= 80 and nota_do_aluno < 90:
    print("Muito bem, você tirou B. 👍")
elif nota_do_aluno >= 70 and nota_do_aluno < 80:
    print("Bom trabalho, você tirou C. 😊")
elif nota_do_aluno >= 60 and nota_do_aluno < 70:
    print("Fique atento, você tirou D. ⚠️")
elif nota_do_aluno < 60 and nota_do_aluno >= 0:
    print("Estude um pouco mais, você tirou F. 😔")
else:
    print("Nota inválida! 🚫")
