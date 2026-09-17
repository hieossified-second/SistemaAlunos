import mysql.connector
from backend.conexao import conectarA

class QA:
    def __init__(self, alunoid):
        self.alunoid = alunoid

    def procurarAluno(self):
   
        connect = conectarA

        cursor = connect.cursor()

        sql = """
            SELECT * from Alunos
            WHERE id = %s
            """

        valores = (self.alunoid,)

        cursor.execute(sql, valores)

        aluno = cursor.fetchone()

        cursor.close()
        connect.close()

        return aluno

    # --- BLOCO DE TESTE NO MESMO ARQUIVO ---
if __name__ == "__main__":
    print("------------------------------------------")
    print("TESTANDO A CLASSE QA (ALUNOS)")
    print("------------------------------------------")
    
    try:
        id_teste = int(input("Digite um ID de aluno para testar: "))
        
        # Cria a instância da classe
        busca_teste = QA(id_teste)
        
        # Executa o método
        resultado = busca_teste.procurarAluno()
        
        print("\n--- RESULTADO ---")
        if resultado:
            print("Aluno encontrado com sucesso!")
            print(f"Tupla retornada: {resultado}")
        else:
            print("Nenhum aluno encontrado com o ID informado.")
            
    except ValueError:
        print("Erro: Digite apenas números inteiros para o ID.")
    print("------------------------------------------")