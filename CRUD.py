import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "302302",
    database = "academiaturmac"
)

meu_cursor = banco.cursor()
menu = '''1 - Alunos
2 - Funcionários
3 - Personal
4 - Modalidades'''
operacoes = '''1 - Adicionar 
2 - Deletar
3 - Atualizar
4 - Exibir
5 - Trocar'''
dadosALUNOS = ['Nome','CPF','Telefone','Endereço']
dadosalunos = [''] * 4
dadosFUNCIONARIOS = ['Nome','CPF','Salário','E-mail']
dadosfuncionarios = [''] * 4
dadosMODALIDADES = ['Nome_modalidades','Duração']
dadosmodalidades = [''] * 2
dadosPERSONAL = ['Nome','CPF','Telefone','CEP','CREF']
dadospersonal = [''] * 5

print(menu)

while True:
    escolha_tabela = int(input("Digite o menu que você quer:"))
    if escolha_tabela == 1:
        print("Tabela ALUNOS")
        escolha_operacoes = int(input("Digite a operação que você quer:"))
        if escolha_operacoes == 1:
            print("Adicionar ALUNOS")
            adicao = 'insert into alunos(nome, cpf, telefone, endereco);'
            for c in range(4):
                dadosalunos[c] = input(f"Insira {dadosALUNOS[c]}")
            sql = "insert into alunos(nome,cpf,telefone,endereco) values (%s,%s,%s,%s)"
            data = (dadosalunos[0],dadosalunos[1],dadosalunos[2],dadosalunos[3])
            meu_cursor.execute(sql, data)
            banco.commit()
            userid = meu_cursor.lastrowid

        elif escolha_operacoes == 2:
            pesquisa = "select * from alunos;"
            meu_cursor.execute(pesquisa)
            resultado = meu_cursor.fetchall()
            for x in resultado:
                print(x)
            delet = int(input("Digite o ID do funcionário:"))
            deletar = (f'''delete from funcionarios
            where id_funcionario = {delet}''')
            meu_cursor.execute(deletar)
            banco.commit()
            meu_id = meu_cursor.lastrowid
        elif escolha_operacoes == 4:
            pesquisa = 'select * from alunos'
            meu_cursor.execute(pesquisa)
            resultado = meu_cursor.fetchall()
            for x in resultado:
                print(x)
    else:
        print("Operação inválida selecione uma operação válida")
        escolha_tabela = int(input("Digite o menu que você quer:"))