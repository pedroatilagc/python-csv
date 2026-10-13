import csv

#ESCRITA DE CSV
'''
novos_alunos = [
    ["Daniel", 17, 6.7],
    ["Francisco", 16, 5.2],
    ["Rafaela", 15, 8.8]
]

with open("alunos.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(novos_alunos)
'''

#DESAFIO
aluno = []
name = input("Digite o nome do aluno: ")
aluno.append(name)
age = input("Digite a idade do aluno: ")
aluno.append(age)
grade = input("Digite a nota do aluno: ")
aluno.append(grade)

with open("alunos.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(aluno)

with open("alunos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)


