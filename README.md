# Protocolo de comunicação para conversar com o Papai Noel

Protocolo de comunicação com o papai noel. Se a criança fez bem durante todo o ano, receberá uma surpresa! Se não... Será mandada embora... :(

### VMs Para Testar:

*Criança (Cliente):* <button style="position: relative; right: 20px; bottom: 20px; border: none; box-shadow: none; width: 130px; height: 40px; line-height: 42px; -webkit-perspective: 230px; perspective: 230px; background: transparent; cursor: pointer; overflow: hidden; font-family: 'Lato', sans-serif; font-weight: 500; text-transform: uppercase; color: #fff;">
  <span style="background: linear-gradient(0deg, rgba(0,172,238,1) 0%, rgba(2,126,251,1) 100%); display: block; position: absolute; width: 130px; height: 40px; box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5), 7px 7px 20px 0px rgba(0,0,0,.1), 4px 4px 5px 0px rgba(0,0,0,.1); transition: all 0.3s ease; top: 0; left: 0;"><a href="https://google.com">Agora!<a></span>
  <span style="background: linear-gradient(0deg, rgba(0,172,238,1) 0%, rgba(2,126,251,1) 100%); display: block; position: absolute; width: 130px; height: 40px; box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5), 7px 7px 20px 0px rgba(0,0,0,.1), 4px 4px 5px 0px rgba(0,0,0,.1); transition: all 0.3s ease; transform: rotateX(90deg); top: 0; left: 0;">Baixar VM</span>
</button>
*IP:* 192.168.10.1

*Papai Noel (Servidor):* <button style="position: relative; right: 20px; bottom: 20px; border: none; box-shadow: none; width: 130px; height: 40px; line-height: 42px; -webkit-perspective: 230px; perspective: 230px; background: transparent; cursor: pointer; overflow: hidden; font-family: 'Lato', sans-serif; font-weight: 500; text-transform: uppercase; color: #fff;">
  <span style="background: linear-gradient(0deg, rgba(0,172,238,1) 0%, rgba(2,126,251,1) 100%); display: block; position: absolute; width: 130px; height: 40px; box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5), 7px 7px 20px 0px rgba(0,0,0,.1), 4px 4px 5px 0px rgba(0,0,0,.1); transition: all 0.3s ease; top: 0; left: 0;"><a href="https://google.com">Agora!<a></span>
  <span style="background: linear-gradient(0deg, rgba(0,172,238,1) 0%, rgba(2,126,251,1) 100%); display: block; position: absolute; width: 130px; height: 40px; box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5), 7px 7px 20px 0px rgba(0,0,0,.1), 4px 4px 5px 0px rgba(0,0,0,.1); transition: all 0.3s ease; transform: rotateX(90deg); top: 0; left: 0;">Baixar VM</span>
</button>
*IP:* 192.168.10.2

### Considerações:

* Projeto criado em Python v.3.13
* Roda no software *IDLE*
* As VMs devem possuir 2 adaptadores de rede (NAT e Rede Interna)
* A rede Interna deve ter o mesmo nome em ambas as VMs
* O Firewall deve estar desativado para garantir que não haja impedimentoos de conexão

### Verificação de conexão:

``` ipconfig ``` - verificar se os ips estão configurados corretamente
``` ping ip.ip.ip.ip ``` - verificar se as máquinas estão enviando e recebendo pacotes, pode testar com os dois ips nas duas máquinas