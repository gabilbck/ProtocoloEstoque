import socket

# Endereço IP e porta do Codespace (substitua pelo endereço do Codespace)
HOST = 'obscure-sniffle-7xwvwpv47qxfrxwq.github.dev'  # Endereço do Codespace
PORT = 12345  # Mesma porta usada no servidor

def iniciar_cliente():
    # Criando o socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((HOST, PORT))
    print("Conectado ao Papai Noel!")

    while True:
        mensagem = input("Criança: ")
        cliente_socket.sendall(mensagem.encode('utf-8'))
        
        resposta = cliente_socket.recv(1024).decode('utf-8')
        if not resposta:
            print("Papai Noel desconectou.")
            break
        
        print(f"Papai Noel: {resposta}")

    cliente_socket.close()

if __name__ == "__main__":
    iniciar_cliente()