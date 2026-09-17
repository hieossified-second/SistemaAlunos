import mysql.connector
from backend.conexao import conectarP

class Professor:
    materia: str
    
    def __init__(self, nome, idade, materia:str):
        self.nome = nome
        self.idade = idade
        self.materia = materia

        

    def salvar_no_banco(self):

        connect = conectarP()

        cursor = connect.cursor()

        sql = """
        INSERT INTO professores (nome, idade, materia)
        VALUES (%s, %s, %s)
        """

        valores = (self.nome, self.idade, self.materia)

        cursor.execute(sql, valores)

        connect.commit()

        cursor.close()
        connect.close()


if __name__ == "__main__":
    print("------------------------------------------")
    print("TESTANDO A CLASSE PROFESSOR")
    print("------------------------------------------")
    
    try:
        nome_teste = input("Digite o nome do professor: ")
        idade_teste = int(input("Digite a idade: "))
        materia_teste = input("Digite a matéria: ")
        
        # Cria a instância da classe
        prof_teste = Professor(nome_teste, idade_teste, materia_teste)
        
        # Executa o método para salvar
        prof_teste.salvar_no_banco()
        
        print("\n Professor salvo com sucesso no banco 'professores'!")
        
    except ValueError:
        print("Erro: Digite um número válido para a idade.")
    except Exception as erro:
        print(f"Erro ao conectar ou salvar no banco: {erro}")
        
    print("------------------------------------------")