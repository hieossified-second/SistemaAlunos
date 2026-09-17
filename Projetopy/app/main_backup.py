from flask import Flask
from backend.Alunos import Aluno
from backend.Alunos import CalcMedia
from backend.Professores import Professor
from backend.QueryAluno import QA
from backend.QueryProfessor import QP
from backend.DeleteAlunosEProfessores import DeleteAluno
from backend.DeleteAlunosEProfessores import DeleteProfessor

app = Flask(__name__)
@app.route("/")
def inicio():
    return "Meu site esta working!"

if __name__ == "__main__":
    app.run(debug=True)





while True:
    print("----------------------------------------------------------------------")
    print("|Bem-Vindo ao sistema da E.E Solo Desenvolvimento Epsilon")
    print("|O que deseja para o dia de hoje ")
    print("|1 - Adicionar Aluno e sua media ")
    print("|2 - Adicionar novo professor")
    print("|3 - fazer uma consulta de Professor")
    print("|4 - fazer consulta de um Aluno")
    print("|5 - Deletar o Registro de um Professor")
    print("|6 - Deletar o Registro de um Aluno")
    print("|0 - SAIR")
    ope = int(input("Digite sua opcao: "))
    print("----------------------------------------------------------------------")


    if ope == 1:


        nome = input("Digite o nome do Aluno: ")
        idade = int(input("Digite a idade do mesmo: "))
        ope = int(input("Se deseja sair do programa digite 1, se nao 0: "))


        print("----------------------------------------------------------------------")
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))


        mediaA = CalcMedia(n1, n2, n3)

        nAluno = Aluno(nome, idade, mediaA)

        print(
            "---------------------------------------"
            f"A Média final do aluno {nAluno.nome} é: "
            f"{nAluno.nota:.2f}"
            "----------------------------------------"
        )

        nAluno.salvar_no_banco()
        print("Aluno salvo no banco de dados")
        print("------------------------------------------")

        continue


    if ope == 2:

        print("------------------------------------------")
        nome_prof = input("Digite o nome do Professor: ")
        idade_prof = int(input("Digite a idade do professor: "))
        materia_prof = input("Digite a Matéria: ")


        p = Professor(nome_prof, idade_prof, materia_prof)
        p.salvar_no_banco()

        print("Professor salvo no banco de dados")
        print("------------------------------------------")

        continue


    if ope == 3:
        idprofessor = int(input("Insira o ID do professor: "))

        QueryPRof = QP(idprofessor)
        buscaProfessor = QP.procurarProfessor(QueryPRof)


        if(buscaProfessor):
            print("------------------------------------------")
            print(buscaProfessor)
            print("------------------------------------------")
        else:
            print("------------------------------------------")
            print("Professor nao encontrado :(")
            print("------------------------------------------")

        continue

    if ope == 4:
        idAluno = int(input("Insira o ID do aluno: "))
        QueryAluno = QA(idAluno)
        buscaAluno = QA.procurarAluno(QueryAluno)

        if(buscaAluno):
            print("------------------------------------------")
            print(buscaAluno)
            print("------------------------------------------")
        else:
            print("------------------------------------------")
            print("Aluno nao encontrado :(")
            print("------------------------------------------")

        continue

    if ope == 5:
        print("------------------------------------------")
        idprofessor= int(input("Insira o ID do Professor: "))
        print("------------------------------------------")
        deletar = DeleteProfessor(idprofessor)
        afetados = deletar.DeletarUser()
        if(afetados > 0):
            print(f"Professor {idprofessor} Deletado!")
            print("------------------------------------------")
            continue
        else:
            print("Nenhum Professor foi apagado")
    if ope == 6:
        print("------------------------------------------")
        idAluno= int(input("Insira o ID do Aluno: "))
        print("------------------------------------------")
        deletar = DeleteAluno(idAluno)
        afetados = deletar.DeletarUser()
        if(afetados > 0):
            print(f"Aluno {idAluno} Deletado!")
            print("------------------------------------------")
            continue
        else:
            print("Nenhum Aluno foi apagado")
    if ope == 0:
        break





