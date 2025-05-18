import json

senhacerta = 'unip'

dados = []

# Função que solicita o nome do aluno e valida se é apenas letras
def solicitar_aluno():
    while True:
        aluno = input('Digite o nome do Aluno(Sem dar espaço): ')
        if aluno.isalpha():
            print(f"Pronto {aluno}, agora falta somente a senha!")
            return aluno
        else:
            print("Digite um nome válido por favor! Não pode conter números e espaços.")

def validar_senha(senhacerta):
    while True:
        senha = input('Digite a senha para prosseguir: ')
        if senha == senhacerta:
            break  # Sai do loop se a senha estiver correta
        else:
            print('Senha incorreta. Por favor, digite a senha correta.')

def ConvJson(lista):
    print(f"\nConvertendo a lista de dados em JSON:\n")
    objJson = json.dumps(lista, indent=4)
    return objJson

def processar_materia(aluno):
    print('Siga com as listas de disciplinas:')
    print('1 - Tecnologia da Informação e Comunicação.')
    print('2 - Pensamento Lógico Computacional com Python.')
    print('3 - Infraestrutura Computacional.')
    print('4 - Matemática e Estatística.')

    mat = int(input('Digite a matéria desejada: '))

    materias = {
        1: 'Tecnologia da Informacao e Comunicacao',
        2: 'Pensamento Logico Computacional com Python',
        3: 'Infraestrutura Computacional',
        4: 'Matematica e Estatistica'
    }

    if mat == 1 or mat == 2 or mat == 3 or mat == 4:
        materia = materias[mat]
        print(f'Você escolheu {materia}.')
        np1 = float(input('Digite a nota da NP1: '))
        np2 = float(input('Digite a nota da NP2: '))
        pim = float(input('Digite a nota do PIM: '))
        media = ((np1 * 4) + (np2 * 4) + (pim * 2)) / 10

        if media >= 7:
            print(f"Você foi aprovado, com a média: {media:.2f}. Parabéns!")
            exame = None
        else:
            print('Você ficou de exame!')
            exame = float(input('Digite a nota do exame final: '))
            if exame + media / 2 >= 5:
                print('Você foi aprovado!')
            else:
                print('Você foi reprovado!')

        print(f'{aluno}, suas notas em {materia} foram:')
        print(f'NP1: {np1}')
        print(f'NP2: {np2}')
        print(f'PIM: {pim}')
        print(f'MÉDIA: {media:.2f}')
        if media < 7:
            print(f'EXAME: {exame}')

        # Salvar os dados do aluno
        DadosAluno = {
            "nome": aluno,
            "materia": materia,
            "np1": np1,
            "np2": np2,
            "pim": pim,
            "media": media,
            "exame": exame
        }

        dados.append(DadosAluno)

    else:
        print('Opção inválida!')

# Função principal do programa
def main():
    print('Seja Bem-Vindo ao cadastro de aluno no curso de ADS (Análise e Desenvolvimento de Sistemas)')
    while True:
        aluno = solicitar_aluno()
        validar_senha(senhacerta)
        processar_materia(aluno)

        continuar = input('Deseja cadastrar outro aluno? (s/n): ')
        if continuar.lower() != 's':
            break

    objJson = ConvJson(dados)
    print(objJson)

    with open("dados.json", 'w') as arquivo:
        arquivo.write(objJson)

# Executa o programa
main()
