# Picosat_Horus
Desenvolvimento e produção de um picossatélite para realizações de medições atmosféricas e envio de telemetria por RF.

![download](https://user-images.githubusercontent.com/40063504/126914282-48e06e31-83de-4a18-91f1-eec003de2222.png)
_obs: Imagem meramente ilustrativa_


### Objetivo Final
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

#### Lista de materiais
- **BMP180:** Sensor de pressão (300 à 1100hPa) e temperatura (-40 à +85°C).
- **RTC DS3231:** Relógio de tempo real de alta precisão e baixo consumo de energia.
- **MPU 6050:** Acelerômetro e Giroscópio 3 Eixos 6 DOF.
- **GPS NEO-6M:** Módulo GPS NEO-6M ublox.
- **SD Card:** Utilizado como datalogger.
- **Mini câmera digital:** Utilizado para captação de áudio e vídeo do voo.
- **PowerBank:** Utilizado para energizar os componentes
- **Arduino Nano V3:** Microcontrolador ATmega328

#### Protótipo / Protoboard
![image](https://user-images.githubusercontent.com/40063504/127258064-80d4414e-5d2b-4d77-bf73-99c5430bccbd.png)

_Figura 1 - Protótipo Picosat Horus versão 1_


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
- _Integração do modo de visualização do GPS ao dashboard inicial.
- _Apresentação dos dados de telemetria em tempo real em nossa estação de solo.

![Figure_1](https://user-images.githubusercontent.com/40063504/127744964-3d4227bc-6bd9-4ff7-b9b0-3927be43a010.png)

https://user-images.githubusercontent.com/40063504/127744967-6b089bce-fc8b-431d-9497-ab9e0f8e1d2f.mp4


