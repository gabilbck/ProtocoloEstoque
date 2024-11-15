import socket

def servidor():
    host = '0.0.0.0'  # Aceita conexões de qualquer IP
    porta = 5000       # Porta de comunicação

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(1)

    print("Papai Noel esperando por uma criança para conversar...\n")

    conexao, endereco = servidor_socket.accept()
    print(f"Uma criança chegou para conversar! Conectado com {endereco}\n")

    perguntas = [
        "Você foi uma boa criança este ano? (sim/não)",
        "Você ajudou nas tarefas de casa? (sim/não)",
        "Você foi gentil com seus amigos? (sim/não)"
    ]

    for pergunta in perguntas:
        conexao.send(pergunta.encode())
        resposta = conexao.recv(1024).decode().strip().lower()

        print(f"Criança respondeu: {resposta}")

        if resposta == "não":
            conexao.send("Papai Noel: Você foi uma má criança! Vá embora!".encode())
            print("Conversa encerrada: Criança foi mandada embora.")
            conexao.close()
            servidor_socket.close()
            return

    conexao.send("Papai Noel: Parabéns! Você foi uma boa criança! Feliz Natal!".encode())
    print("Conversa encerrada: Criança foi aprovada.")
    conexao.close()
    servidor_socket.close()

if __name__ == "__main__":
    servidor()
