import mysql.connector
from backend.conexao import conectarA
from backend.conexao import conectarP

class DeleteProfessor:
    def __init__(self, id) -> None:
        self.id = id

    def DeletarUser(self):
        conexao = conectarP()

        cursor = conexao.cursor()

        sql = "DELETE FROM professores WHERE id = %s"
        valores = (self.id,)

        cursor.execute(sql, valores)
        conexao.commit()

        # Armazena a quantidade de linhas afetadas
        linhas_afetadas = cursor.rowcount

        cursor.close()
        conexao.close()

        # GARANTIA: Retorna explicitamente o número (ou 0 se for -1/None)
        return linhas_afetadas if linhas_afetadas is not None else 0


class DeleteAluno:
    def __init__(self, id) -> None:
        self.id = id

    def DeletarUser(self):
        conexao = conectarA

        cursor = conexao.cursor()

        sql = "DELETE FROM alunos WHERE id = %s"
        valores = (self.id,)

        cursor.execute(sql, valores)
        conexao.commit()

        linhas_afetadas = cursor.rowcount

        cursor.close()
        conexao.close()

        return linhas_afetadas if linhas_afetadas is not None else 0


# --- BLOCO DE TESTE ---
if __name__ == "__main__":
    print("------------------------------------------")
    print("TESTE DE EXCLUSÃO (DELETAR)")
    print("------------------------------------------")
    print("O que você deseja deletar?")
    print("1 - Deletar Professor")
    print("2 - Deletar Aluno")
    
    try:
        opcao = int(input("Escolha a opção (1 ou 2): "))
        
        if opcao == 1:
            id_prof = int(input("Digite o ID do professor que deseja apagar: "))
            deletar_p = DeleteProfessor(id_prof)
            afetados = deletar_p.DeletarUser()
            
            if afetados > 0:
                print(f"Sucesso! Professor com ID {id_prof} foi deletado.")
            else:
                print(f"Nenhum professor encontrado com o ID {id_prof}.")
                
        elif opcao == 2:
            id_aluno = int(input("Digite o ID do aluno que deseja apagar: "))
            deletar_a = DeleteAluno(id_aluno)
            afetados = deletar_a.DeletarUser()
            
            if afetados > 0:
                print(f"Sucesso! Aluno com ID {id_aluno} foi deletado.")
            else:
                print(f"Nenhum aluno encontrado com o ID {id_aluno}.")
        else:
            print("Opção inválida.")
            
    except ValueError:
        print("Erro: Digite apenas números inteiros válidos.")
    
    print("------------------------------------------")