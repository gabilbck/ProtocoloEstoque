# 💬 Protocolo de comunicação para conversar com o Papai Noel 🎅

*Imagine só:* o Natal está chegando, e o espírito natalino já tomou conta de todos os cantos. Luzes piscam, músicas tocam, e o cheiro de biscoitos recém-assados está no ar. Mas aí você descobre uma notícia preocupante... O Papai Noel pegou um resfriado! Isso mesmo, ele não pode atender as crianças pessoalmente este ano.

Felizmente, você, sendo uma criança brilhante e cheia de criatividade, encontrou uma solução incrível: um programa especial que permite conversar com o Bom Velhinho através de um protocolo de comunicação super fácil de usar!

Funciona assim: a cada pergunta que o Papai Noel fizer, você responde. Se sua resposta for positiva, indicando que você foi uma boa criança durante o ano, a conversa continua e você se aproxima do tão esperado presente de Natal. Mas cuidado! Se você não tiver sido tão comportado assim... o Papai Noel poderá encerrar a conversa, e lá se vão suas chances de receber aquele presente tão desejado.

### VMs Para Testar:

**Criança (Cliente):** <a href="#">Baixar VM</a> <br>
**IP:** 192.168.10.1

**Papai Noel (Servidor):** <a href="#">Baixar VM</a> <br>
**IP:** 192.168.10.2

### Considerações:

* As VMS roda em SO Windows 10
* Necessário, pelo menos, 30 GBs de armazenamento para baixar ambas VMs
* As VMs devem estar configuradas com 2 adaptadores de rede (NAT e Rede Interna)
* A rede Interna deve ter o mesmo nome em ambas as VMs
* O Firewall deve estar desativado para garantir que não haja impedimentoos de conexão
* Projeto criado em Python v.3.13
* Roda no software *IDLE*

### Verificação de conexão:

* ``` ipconfig ``` - verificar se os ips estão configurados corretamente
  * Se não estiver correto, deve ser alterado manualmente pelas configurações de rede no *Painel de Controle* > *Central de Rede e Compartilhamento* > *Alterar configurações do Adaptador* > (Selcionar a Ethernet sem conexão e botão direito) *Propriedades* > Opção *Protocolo IPV4* > *Propriedades* > (Desmarque a primeira opção e marque a outra) > Configure o primeiro IP como 192.168.10.1 (para a Criança) e 192.168.10.2 (para o Noel) > Clique em OK e pronto.
  * Teste o comando novamente e veja se foi alterado corretamente
* ``` ping ip.ip.ip.ip ``` - verificar se as máquinas estão enviando e recebendo pacotes, pode testar com os dois ips nas duas máquinas
  * Caso não funcione, verifique o passo anteerior, ou deligue a VM e verifique se os adaptadores estão corretamente configurados na VM do VirtualBOX.  
