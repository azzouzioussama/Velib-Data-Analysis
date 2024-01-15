# Velib-Data-Analysis - SAE15 Project

## Project Overview
The **Velib-Data-Analysis - SAE15 Project** is dedicated to the analysis and visualization of data from the Vélib' Métropole bike-sharing system in Lyon. The project utilizes Open Data from the Vélib' Métropole API, providing both static and dynamic information about bike stations. The primary goals include reading and interpreting data, processing it, and presenting the results through a web page.

## Project Phases
1. **Importations, Installations, and Configurations:**
   Set up the necessary imports, installations, and configurations for the project.

2. **Récupération des Données Vélib en OpenData:**
   Retrieve bike-sharing data from the OpenData source.

3. **Mise Sous Forme de DataFrames:**
   Organize the data into DataFrames for further analysis.

4. **Analyses Statistiques:**
   Perform statistical analyses on both static and dynamic data, including measures such as min, max, mean, and standard deviation.

5. **Exportation des Mesures Statistiques pour le Web:**
   Export the statistical measures in a format suitable for web publication.

6. **Spatialisation des Données, Exportation pour le Web:**
   Spatialize the data, generate a city map with markers representing bike stations, and export it for web publication.

## Specific Functions
In **tools/sae15_spec.py**:

- `getLatestDate(json_data):`
  Retrieve and format the date of the last update from the dynamic data.

- `availableBikesRate(stations):`
  Calculate and return the availability rates of bikes for each station.

- `availableDocksRate(stations):`
  Calculate and return the availability rates of docks (stands) for each station.

- `stationStatistics(key):`
  Return statistical measures (count, min, max, mean, std) for a specified key in the station DataFrame.

- `exportStatistics(stats, filename):`
  Export a table of statistical measures in HTML format.

- `exportCityMap(stations, marker_size, marker_color, title, date, filename):`
  Generate, display, and export a city map with markers representing stations.

## Supporting Functions
(from **tools/sae15_tools.py**):

- `loadVelibInformation():`
  Load static data from the Vélib' Métropole OpenData.

- `loadVelibStatus():`
  Load dynamic data from the Vélib' Métropole OpenData.

- `getVelibStations(json_data):`
  Extract and return the list of Vélib stations from JSON data.

- `exportToGeoDF(df):`
  Convert a DataFrame to a GeoDataFrame.

## Web Publication
Use the provided tutorial (**SAE15-Publication Web.ipynb**) to publish the results, including statistical measures and the city map, on the web.

## Project Structure
- **web/:** Contains HTML and CSS files for web page publication.
- **tools/:** Houses utility scripts for project support.
- **tests/:** Includes test notebooks for different project activities.
- **projetSAE15.ipynb:** The main Python script for the project.

## Programming Languages
The project involves programming in Python for data processing and analysis, and HTML/CSS for web page presentation.

## Environment
Development in Google Colab using Python. Web pages can be created using any text editor, such as Notepad++.

## Project Workflow
1. **Data Reading:** Read data from Vélib' Métropole stations.
2. **Data Interpretation:** Extract relevant information from the data.
3. **Data Processing:** Perform necessary calculations and analysis.
4. **Textual Representation:** Construct text-based representations using HTML/CSS.
5. **Graphical Representation:** Create graphical representations and export them.

## Evaluation
The project will be evaluated based on project management, code quality, and Python programming skills. Various test units will be provided and should be completed as per the schedule.

## Project Timeline
Refer to the provided schedule for specific tasks and deadlines.

## Activities
### Activity 1: Environment Setup
Ensure the development environment adheres to project specifications. Understand the JSON data format. Deliverable: **tu_Activité1.ipynb**

### Activity 2: OpenData Sources
Access and format datasets from OpenData portals. Deliverable: **tu_Activité2.ipynb**

### Activity 3: Analysis and Web Publication
Publish textual results on a web page. Start formatting data in HTML/CSS. Deliverable: **tu_Activité3.ipynb**

### Activity 4: Graphical Tools
Create graphical representations of data. Integrate graphics into the web page. Deliverable: **tu_Activité4.ipynb**
