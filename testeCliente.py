import socket

def cliente():
    host = '192.168.10.1'  # IP do servidor (máquina 1)
    porta = 5000           # Porta do servidor
    
    # Criar o socket
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, porta))
    
    print(f"Conectado ao servidor em {host}:{porta}")
    
    while True:
        mensagem = input("Digite uma mensagem para enviar ao servidor: ")
        cliente_socket.send(mensagem.encode())
        resposta = cliente_socket.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")
    
    cliente_socket.close()

if __name__ == "__main__":
    cliente()
