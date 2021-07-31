import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from datetime import datetime


fig = plt.figure(figsize=(8, 8))
m = Basemap(
    resolution='l', # resolução baixa
    projection='lcc', 
    width=17E5,
    height=17E5,
    lon_0=-46.4873986,
    lat_0=-23.6399634,
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
x, y = m(-46.4873986, -23.6399634)
plt.plot(x, y, '*', color='white', markersize=5)
plt.text(x, y, ' GPS - Sinal',color='white', fontsize=9)
plt.show()

