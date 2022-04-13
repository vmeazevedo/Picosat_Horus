# Picosat_Horus
Desenvolvimento e produção de um picossatélite para realizações de medições atmosféricas e envio de telemetria por RF.

![download](https://user-images.githubusercontent.com/40063504/126914282-48e06e31-83de-4a18-91f1-eec003de2222.png)
_obs: Imagem meramente ilustrativa_

![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0) [![Twitter Follow](https://img.shields.io/twitter/follow/vmeazevedo.svg?style=social)](https://twitter.com/vmeazevedo) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Vinícius_Azevedo%20-blue)](https://www.linkedin.com/in/vin%C3%ADcius-azevedo-45180ab2/)

![Star](https://img.shields.io/github/stars/vmeazevedo/Picosat_Horus?style=social)
![Fork](https://img.shields.io/github/forks/vmeazevedo/Picosat_Horus?label=Fork&style=social)


## Apoie esse projeto! 💵💵
Olá!
Você pode realizar doações de qualquer banco para minha chave Pix Itaú: **865875c7-c1cc-4254-8585-7c1616dfbc59**


## Projeto de Pesquisa
Estudo do comportamento de microcontroladores Atmega328 ao longo da variação de altitude e temperatura em missões espaciais.

## Objetivo de Missão
- Realizar a produção e lançamento de um picosatélite na estratosfera através de HAB (Balão de alta altitude).
- Realizando a captura dos dados atmosféricos através do sensores acoplados ao picosat.
- Realizar o registro de logs dos sensores e do sistema.
- Realizar a captura de áudio e vídeo todo o voo.
- Realizar o envio de telemetria em tempo real.
- Recuperação da carga e dos dados.


## Definição de Picossatélite
O termo picossatélite ou picosat é utilizado para designar um satélite artificial com uma massa menor do que 1 kg. 

Link: https://pt.wikipedia.org/wiki/Sat%C3%A9lite_miniaturizado


## Vantagens
- Baixo custo de fabricação.
- Produção em massa facilitada.
- Custo de lançamento menor.
- Possibilidade de serem lançados em grupos (piggyback) ou junto com satélites maiores.
- Em caso de falhas, a perda (financeira) é mínima.

## Limitações
- Geralmente têm uma vida útil mais curta.
- A capacidade do hardware de bordo é menor.
- Menor potência de transmissão de dados.
- Decaimento orbital mais rápido.


## Diário de Bordo
### Missão I
#### Objetivo de missão
- Envio do Picosat em um balão meteorológico de forma controlada a uma altitude X a ser definida.
- Realização da captura de áudio e vídeo de todo percurso de subida e descida.
- Realizar a medição de data/hora, pressão, temperatura, umidade e altitude através dos sensores acoplados ao picosat.
- Registrar todos os dados capturados pelos sensores no datalogger.
- Realizar um pouso suave em terra e recuperar os dados da missão.


## Updates
### 27/07/2021: 
- _Realização dos testes dos sensores bmp180, DS3231 e modulo SC Card._
- _Primeira montagem de teste dos componentes realizada com sucesso._
- _Validação dos registros salvos no datalog._

![log](https://user-images.githubusercontent.com/40063504/127258601-e1fb1e56-ee62-4a9b-90a4-0bbdf42bcf49.jpeg)


### 28/07/2021:
- _Desenvolvimento de um dashboard inicial em python que será a interface da estação de solo para monitoramento live streaming da telemetria dos dados recebidos dos sensores via porta COM._

https://user-images.githubusercontent.com/40063504/127258828-0524be32-c405-49d9-a180-073df0f762e6.mp4

### 29/07/2021:
- _Inclusão do modulo de GPS ao sistema e validação de log com os novos dados de telemetria._
- _Desenvolvimento de um modo de visualização de coordenadas do GPS através de script python, plotando o sinal no mapa de forma amigável._

![WhatsApp Image 2021-07-31 at 12 32 55](https://user-images.githubusercontent.com/40063504/127744906-36191b2e-64b9-4dc2-8913-9bbc871f3b88.jpeg)
![WhatsApp Image 2021-07-31 at 12 28 13](https://user-images.githubusercontent.com/40063504/127744911-6e284f59-6254-4964-a0e7-28ff7481243a.jpeg)

### 31/07/2021:
- _Integração do modo de visualização do GPS ao dashboard inicial._
- _Apresentação dos dados de telemetria em tempo real em nossa estação de solo._

![Figure_1](https://user-images.githubusercontent.com/40063504/127744964-3d4227bc-6bd9-4ff7-b9b0-3927be43a010.png)

https://user-images.githubusercontent.com/40063504/127744967-6b089bce-fc8b-431d-9497-ab9e0f8e1d2f.mp4

### 04/08/2021:
- _Desenvolvimento da primeira PCB do projeto utilizando o software EasyEDA._
- _Futuramente será desenvolvida outra PCB com o sistema de transmissão por RF incluso._

![layout_conexões](https://user-images.githubusercontent.com/40063504/128271947-032a46bb-cd02-41bb-bbcf-087c08a0f3b4.PNG)

![pcb_layout](https://user-images.githubusercontent.com/40063504/128271953-42d18928-90f0-4551-acb8-be58f9707857.PNG)



https://user-images.githubusercontent.com/40063504/128271961-c4afb1bf-5d95-4cc0-81f1-9f9d74a43510.mp4

### 06/08/2021:
- _Desenvolvimento do um script de monitoramento da tensão de alimentação do Microcontrolador e de sua temperatura interna._
- _Desenvolvimento de um novo gráfico para monitoramento da VIN e temperatura interna do microcontrolador._

![Update_monitor](https://user-images.githubusercontent.com/40063504/128581430-b16f1d82-dba3-4801-903c-27e04c965e60.png)

### 07/08/2021:
- _Testes com o sistema preliminar de alimentação do picosat via energia solar._

![solar](https://user-images.githubusercontent.com/40063504/128610020-e8b2a47f-2bc2-4f58-937e-702937d0a11d.PNG)



https://user-images.githubusercontent.com/40063504/128610028-a982d79e-3cf4-4442-8962-9cac5c6e8880.mp4

### 17/08/2021:
- _Desenvolvimento do sistema de Unidade de Medição Inercial para monitorar os dados de estabilização e posicionamento._

![IMU_TESTE](https://user-images.githubusercontent.com/40063504/129812345-69590c7d-0ba5-439e-a3e8-de3e8529f36f.PNG)


https://user-images.githubusercontent.com/40063504/129812302-c0c55daa-0df7-4195-b5dc-750e4aad3463.mp4

