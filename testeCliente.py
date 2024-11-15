import socket

def cliente():
    host = '192.168.10.2'  # IP do Papai Noel (Servidor)
    porta = 5000           # Porta de comunicação

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, porta))

    print("Conectado ao Papai Noel!\n")

    while True:
        mensagem = cliente_socket.recv(1024).decode()
        print(mensagem)

        if "Vá embora" in mensagem or "Feliz Natal" in mensagem:
            print("Conversa encerrada pelo Papai Noel.")
            break

        resposta = input("Sua resposta: ")
        cliente_socket.send(resposta.encode())

    cliente_socket.close()

if __name__ == "__main__":
    cliente()
