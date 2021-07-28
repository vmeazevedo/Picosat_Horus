import serial
import numpy
import matplotlib as plt
from drawnow import *

# Lista para armazenamento dos dados
altitude = []
pressao = []
temperatura = []
cnt=0
plt.ion()

arduinoData = serial.Serial('com8', 9600)
print("Conexão realizada com sucesso!")

# Função responsável pelo dashboard
def live_stream():
    plt.subplot(3,1,1)
    plt.title("Live Streaming - Sensor de Altitude")
    plt.grid(True)
    plt.ylabel('Altitude m')
    plt.plot(altitude, 'ro-', label='Metros m')
    plt.legend(loc='upper left')

    plt.subplot(3,1,2)
    plt.title("Live Streaming - Sensor de Pressão hPa")
    plt.grid(True)
    plt.ylabel('Pressão hPa')
    plt.plot(pressao, 'ro-', color='blue', label='Pressão hPa')
    plt.legend(loc='upper left')

    plt.subplot(3,1,3)
    plt.title("Live Streaming - Sensor de Temperatura")
    plt.grid(True)
    plt.ylabel('Temperatura °C')
    plt.plot(temperatura, 'ro-', color='green', label='Temperatura °C')
    plt.legend(loc='upper left')
    plt.tight_layout()
  

while True:
    while (arduinoData.inWaiting()==0):
        pass
    # Lemos os dados de output dos sensores
    arduinoString = arduinoData.readline()
    # Decodificamos os valores e transformamos eles em string
    decoded_values = str(arduinoString[0:len(arduinoString)].decode("utf-8"))
    # Tratamos o dados
    dataArray = decoded_values.split(",")

    # Separamos o dados a ser impresso por posição do index
    alt = float(dataArray[0])
    press = float(dataArray[1])
    temp = float(dataArray[2])
    
    # Alimentamos nossa lista com os dados atualizados
    altitude.append(alt)
    pressao.append(press)
    temperatura.append(temp)

    # Grafico de live Streaming
    drawnow(live_stream)
    plt.pause(.0000001)

    # Contador para plotar no gráfico os ultimos 50 registros
    cnt=cnt+1
    if(cnt>50):
        altitude.pop(0)
        pressao.pop(0)
        temperatura.pop(0)

    print(dataArray)
