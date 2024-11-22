import socket  # Permitir conexões

def servidor():
    host = '0.0.0.0'  # Aceita conexões de qualquer IP
    porta = 5000      # Porta de comunicação

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
    servidor_socket.bind((host, porta))                                  # Conecta-se à porta e endereço
    servidor_socket.listen(1)                                            # Escuta um IP por vez

    print("Papai Noel esperando por uma criança para conversar...\n")

    conexao, endereco = servidor_socket.accept()                             # Quando aceita conexão, `conexao` e `endereco` recebem as informações para estabelecer a comunicação
    print(f"Uma criança chegou para conversar! Conectado com {endereco}\n")  # Exibe o IP da criança

    perguntas = [
        "Você foi uma boa criança este ano? (sim/não)",
        "Você ajudou nas tarefas de casa? (sim/não)",
        "Você foi gentil com seus amigos? (sim/não)",
        "Você fez sua lição de casa sem reclamar? (sim/não)",
        "Você pediu desculpas quando errou? (sim/não)",
        "Você compartilhou seus brinquedos com outros? (sim/não)",
        "Você cuidou bem dos seus pets ou plantas? (sim/não)",
        "Você agradeceu às pessoas que te ajudaram? (sim/não)",
        "Você não brigou com seus irmãos ou amigos? (sim/não)",
        "Você escovou os dentes todos os dias? (sim/não)"
    ]

    todas_respostas_sim = True

    for pergunta in perguntas:
        while True:
            # Envia a pergunta para a criança
            conexao.send(pergunta.encode())
            resposta = conexao.recv(1024).decode().strip().lower()  # Decodifica, retira espaços

            print(f"Criança respondeu: {resposta}")

            # Verifica se a resposta é válida (sim ou não)
            if resposta in {"sim", "não"}:
                break
            else:
                # Resposta inválida, pede para a criança digitar novamente
                conexao.send("Papai Noel: Eu não entendi sua resposta. Por favor, responda com 'sim' ou 'não'.\n".encode())

        # Processa a resposta válida
        if resposta == "não":
            todas_respostas_sim = False
            conexao.send("Papai Noel: Você foi uma má criança! Vá embora!".encode())
            print("Conversa encerrada: Criança foi mandada embora.")
            break  # Encerra o loop de perguntas e sai do servidor

    # Se todas as respostas foram "sim", entrega o presente
    if todas_respostas_sim:
        presente = """
{~._.~}
 ( Y )
()~*~()
(_)-(_)
"""
        conexao.send(f"Papai Noel: Parabéns! Você foi uma boa criança! Aqui está seu presente:\n{presente}".encode())
        print("Conversa encerrada: Criança fez bem e recebeu o presente.")

    # Fecha a conexão com a criança (ao final da conversa ou quando ela é mandada embora)
    conexao.close()
    servidor_socket.close()
    print("Conexão encerrada.")

if __name__ == "__main__":
    servidor()
