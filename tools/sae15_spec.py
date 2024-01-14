#################################################################################################
# FONCTIONS SPECIFIQUES
#------------------------------------------------------------------------------------------------
# Les fonctions à coder selon l'échancier donné dans le document SAE15-Présentation.ipynb
#################################################################################################

#------------------------------------------------------------------------------------------------
# importations des modules utiles
#
# attention : geopandas et contextily doivent être installés avant l'importation
# utiliser pour cela !pip install ... dans le Notebook principal
#
import pandas as pd             # pour la mise en forme, l'analyse et la publication
import datetime as dt           # pour la détermination de la date
import geopandas as gpd         # pour la spatialisation des données
import matplotlib.pyplot as plt # pour les graphes
import contextily as ctx        # pour l'utilisation de cartes géographiques

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des stands (en %)
def availableDocksRate(stations_df) :

  # votre code...
  # Vérifier si les colonnes nécessaires existent dans le DataFrame
  if 'num_docks_available' not in stations_df.columns or 'num_bikes_available' not in stations_df.columns:
      raise ValueError("Le DataFrame ne contient pas les colonnes nécessaires.")

    # Calculer le taux de disponibilité des stands en %
  numDocksAvailable = stations_df['numDocksAvailable']
  numBikesAvailable = stations_df['numBikesAvailable']


  rate = (numDocksAvailable/(numBikesAvailable+numDocksAvailable)) * 100
  rate.fillna(0, inplace=True)

  return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des vélos (en %)
def availableBikesRate(stations_df) :

  # votre code...
  # Vérifier si les colonnes nécessaires existent dans le DataFrame
  # if ('num_docks_available' not in stations_df.columns) or ('num_bikes_available' not in stations_df.columns):
  #     raise ValueError("Le DataFrame ne contient pas les colonnes nécessaires.")

    # Calculer le taux de disponibilité des vélos en %
  numDocksAvailable = stations_df['numDocksAvailable']
  numBikesAvailable = stations_df['numBikesAvailable']
  
  rate = (numBikesAvailable/(numBikesAvailable+numDocksAvailable)) * 100
  rate.fillna(0, inplace=True)

  return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne la date la plus récente de la mise à jour des données dynamiques
def getLatestDate(stations_df) :

  # votre code...
  # Vérifier si la colonne nécessaire existe dans le DataFrame
  if 'last_reported' not in stations_df.columns:
      raise ValueError("Le DataFrame ne contient pas la colonne nécessaire.")
  
  # Récupérer la date la plus récente
  date = stations_df['last_reported'].max()
  date = dt.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

  return date

#------------------------------------------------------------------------------------------------
# fonction qui retourne les mesures statistiques  d'une clé du DataFrame de stations
def stationStatistics(stations_df, stations_df_key) :

  # calcul des mesures statistiques
  # votre code...
  if stations_df_key not in stations_df.columns:
      raise ValueError("La clé n'existe pas dans le DataFrame.")
  
  # check if the column is numeric
  if stations_df[stations_df_key].dtype == 'object':
      raise ValueError("La clé n'est pas numérique.")
  
  mean = stations_df[stations_df_key].mean()
  std_dev = stations_df[stations_df_key].std()
  median = stations_df[stations_df_key].median()
  min = stations_df[stations_df_key].min()
  max = stations_df[stations_df_key].max()
  mode = stations_df[stations_df_key].mode()[0]
  var = stations_df[stations_df_key].var()
  sum = stations_df[stations_df_key].sum()
  count = stations_df[stations_df_key].count()
  skew = stations_df[stations_df_key].skew()
  kurt = stations_df[stations_df_key].kurt()
  quantile_25 = stations_df[stations_df_key].quantile(0.25)
  quantile_50 = stations_df[stations_df_key].quantile(0.5)
  quantile_75 = stations_df[stations_df_key].quantile(0.75)



  # créaton d'un DataFrame des mesures statistiques avec le nom de la clé passée à la fonction
  # votre code...
  stats = pd.DataFrame({
            'Mean': [mean],
            'Median': [median],
            # 'Mode': [mode],
            'Standard Deviation': [std_dev],
            # 'Variance': [var],
            'Min': [min],
            'Max': [max],
            # 'Sum': [sum],
            'Count': [count],
            # 'Skewness': [skew],
            # 'Kurtosis': [kurt],
            # 'Quantile 25%': [quantile_25],
            # 'Quantile 50%': [quantile_50],
            # 'Quantile 75%': [quantile_75]
        }, index=[stations_df_key])

  return stats

#------------------------------------------------------------------------------------------------
# fonction qui exporte au format HTML le DataFrame des mesures statistiques
def exportStatistics(stats_df, filename) :

  # votre code...
  stats_html = stats_df.to_html(index=False)

  # Écrire le contenu HTML dans un fichier
  with open(filename, 'w') as file:
      file.write(stats_html)

  return

#------------------------------------------------------------------------------------------------
# fonction qui affiche et exporte la carte des stations Vélibs géolocalisées
def exportCityMap(geo_stations,geo_key, marker_size=None, marker_color=None, title='Just a Map', date=None, filename='map.svg') :
  # figure et axes
  # votre code...
  f, axes = plt.subplots(1, figsize=(15,15))

  # conversion des coordonnées dans le système approprié
  # votre code...
  geo_stations_map = geo_stations.to_crs(epsg=3857)
  
  # affichage en fonction des variables passées en argument
  # votre code...
  if marker_size is None:
    marker_size = geo_stations_map[geo_key]
  else:
    marker_size = marker_size

  if marker_color is None:
    marker_color = 'coolwarm'
  else:
    marker_color = marker_color
     
  
  geo_stations_map.plot(geo_stations[geo_key],ax=axes, markersize=marker_size, cmap=marker_color)
  # effacement des axes gradués
  # votre code...
  axes.set_axis_off()

  # ajout du fond de carte correspondant aux coordonnées géographiques des stations
  # votre code...
  ctx.add_basemap(axes)

  # affichage du titre avec la date de mise à jour
  # votre code...
  if date is None:
      axes.set_title(title)
  else:
      axes.set_title(f"{title} - Mise à jour le {date} \nPoint Color: '{marker_color}'")
      # to make title bigger and bold
      axes.title.set_size(20)
      #axes.title.set_weight('bold')

  # sauvegarde de la carte sur le Drive .png
  # votre code...
  plt.savefig(filename, format='png')

  # set aa string bold in python
  # https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot

  # affichage forçé
  # votre code...
  plt.show()

  return 


