from flask import Flask, render_template, request

from backend.Alunos import Aluno
from backend.Alunos import CalcMedia
from backend.Professores import Professor
from backend.QueryAluno import QA
from backend.QueryProfessor import QP
from backend.DeleteAlunosEProfessores import DeleteAluno
from backend.DeleteAlunosEProfessores import DeleteProfessor

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        idade = int(request.form["idade"])

        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        n3 = float(request.form["n3"])

        mediaA = CalcMedia(n1, n2, n3)

        nAluno = Aluno(nome, idade, mediaA)

        nAluno.salvar_no_banco()

    

    return render_template("cadastro.html")



@app.route("/cadastroP", methods=["GET", "POST"])
def cadastroP():

    if request.method == "POST":

        nome = request.form["nome"]
        idade = int(request.form["idade"])
        materia = request.form["materia"]

        p = Professor(nome, idade, materia)

        p.salvar_no_banco()


    return render_template("cadastroP.html")


@app.route("/consultaA", methods=["GET", "POST"])
def consultaA():

    resultado = None

    if request.method == "POST":

        idAluno = int(request.form["id"])

        QueryAluno = QA(idAluno)

        resultado = QA.procurarAluno(QueryAluno)

    return render_template(
        "consultaA.html",
        resultado=resultado
    )

@app.route("/consultaP", methods=["GET", "POST"])
def consultaP():

    resultado = None

    if request.method == "POST":

        idProfessor = int(request.form["id"])

        QueryProfessor = QP(idProfessor)

        resultado = QP.procurarProfessor(QueryProfessor)


    return render_template(
        "consultaP.html",
        resultado=resultado
    )

@app.route("/ExcluirA", methods=["GET", "POST"])
def excluirA():

    resultado = None

    if request.method == "POST":

        idAluno = int(request.form["id"])

        delete = DeleteAluno(idAluno)

        delete.DeletarUser()

        if delete:
            resultado = f"Aluno {idAluno} deletado com sucesso!"
        else:
            resultado = "Aluno nao encontrado / nao foi deletado"


    return render_template(
        "ExcluirA.html",
        resultado=resultado
    )


@app.route("/DeleteP", methods=["GET", "POST"])
def DeleteP():

    resultado = None

    if request.method == "POST":

        idProfessor = int(request.form["id"])

        delete = DeleteProfessor(idProfessor)

        delete.DeletarUser()

        if delete:
            resultado = f"Professor {idProfessor} deletado com sucesso!"
        else:
            resultado = "Professor nao encontrado / nao foi deletado"


    return render_template(
        "DeleteP.html",
        resultado=resultado
    )
        


if __name__ == "__main__":
    app.run(debug=True)