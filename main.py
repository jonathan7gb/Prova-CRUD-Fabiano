import mysql.connector
import time as t

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'materialEscolar'
)

cursor = conexao.cursor()
print("Conexão estabelecida com sucesso!")

tipoMaterialStr = ""

def menu():
    print("\n== Gerenciamento de Materiais Escolares == ")
    print("1 - Cadastrar material")
    print("2 - Listar materiais")
    print("3 - Editar materiais")
    print("4 - Excluir material")
    print("0 - Sair")
    
escolha = 1


while escolha != 0:  
    menu()
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
            print('\n-- Cadastrar material --')
            tituloMaterial = input("Digite o título do material: ")
            quantidadeEstoqueMaterial = int(input("---\nDigite a quantidade em estoque: "))
            if quantidadeEstoqueMaterial < 0:
                print("Quantidade inválida. Deve ser um número positivo.")
            else:
                isbnMaterial = input("---\nDigite o ISBN do material: ")
                
                cursor.execute(f'select * from materiais where isbn = "{isbnMaterial}"')
                resultado = cursor.fetchall()
                
                if resultado:
                    print("\n!! ISBN já cadastrado. Tente novamente. !!\n")
                else:
                    dataAquisicaoMaterial = input("---\nDigite a data de aquisição (AAAA-MM-DD): ")
                    
                    if dataAquisicaoMaterial == "":
                        dataAquisicaoMaterial = '2025-06-11'
                   
                    print("---\nQual o tipo do Material?")
                    print("1 - Livro\n2 - Apostila\n3 - Multimídia\n4 - Periódico\n5 - Equipamento")
                    tipoMaterial = int(input("Digite o tipo do material: "))
                        
                    if tipoMaterial < 1 or tipoMaterial > 5:
                        print("Tipo inválido. Tente novamente.")
                    elif tipoMaterial == 1:
                        tipoMaterialStr = "Livro"
                    elif tipoMaterial == 2:
                        tipoMaterialStr = "Apostila"
                    elif tipoMaterial == 3:
                        tipoMaterialStr = "Multimídia"
                    elif tipoMaterial == 4:
                        tipoMaterialStr = "Periódico"
                    elif tipoMaterial == 5:
                        tipoMaterialStr = "Equipamento"
                    
                    comando = f'INSERT INTO materiais (titulo, quantidade_estoque, isbn, data_aquisicao, tipo) VALUES ("{tituloMaterial}", {quantidadeEstoqueMaterial}, "{isbnMaterial}", "{dataAquisicaoMaterial}", "{tipoMaterialStr}")'
                    cursor.execute(comando)
                    conexao.commit()
                    print("\n-- Material cadastrado com sucesso! --")
    elif escolha == 2:
            print('\n-- Listar materiais --')
            print('1 - Listar todos os materiais')
            print('2 - Filtrar materiais por tipo')
            print('3 - Listar materiais por título')
            print('4 - Listar materiais por Código ISBN')
            escolhaBusca = int(input("Digite sua escolha: "))
            t.sleep(0.5)
            
            match escolhaBusca:
                case 1:
                    cursor.execute('SELECT * FROM materiais')
                    resultados = cursor.fetchall()
                    if resultados:
                        print("\n-- Lista de Materiais --")
                        for material in resultados:
                            print("=" * 30)
                            print(f"ID: {material[0]}\nTítulo: {material[1]}\nQuantidade: {material[2]}\nISBN: {material[3]}\nData de Aquisição: {material[4]}\nTipo: {material[5]}")
                            t.sleep(0.5)
                    else:
                        print("\n!! Nenhum material cadastrado. !!")
                case 2:
                    print("\n-- Filtrar materiais por tipo --")
                    print("1 - Livro\n2 - Apostila\n3 - Multimídia\n4 - Periódico\n5 - Equipamento")
                    tipoBusca = int(input("Digite o tipo do material: "))
                    
                    if tipoBusca < 1 or tipoBusca > 5:
                        print("Tipo inválido. Tente novamente.")
                    elif tipoBusca == 1:
                        tipoBuscaStr = "Livro"
                    elif tipoBusca == 2:
                        tipoBuscaStr = "Apostila"
                    elif tipoBusca == 3:
                        tipoBuscaStr = "Multimídia"
                    elif tipoBusca == 4:
                        tipoBuscaStr = "Periódico"
                    elif tipoBusca == 5:
                        tipoBuscaStr = "Equipamento"
                    
                    if tipoBusca > 0 and tipoBusca < 6:
                        comando = f'SELECT * FROM materiais WHERE tipo = "{tipoBuscaStr}"'
                        cursor.execute(comando)
                        resultados = cursor.fetchall()
                        if resultados:
                            print("\n-- Materiais encontrados --")
                            for material in resultados:
                                print("=" * 30)
                                print(f"ID: {material[0]}\nTítulo: {material[1]}\nQuantidade: {material[2]}\nISBN: {material[3]}\nData de Aquisição: {material[4]}\nTipo: {material[5]}")
                        else:
                            print("\n!! Nenhum material encontrado. !!")
                case 3:
                    tituloBusca = input("\nDigite o título do material: ")
                    comando = f'SELECT * FROM materiais WHERE titulo LIKE "%{tituloBusca}%"'
                    cursor.execute(comando)
                    resultados = cursor.fetchall()
                    if resultados:
                        print("\n-- Materiais encontrados --")
                        for material in resultados:
                            print("=" * 30)
                            print(f"ID: {material[0]}\nTítulo: {material[1]}\nQuantidade: {material[2]}\nISBN: {material[3]}\nData de Aquisição: {material[4]}\nTipo: {material[5]}")
                    else:
                        print("\n!! Nenhum material encontrado. !!")
                case 4:
                    isbnBusca = input("\nDigite o Código ISBN do material: ")
                    comando = f'SELECT * FROM materiais WHERE isbn = "{isbnBusca}"'
                    cursor.execute(comando)
                    resultados = cursor.fetchall()
                    if resultados:
                        print("\n-- Materiais encontrados --")
                        for material in resultados:
                            print("=" * 30)
                            print(f"ID: {material[0]}\nTítulo: {material[1]}\nQuantidade: {material[2]}\nISBN: {material[3]}\nData de Aquisição: {material[4]}\nTipo: {material[5]}")
                    else:
                        print("\n!! Nenhum material encontrado. !!")
    elif escolha == 3:
            print('\n-- Editar materiais --')
            isbnMaterial = input("Digite o ISBN do material que deseja editar: ")
            cursor.execute(f'SELECT * FROM materiais WHERE isbn = "{isbnMaterial}"')
            resultado = cursor.fetchall()
            if not resultado:
                print("\n!! Material não encontrado. !!")
            else:
                print("\n-- Material encontrado --")
                for material in resultado:
                    print("=" * 30)
                    print(f"ID: {material[0]}\nTítulo: {material[1]}\nQuantidade: {material[2]}\nISBN: {material[3]}\nData de Aquisição: {material[4]}\nTipo: {material[5]}")
                
                novaQuantidade = int(input("---\nDigite a nova quantidade em estoque: "))
                
                if novaQuantidade <= 0:
                    print("Quantidade inválida. Deve ser um número positivo.")
                else:
                    comandoUpdate = f'UPDATE materiais SET quantidade_estoque = {novaQuantidade} WHERE isbn = "{isbnMaterial}"'
                    cursor.execute(comandoUpdate)
                    conexao.commit()
                    print("\n-- Material editado com sucesso! --")
              
    elif escolha == 4:
            print('\n-- Excluir materiais por Tipo --')
            print("1 - Livro\n2 - Apostila\n3 - Multimídia\n4 - Periódico\n5 - Equipamento")
            tipoExcluir = int(input("Digite o tipo do material: "))
            
            if tipoExcluir < 1 or tipoExcluir > 5:
                print("Tipo inválido. Tente novamente.")
            elif tipoExcluir == 1:
                tipoExcluirStr = "Livro"
            elif tipoExcluir == 2:
                tipoExcluirStr = "Apostila"
            elif tipoExcluir == 3:
                tipoExcluirStr = "Multimídia"
            elif tipoExcluir == 4:
                tipoExcluirStr = "Periódico"
            elif tipoExcluir == 5:
                tipoExcluirStr = "Equipamento"
                
                if tipoExcluir > 0 and tipoExcluir < 6:
                    comandoExcluir = f'DELETE FROM materiais WHERE tipo = "{tipoExcluirStr}"'
                    cursor.execute(comandoExcluir)
                    conexao.commit()
                    print("\n-- Materiais excluídos com sucesso! --")
                else:
                    print("Tipo inválido. Tente novamente.")
            
    else:
        print("Opção inválida. Tente novamente.")