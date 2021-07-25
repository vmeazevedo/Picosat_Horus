# Picosat_Malloner
Desenvolvimento e produção de um picossatélite para realizações de medições atmosféricas e envio de telemetria por RF.

![download](https://user-images.githubusercontent.com/40063504/126914282-48e06e31-83de-4a18-91f1-eec003de2222.png)

## Definição de Picossatélite
O termo picossatélite ou picosat é utilizado para designar um satélite artificial com uma massa menor do que 1 kg. 

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

## Diário de missão
O objetivo final desse projeto é realizar a produção e lançamento de um picosatélite na estratosfera (20km ~ 40km), realizando o registros dos sensores em log e transmitindo a telemetria dos sensores em tempo real.

### Missão I
#### Lista de materiais
- **BMP180:** Sensor de pressão (300 à 1100hPa) e temperatura (-40 à +85°C).
- **RTC DS3231:** Relógio de tempo real de alta precisão e baixo consumo de energia.
- **DHT AM2302:** Sensor de temperatura (-40º a +80ºC) e umidade (0 a 100% UR).
- **SD Card:** Utilizado como datalogger.
- **Mini câmera digital:** Utilizado para captação de audio e video do vôo.
- **PowerBank:** Utilizado para energizar os componentes
- **Arduino Nano V3:** Microcontrolador ATmega328

#### Objetivo de missão
- Envio do Picosat em um balão meteorológico de forma controloda a uma altitude X a ser definida.
- Realização da captura de audio e video de todo percurso de subida e descida.
- Realizar a medição de data/hora, pressão, temperatura, umidade e altitude através dos sensores acoplados ao picosat.
- Registrar todos os dados capturados pelos sensores no datalogger.
- Realizar um pouso suave em terra e recuperar os dados da missão.


### Missão II
#### Upgrades esperados
- Inclusão do modulo de GPS NEO-6 u-blox.
- Inclusão de um sistema de transmissão de telemetria utilizando o Transceptor RF 433MHz HC-12.
