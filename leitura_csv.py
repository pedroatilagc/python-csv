import csv

#LEITURA DE CSV - DICT
with open("alunos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(f'Aluno: {linha["Nome"]} | Nota: {linha["Nota"]}')

