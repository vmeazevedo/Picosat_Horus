import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from datetime import datetime
from drawnow import *


def iss_latitude():   
    url = "http://api.open-notify.org/iss-now.json"
    resposta = requests.get(url)
    dados = resposta.json()
    latitude = dados['iss_position']['latitude']
    return latitude

def iss_longitude():   
    url = "http://api.open-notify.org/iss-now.json"
    resposta = requests.get(url)
    dados = resposta.json()
    longitude = dados['iss_position']['longitude']
    return longitude

def plot_iss():

    latitude = iss_latitude()
    longitude = iss_longitude()

    #plt.figure(figsize=(8,8), constrained_layout=True)
    plt.subplot(1,1,1)
    plt.title("Live Streaming - ISS")
    plt.plot(latitude,longitude, '*',color='black', label='Sinal GPS')
    plt.legend(loc='upper left')
    plt.tight_layout()
    
    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_geometry("+700+100")

    m = Basemap(
        resolution='c', # resolução baixa
        projection='lcc', 
        width=15E6,
        height=15E6,
        lon_0=longitude,
        lat_0=latitude,
        )

    # exibe uma imagem de mármore azul (de http://visibleearth.nasa.gov) como plano de fundo do mapa
    m.bluemarble(scale=0.9, alpha=1)        
    # mostra o contorno dos países
    m.drawcountries(linewidth=0.8, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
    # mostra o contorno dos estados
    m.drawstates(linewidth=0.8, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
    # Sombreia as regiões do mapa que estão escuras no momento especificado pela data
    date = datetime.utcnow()
    m.nightshade(date)

    # Passando as coordenadas (long,lat) para plotar (x,y) no mapa
    x, y = m(longitude, latitude)
    plt.plot(x, y, '*', color='white', markersize=5)
    plt.text(x, y, ' ISS - Sinal',color='white', fontsize=9)
    plt.pause(3)


while True:
    # Grafico de live Streaming
    drawnow(plot_iss)
    plt.pause(1)
    plt.close("all")
