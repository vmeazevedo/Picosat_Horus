import serial
import numpy
import matplotlib as plt
from drawnow import *
from mpl_toolkits.basemap import Basemap
from datetime import datetime


# Lista para armazenamento dos dados
latitude = []
longitude = []
altitude = []
pressao = []
temperatura = []
cnt=0
plt.ion()

# Conexão com a porta serial do Arduino
arduinoData = serial.Serial('com8', 9600)
print("Conexão realizada com sucesso!")

# Função responsável pelo dashboard
def live_stream():
    # Plotando o nosso mapa e apresentando as coordenadas do GPS nele
    plt.subplot(1,2,1)
    plt.title("Live Streaming - Sinal de GPS")
    m = Basemap(
        resolution='c', # resolução baixa
        projection='lcc', 
        width=12E6,
        height=12E6,
        lon_0=longitude[-1],
        lat_0=latitude[-1],
        )
    m.bluemarble(scale=0.9, alpha=1)        
    m.drawcountries(linewidth=0.8, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
    m.drawstates(linewidth=0.8, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
    date = datetime.utcnow()
    m.nightshade(date)

    # Passando as coordenadas (long,lat) para plotar (x,y) no mapa
    x, y = m(longitude[-1], latitude[-1])
    plt.plot(x, y, '*', color='white', markersize=5)
    plt.text(x, y, ' GPS - Sinal',color='white', fontsize=9)
    
    # Plot do sensor de altitude
    plt.subplot(3,2,2)
    plt.title("Live Streaming - Sensor de Altitude")
    plt.grid(True)
    plt.ylabel('Altitude m')
    plt.plot(altitude, 'ro-', label='Metros m')
    plt.legend(loc='upper left')
    
    # Plot do sensor de pressão
    plt.subplot(3,2,4)
    plt.title("Live Streaming - Sensor de Pressão hPa")
    plt.grid(True)
    plt.ylabel('Pressão hPa')
    plt.plot(pressao, 'ro-', color='blue', label='Pressão hPa')
    plt.legend(loc='upper left')
    
    # Plot do sensor de temperatura
    plt.subplot(3,2,6)
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
    lat = float(dataArray[0])
    long = float(dataArray[1])
    sat = float(dataArray[2])
    prec = float(dataArray[3])
    alt = float(dataArray[4])
    press = float(dataArray[5])
    temp = float(dataArray[6])
    
    # Alimentamos nossa lista com os dados atualizados
    latitude.append(lat)
    longitude.append(long)
    altitude.append(alt)
    pressao.append(press)
    temperatura.append(temp)

    # Grafico de live Streaming
    drawnow(live_stream)
    plt.pause(.0000001)
    
    # Contador para plotar no gráfico os ultimos 50 registros
    cnt=cnt+1
    if(cnt>50):
        latitude.pop(0)
        longitude.pop(0)
        altitude.pop(0)
        pressao.pop(0)
        temperatura.pop(0)

    #print(dataArray)
