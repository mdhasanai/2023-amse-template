# Electric Vehicle Charging Patterns and Infrastructure Analysis in Germany

This repository contains a data science project that analyzes the availability and usage patterns of electric vehicle (EV) charging facilities in Germany. The aim is to provide insights into the current state of EV charging infrastructure, understand usage behaviors, and provide recommendations for future expansions.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Dependencies](#dependencies)
3. [Data Sources](#data-sources)
4. [Data Loading](#data-loading)
5. [Exploratory Data Analysis](#exploratory-data-analysis)
6. [Limitations and Conclusion](#limitations-and-conclusion)

## Project Overview

- Objective: Understand the distribution and usage patterns of EV charging stations in Germany.
- Questions:
  - What are the usage patterns of electric vehicle charging stations in Germany?
  - How does the number of charging points and power capacity vary across different types of charging stations?
  - Which areas in Germany have the highest and lowest concentration of charging stations?
  - Are certain types of charging stations more prevalent in specific regions or urban areas?

## Dependencies

```bash
pip install pandas plotly 'SQLAlchemy==1.4.46' nbformat pysqlite seaborn matplotlib
```

## Data Sources

1. **Electric Charging Station**:
   - **Type**: CSV
   - [Metadata URL](https://mobilithek.info/offers/-2989425250318611078)
   - [Data URL](https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv)
   
2. **E-Ladesäulenregister**:
   - **Type**: XLSX
   - [Metadata URL](https://www.govdata.de/web/guest/daten/-/details/e-ladesaulenregister)
   - [Data URL](https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx?__blob=publicationFile&v=21)

## Data Loading

Code provided in the project imports necessary libraries, connects to an SQLite database, and loads datasets into Pandas dataframes. For comprehensive data processing, both datasets were merged, cleaned, and preprocessed.

## Exploratory Data Analysis

The project contains detailed analysis on:

1. Distribution of the number of charging points.
2. Usage patterns based on the type of charging device.
3. Variation in the number of charging points and power capacity across different types of charging stations.
4. Regions in Germany with the highest and lowest concentration of charging stations.
5. Types of charging stations prevalent in certain regions or urban areas.

## Limitations and Conclusion

- **Limitations**:
  - Data quality and biases might affect the analysis.
  - Potential underestimation due to only considering registered charging stations.
  - Lack of population density data.
  - No future projections or predictions provided.

- **Conclusion**: 
  - The analysis highlights the current state of the EV charging landscape in Germany.
  - Emphasizes the need for expanding the charging network in areas with limited coverage.
  - Regular monitoring and updates are crucial for keeping up with the evolving EV landscape.

## Usage

Fork or clone the repository and execute the Jupyter Notebook to see the detailed analysis and visualizations. Make sure to install all the dependencies mentioned above.

## License

This project is open-source and available to everyone. Feel free to use, modify, or distribute as needed. Make sure to reference this repository if you use any part of the analysis or code.

--- 

For any additional information or queries, open an issue in this repository or contact: mdhasan.nsu@gmail.com

