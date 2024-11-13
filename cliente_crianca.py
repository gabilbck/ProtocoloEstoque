# cliente_crianca.py
import socket

HOST = 'curly-space-eureka-7xwvwpv4xx6hwqw4.github.dev'  # Substitua pelo endereço público do primeiro Codespace
PORT = 12345  # Porta que o servidor está escutando

def iniciar_cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conecta ao servidor (primeiro Codespace)
        cliente_socket.connect((HOST, PORT))
        print(f"Conectado ao Papai Noel em {HOST}:{PORT}")

        # Mensagem que a criança quer enviar
        mensagem = "Oi Papai Noel, eu fui um bom menino esse ano!"
        cliente_socket.sendall(mensagem.encode('utf-8'))

        # Recebe a resposta de Papai Noel
        resposta = cliente_socket.recv(1024).decode('utf-8')
        print(f"Papai Noel: {resposta}")

    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")

    finally:
        # Fecha a conexão
        cliente_socket.close()
        print("Conexão com Papai Noel encerrada.")

if __name__ == "__main__":
    iniciar_cliente()