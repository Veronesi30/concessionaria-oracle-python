# Alvaro Freitas Miranda: RM565364
# João Victor Veronesi: RM565290
 
import os
import oracledb
import pandas as pd
import time
os.system("cls")
 
 
# tabela sql
 
"""CREATE TABLE carros (
    id_carro INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    ano DECIMAL(4) NOT NULL,            
    cor VARCHAR(30),            
    proprietario VARCHAR(100)  
);"""
 
 
try:
    conn = oracledb.connect(user = "rm565290", password = "300307", dsn='oracle.fiap.com.br:1521/ORCL')
 
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
 
except Exception as e:
    print(f"ERRO!! {e}")
 
    conexao = False
else:
 
    conexao = True
 
 
while conexao:
    os.system("cls")
    print("""Bem vindo a Company Cars! O que você desja ?
 
0 - SAIR                  
1 - Cadastrar Carros
2 - Pesquisar Carros
3 - Listar todos os Carros cadastrados
4 - Editar registro do carro
5 - Apagar registro do carro
""")
   
    opcao = input("Escolha: ")
 
    match opcao:
 
        case "1":
            try:
                os.system("cls")
                print("----- CADASTRAR CARROS -----\n")
                modelo = input("Digite o modelo....: ")
                marca = input("Digite o marca....: ")
                ano = int(input("Digite o ano...: "))
                cor = input("Digite a cor...: ")
                propietario = input("Digite o propietário...: ")
 
                cadastro = f""" INSERT INTO carros (modelo, marca, ano, cor, proprietario) VALUES ('{modelo}', '{marca}', {ano}, '{cor}','{propietario}') """
 
                inst_cadastro.execute(cadastro)
                conn.commit()
 
            except ValueError:
                print("Digite um número na idade!")
 
            except:
                print("Erro na transação do BD")
 
            else:
                print("\nDADOS GRAVADOS COM SUCESSO!")
 
 
        case "2":
            os.system("cls")
            print("----- PESQUISAR CARRO -----\n")
 
            id_carro = input("\nEscolha um Id: ")
 
            os.system("cls")
            print("DADOS ESCOLHIDOS POR ID\n")
 
            lista_carros2 = []
 
            if id_carro.isdigit():
                id_carro = int(id_carro)
                consulta = f""" SELECT * FROM carros WHERE id_carro = {id_carro}"""
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
 
                for dt in data:
                    lista_carros2.append(dt)
 
                print("-" * 45)
                dados_df = pd.DataFrame.from_records(
                lista_carros2, columns=['Id', 'Modelo', 'Marca', 'Ano', 'Cor', 'Proprietário'], index='Id')
 
                if len(lista_carros2) == 0:
                    print(f"Não há um pet cadastrado com o ID = {id_carro}")
                else:
                    consulta = f"SELECT * FROM carros WHERE id_carro ={id_carro}"
                    inst_consulta.execute(consulta)
                    conn.commit()
                    print(dados_df)
                    print("-" * 45)
            else:
                print("O Id não é numérico!")
 
        case "3":
            os.system("cls")
            print("----- LISTAR CARROS -----\n")
            lista_carros = []
 
            inst_consulta.execute('SELECT * FROM carros')
            data = inst_consulta.fetchall()
           
            for dt in data:
                lista_carros.append(dt)
            lista_carros = sorted(lista_carros)
 
            print("-" * 45)
            dados_df = pd.DataFrame.from_records(
                lista_carros, columns=['Id', 'Modelo', 'Marca', 'Ano', 'Cor', 'Proprietário'], index='Id')
 
            if dados_df.empty:
                print(f"Não há Carros cadastrados!")
            else:
                print(dados_df)
                print("-" * 45)

        case "4":
            try:
                print("----- ALTERAR DADOS DO CARRO -----")
                print("DADOS JA GRAVADOS NA TABELA")
                lista_carros1 = []  
    
                # Mostrando arquivos ja salvos no BD
                inst_consulta.execute('SELECT * FROM CARROS')
                data = inst_consulta.fetchall()
            
                for dt in data:
                    lista_carros1.append(dt)
                lista_carros1 = sorted(lista_carros1)
    
    
                print("-" * 45)
                dados_df = pd.DataFrame.from_records(
                    lista_carros1, columns=['Id', 'Modelo', 'Marca', 'Ano', 'Cor', 'Proprietário'], index='Id')
                print(dados_df)
                print("-" * 45)
                lista_dados = [] 
 
                id_carro = int(input("Escolha um Id: "))
 
                # Constroi a instrução de consulta para verificar a existencia ou não do id
                consulta = f""" SELECT * FROM CARROS WHERE id_carro = {id_carro}"""
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
 
                # Preenche a lista com o registro encontrado (ou não)
                for dt in data:
                    lista_dados.append(dt)
 
                # analisa se foi encontrado algo
                if len(lista_dados) == 0:  # se não há o id
                    print(f"Não há um carro cadastrado com o ID = {id_carro}")
                    input("Pressione ENTER")
                else:
                    # Captura os novos dados
                    novo_modelo = input("Digite um novo modelo: ")
                    nova_marca = input("Digite uma nova marca: ")
                    novo_ano = input("Digite um novo ano: ")
                    nova_cor = input("Digite uma nova cor: ")
                    novo_proprietario = input("Digite um novo proprietário: ")

                
                    # Constroi a instrução de edição do registro com os novos dados
                    alteracao = f"""
                    UPDATE CARROS SET MODELO ='{novo_modelo}', marca ='{nova_marca}', ano ='{novo_ano}', cor = '{nova_cor}', proprietário = '{novo_proprietario}' WHERE id_carro = {id_carro}
                    """
                    inst_alteracao.execute(alteracao)
                    conn.commit() 
            except ValueError:
                print("Digite um número no ano!")
            except:
                print("Erro na transação do BD")
            else:
                print("##### Dados ATUALIZADOS! #####")


        case "5":
            os.system("cls")
            print("----- EXCLUIR CARRO DA TABELA POR (ID) -----\n\n")
 
            print("DADOS JA GRAVADOS NA TABELA")
            lista_carros1 = []  
 
            # Mostrando arquivos ja salvos no BD
            inst_consulta.execute('SELECT * FROM carros')
            data = inst_consulta.fetchall()
           
            for dt in data:
                lista_carros1.append(dt)
            lista_carros1 = sorted(lista_carros1)
 
 
            print("-" * 45)
            dados_df = pd.DataFrame.from_records(
                lista_carros1, columns=['Id', 'Modelo', 'Marca', 'Ano', 'Cor', 'Proprietário'], index='Id')
            print(dados_df)
            print("-" * 45)
 
            id_carro = input("Escolha um Id: ")
           
            # excluindo dados da tabela
            os.system("cls")
            print("DADOS EXCLUIDOS POR (ID)\n")
 
            lista_carros = []
 
           
            if id_carro.isdigit():
                id_carro = int(id_carro)
                consulta = f""" SELECT * FROM carros WHERE id_carro = {id_carro}"""
                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall()
 
                for dt in data:
                    lista_carros.append(dt)
 
                if len(lista_carros) == 0:
                    print(f"Não há um pet cadastrado com o ID = {id_carro}")
                else:
                    exclusao = f"DELETE FROM carros WHERE id_carro = {id_carro}"
                    inst_exclusao.execute(exclusao)
                    conn.commit()
 
                    # Mostra os dados excluidos com pandas
                    print("-" * 45)
                    dados_df = pd.DataFrame.from_records(
                    lista_carros, columns=['Id', 'Modelo', 'Marca', 'Ano', 'Cor', 'Proprietário'], index='Id')
                    print(dados_df)
                    print("-" * 45)
            else:
                print("O Id não é numérico!")
 
        case "0":
            os.system("cls")
            print("Programa sendo finalizado! Espere um instante...")
            time.sleep(3)
            os.system("cls")
            print("Programa finalizado!")
            break

        case _:
            print("Nenhuma alternativa encontrada! Tente novamente...")
 
    input("\n\nPressione enter para continuar...")
