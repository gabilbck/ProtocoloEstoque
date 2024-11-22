import socket

def cliente():
    host = '192.168.10.2'  # IP do Papai Noel (Servidor)
    porta = 5000           # Porta de comunicação

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (IPv4, TCP)
    cliente_socket.connect((host, porta))                              # conecta-se a porta e endereço correspondente

    print("Conectado ao Papai Noel!\n")

    while True:
        mensagem = cliente_socket.recv(1024).decode()                  # recebe pergunta ou resposta do papai noel decodificada para String
        print(mensagem)

        if "Vá embora" in mensagem or "presente" in mensagem:          # se o papai noel disser uma das palavras, é encerrada a conexão
            print("Conversa encerrada pelo Papai Noel.")
            break

        resposta = input("Sua resposta: ")                             # se não, continua para a criança responder
        cliente_socket.send(resposta.encode())                         # encaminha a mensagem em formato de bytes

    cliente_socket.close()                                             # quando retornar false

if __name__ == "__main__":
    cliente()
