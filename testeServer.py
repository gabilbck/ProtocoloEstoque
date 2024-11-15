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
        conexao.send(pergunta.encode())
        resposta = conexao.recv(1024).decode().strip().lower()

        print(f"Criança respondeu: {resposta}")

        if resposta != "sim":
            todas_respostas_sim = False
            conexao.send("Papai Noel: Você foi uma má criança! Vá embora!".encode())
            print("Conversa encerrada: Criança foi mandada embora.")
            conexao.close()
            servidor_socket.close()
            return

    if todas_respostas_sim:
        presente = """
 _________________________________________________________
|\\=========================================================\\
||                                                         |
||        _        __        ___        __        _        |
||       ; `-.__.-'. `-.__.-'. .`-.__.-' .`-.__.-' :       |
||     _.'. . . . . . . . .,,,,,,,. . . . . . . . .`._     |
||   .'. . . . . . . . ,a@@@@@@@@@@@a, . . . . . . . .`.   |
||   `. . . . ,a@@@@@a@@@a@@@@@@@@@a@@@a@@@@@a, . . . ,'   |
||     ) . . a@@@@@@a@@@@@a@@@@@@@a@@@@@a@@@@@@a . . (     |
||   ,' . . .@@@%%%a@@@@@@@@@@@@@@@@@@@@@a%%%@@@  . . `.   |
||   `.. . . @@@%%a@@@@@@""@@@@@@@""@@@@@@a%%@@@ . . .,'   |
||     ). . . "@@a@@@@@@@@@SSSSSSS@@@@@@@@@a@@" . . .(     |
||   ,'. . . . . `@@@@@@@@SSS, ,SSS@@@@@@@@' . . . . .`.   |
||   `. . . . . . `@@@@@@@`SSS:SSS'@@@@@@@' . . . . . ,'   |
||     ) . . . . . `@@@@@@@sssssss@@@@@@@' . . . . . (     |
||   ,' . . . . . ,a@@a@@@@@@@@@@@@@@@a@@a, . . . . . `.   |
||   `.. . . . .a@@@a@@@@@a@@@a@@@a@@@@@a@@@a. . . . .,'   |
||     ). . . .a@@@@@a@@@@@@@@@@@@@@@@@a@@@@@a. . . .(     |
||   ,'. . . . @@@@@@a@@@@'   "   `@@@@a@@@@@@ . . . .`.   |
||   `. . . . .@@@@@@@aaaa,       ,aaaa@@@@@@@  . . . ,'   |
||     ) . . . `@@@@@@@@@@@@a, ,a@@@@@@@@@@@@' . . . (     |
||   ,' . . . . .`@@@@@@@@@@a@a@a@@@@@@@@@@'. . . . . `.   |
||   `;;;;;;;;;;;;aaaaaaaaaa@@@@@aaaaaaaaaa;;;;;;;;;;;;'   |
||     );;;;;;;,mMMMMMMMm@@@@@@@@@@@mMMMMMMMm,;;;;;;;(     |
||   ,;;;;;;;;a@%#%%#%%#%Mm@@@@@@@mM%#%%#%%#%@a;;;;;;;;,   |
||   `;;;;;;;;@@%%%%%%%%%%M@@";"@@M%%%%%%%%%%@@;;;;;;;;'   |
||     );;;;;;`@a%%%%%%%%mM";;;;;"Mm%%%%%%%%a@';;;;;;(     |
||   ,;;;;;;;;;;"@@@@@@@@";;;;;;;;;"@@@@@@@@";;;;;;;;;;,   |
||   `;;;;;;;;;;;;"""""";;;;;;;;;;;;;"""""";;;;;;;;;;;;'   |
||     );;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-Catalyst(     |
||     `:;;;:-~~~-:;;:-~~~-:;;;;;:-~~~-:;;:,-~~~-:;;;:'    |
||       ~~~       ~~        ~~~        ~~        ~~~      |
||                     .=============.                     |
||                     | Sr. Ursinho |                     |
||                     `-------------'                     |
|\\_________________________________________________________|
"""
        conexao.send(f"Papai Noel: Parabéns! Você foi uma boa criança! Aqui está seu presente:\n{presente}".encode())
        print("Conversa encerrada: Criança foi aprovada e recebeu o presente.")

    conexao.close()
    servidor_socket.close()

if __name__ == "__main__":
    servidor()
