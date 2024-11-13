import socket

# Configurando o servidor (Papai Noel)
HOST = '0.0.0.0'  # Permite que o servidor aceite conexões externas
PORT = 12345  # Porta de comunicação, escolha uma porta disponível

def iniciar_servidor():
    # Criando o socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((HOST, PORT))
    servidor_socket.listen()
    print("Papai Noel está aguardando as crianças se conectarem...")

    # Aguardando conexão da criança
    while True:
        cliente_socket, endereco = servidor_socket.accept()
        print(f"Criança conectada de: {endereco}")

        # Recebe mensagem da criança e responde
        while True:
            mensagem = cliente_socket.recv(1024).decode('utf-8')
            if not mensagem:
                print("Criança desconectou.")
                break

            print(f"Criança: {mensagem}")
            resposta = input("Papai Noel: ")
            cliente_socket.sendall(resposta.encode('utf-8'))

        cliente_socket.close()

if __name__ == "__main__":
    iniciar_servidor()