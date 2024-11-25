usuarios = []
eventos = []
inscricoes = []
logado = False
op = -1


def verificar_valor_arrecadado(nome_evento, criador_email):
    total_arrecadado = 0
    numero_inscritos = 0

    for inscricao in inscricoes:
        if inscricao[0] == nome_evento:
            numero_inscritos += 1
            for evento in eventos:
                if evento[0] == nome_evento and evento[5] == criador_email:
                    total_arrecadado += evento[4]

    if numero_inscritos > 0:
        valor_por_participante = total_arrecadado / numero_inscritos
    else:
        valor_por_participante = 0

    print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
    print(f"Número de inscritos: {numero_inscritos}")
    print(f"Valor total por participante: R$ {valor_por_participante:.2f}")


def listar_participantes_evento(nome_evento, criador_email, usuario_email):
    for evento in eventos:
        if evento[0] == nome_evento and evento[5] == criador_email:
            if usuario_email != criador_email:
                print("Permissão negada: Apenas o criador do evento pode ver a lista de participantes.")
                return

            print(f"Lista de participantes do evento '{nome_evento}':")
            participantes_encontrados = False
            for inscricao in inscricoes:
                if inscricao[0] == nome_evento:
                    print(f"email: {inscricao[1]}, Status de Pagamento: {inscricao[2]}")
                    participantes_encontrados = True
            if not participantes_encontrados:
                print("Nenhum participante inscrito neste evento.")
            return

    print("Evento não encontrado ou você não tem permissão para visualizá-lo.")


def inscricao(nome_do_evento, usuario_nome, pagamento):
    encontrado = False
    for evento in eventos:
        if evento[0] == nome_do_evento and pagamento.lower() == 'pago':
            encontrado = True
            print('Inscrição realizada com sucesso.')
            inscricoes.append((nome_do_evento, usuario_nome, pagamento))
            break
    if not encontrado:
        print('O evento que você deseja se inscrever não foi encontrado ou pagamento não foi realizado.')


def buscar_eventos(busca):
    resultado = []
    for evento in eventos:
        if busca in evento[0] or busca in evento[1] or busca in evento[2] or busca in evento[3]:
            resultado.append(evento)
    return resultado


def listar_eventos(email=None):
    if email is None:
        resultado = eventos
    else:
        resultado = [evento for evento in eventos if evento[5] == email]

    if resultado:
        print("Eventos encontrados:")
        for evento in resultado:
            print(f"Nome do evento: {evento[0]}")
            print(f"Descrição: {evento[1]}")
            print(f"Data: {evento[2]}")
            print(f"Local: {evento[3]}")
            print(f"Valor da inscrição: {evento[4]:.2f}\n")
        return False
    else:
        print("Nenhum evento encontrado.")
        return True


def remover_evento(email):
    if listar_eventos(email):
        return
    nome_evento = input("Digite o nome do evento que deseja remover: ")

    evento_encontrado = None
    for evento in eventos:
        if evento[0] == nome_evento and evento[5] == email:
            evento_encontrado = evento
            break

    if evento_encontrado:
        confirmacao = input("Tem certeza que deseja remover este evento? (s/n): ")
        if confirmacao.lower() == 's':
            eventos.remove(evento_encontrado)
            print("Evento removido com sucesso.")
        else:
            print("Remoção de evento cancelada.")
    else:
        print("Evento não encontrado ou você não tem permissão para removê-lo.")


def menu_eventos():
    print('[3] Cadastrar eventos')
    print('[4] Buscar eventos')
    print('[5] Listar todos os eventos')
    print('[6] Listar meus eventos')
    print('[7] Remover um evento')
    print('[8] Participar de um evento')
    print('[9] Listar participantes')
    print('[10] Valor arrecadado')
    print('[0] Sair do menu de eventos')


def login(email, senha):
    for user in usuarios:
        if user[1] == email and user[2] == senha:
            return True
        print('Login ou senha errados, tente novamente.')
    return False


def verificar_usuario(email):
    for user in usuarios:
        if user[1] == email:
            return True
    return False


def verificar_senha(senha, senha2):
    return senha == senha2


def cadastrar_evento(email):
    nome_evento = input('Digite o nome do evento: ')
    descricao = input('Descrição do evento: ')
    data = input('Informe a data do evento (DDMMAAAA): ')
    local = input('Informe o local do evento: ')
    valor = float(input('Informe o valor da inscrição: '))

    eventos.append((nome_evento, descricao, data, local, valor, email))
    print("Evento cadastrado com sucesso!")
