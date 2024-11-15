import socket

def servidor():
    host = '192.168.10.1'  # IP da máquina 1
    porta = 5000           # Porta para escutar conexões
    
    # Criar o socket
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(1)
    
    print(f"Servidor esperando conexão em {host}:{porta}...")
    
    conexao, endereco = servidor_socket.accept()
    print(f"Conexão estabelecida com {endereco}")
    
    while True:
        mensagem = conexao.recv(1024).decode()
        if not mensagem:
            break
        print(f"Mensagem recebida: {mensagem}")
        resposta = input("Digite uma resposta: ")
        conexao.send(resposta.encode())
    
    conexao.close()
    servidor_socket.close()

if __name__ == "__main__":
    servidor()
