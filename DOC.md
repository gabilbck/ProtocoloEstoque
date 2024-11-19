

---
### **Importação e Configuração**
```python
import socket
```
- Importa a biblioteca `socket` para permitir a comunicação via sockets, que é usada para estabelecer conexões em rede.

```python
def servidor():
```
- Define a função `servidor`, que contém a lógica principal do servidor.

```python
    host = '0.0.0.0'  # Aceita conexões de qualquer IP
    porta = 5000      # Porta de comunicação
```
- `host = '0.0.0.0'`: Configura o servidor para aceitar conexões de qualquer endereço IP.
- `porta = 5000`: Define a porta na qual o servidor ouvirá conexões.

---

### **Criação do Socket**
```python
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- Cria um socket:
  - `socket.AF_INET`: Indica que será usado IPv4.
  - `socket.SOCK_STREAM`: Indica que será usada comunicação baseada em TCP.

```python
    servidor_socket.bind((host, porta))
```
- Vincula o socket ao endereço e porta especificados.

```python
    servidor_socket.listen(1)
```
- Coloca o servidor em modo de escuta, permitindo até 1 conexão pendente.

```python
    print("Papai Noel esperando por uma criança para conversar...\n")
```
- Exibe uma mensagem indicando que o servidor está pronto para aceitar conexões.

---

### **Aceitação de Conexão**
```python
    conexao, endereco = servidor_socket.accept()
```
- Aguarda uma conexão. Quando uma criança (cliente) se conecta:
  - `conexao`: Representa o socket da conexão ativa.
  - `endereco`: Contém o IP e a porta do cliente.

```python
    print(f"Uma criança chegou para conversar! Conectado com {endereco}\n")
```
- Informa que uma criança se conectou ao servidor, exibindo o endereço do cliente.

---

### **Lista de Perguntas**
```python
    perguntas = [
        "Você foi uma boa criança este ano? (sim/não)",
        ...
    ]
```
- Define uma lista de perguntas que o Papai Noel fará à criança.

```python
    todas_respostas_sim = True
```
- Inicializa uma variável de controle que assume `True` se todas as respostas forem "sim".

---

### **Loop de Perguntas**
```python
    for pergunta in perguntas:
        while True:
```
- Percorre todas as perguntas.
- O `while True` garante que a pergunta será repetida até que a criança responda com "sim" ou "não".

---

### **Envio de Pergunta e Recebimento de Resposta**
```python
            conexao.send(pergunta.encode())
```
- Envia a pergunta atual para o cliente. O `encode()` converte a string para bytes.

```python
            resposta = conexao.recv(1024).decode().strip().lower()
```
- Recebe a resposta do cliente:
  - `conexao.recv(1024)`: Lê até 1024 bytes.
  - `decode()`: Converte os bytes recebidos de volta para string.
  - `strip()`: Remove espaços extras.
  - `lower()`: Converte a resposta para letras minúsculas.

```python
            print(f"Criança respondeu: {resposta}")
```
- Exibe a resposta da criança no terminal do servidor.

---

### **Validação da Resposta**
```python
            if resposta == "sim" or resposta == "não":
                break
```
- Se a resposta for válida ("sim" ou "não"), sai do loop `while`.

```python
            else:
                conexao.send("Papai Noel: Eu não entendi sua resposta. Por favor, responda com 'sim' ou 'não'.\n".encode())
```
- Caso contrário, envia uma mensagem pedindo uma resposta válida.

---

### **Encerramento Antecipado**
```python
        if resposta != "sim":
            todas_respostas_sim = False
            conexao.send("Papai Noel: Você foi uma má criança! Vá embora!".encode())
            print("Conversa encerrada: Criança foi mandada embora.")
            break
```
- Se a resposta for "não":
  - Define `todas_respostas_sim` como `False`.
  - Envia uma mensagem informando que a criança foi mandada embora.
  - Encerra o loop de perguntas.

---

### **Entrega de Presente**
```python
    if todas_respostas_sim:
        presente = """
{~._.~}
 ( Y )
()~*~()
(_)-(_)
"""
        conexao.send(f"Papai Noel: Parabéns! Você foi uma boa criança! Aqui está seu presente:\n{presente}".encode())
        print("Conversa encerrada: Criança fez bem e recebeu o presente.")
```
- Se todas as respostas forem "sim", envia um "presente" ASCII art para o cliente.

---

### **Encerramento da Conexão**
```python
    conexao.close()
    servidor_socket.close()
```
- Fecha a conexão com a criança e o socket do servidor.

```python
    print("Conexão encerrada.")
```
- Exibe uma mensagem indicando que a conexão foi finalizada.

---

### **Execução do Servidor**
```python
if __name__ == "__main__":
    servidor()
```
- Garante que a função `servidor` será executada apenas se o script for executado diretamente, e não importado como módulo.