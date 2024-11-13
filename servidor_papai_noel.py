# servidor_papai_noel.py
import socket

HOST = '0.0.0.0'  # Escuta em todas as interfaces para permitir conexões externas
PORT = 12345      # Porta de escuta do servidor

def iniciar_servidor():
    # Criação do socket TCP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((HOST, PORT))
    servidor_socket.listen()

    print(f"Papai Noel está escutando em {HOST}:{PORT}...")

    while True:
        # Aceita uma nova conexão
        conexao, endereco = servidor_socket.accept()
        print(f"Criança conectada com IP {endereco}")

        # Recebe a mensagem do cliente (criança)
        mensagem = conexao.recv(1024).decode('utf-8')
        print(f"Criança: {mensagem}")

        # Resposta de Papai Noel (servidor)
        resposta = "Ho ho ho! Feliz Natal, pequena criança!"
        conexao.sendall(resposta.encode('utf-8'))

        # Fecha a conexão
        conexao.close()
        print(f"Conexão com a criança {endereco} encerrada.\n")

if __name__ == "__main__":
    iniciar_servidor()