# Multiple Linear Regression Project: Predicting Fire Weather Index (FWI)

## Overview
This project aims to predict the Fire Weather Index (FWI) using a multiple linear regression model on the Algerian Forest Fires dataset. The dataset contains weather and environmental data that can help in understanding the factors contributing to forest fires in Algeria.

## Dataset Information
The dataset includes a total of **244 instances** from two regions of Algeria:
- **Bejaia Region** (Northeast)
- **Sidi Bel-Abbes Region** (Northwest)

Each region contains **122 instances** recorded during the period from **June 2012 to September 2012**. The dataset has been classified into two classes:
- **Fire** (138 instances)
- **Not Fire** (106 instances)

### Attribute Information
The dataset consists of **11 attributes** and **1 output attribute** (class). The attributes are as follows:

- **Date**: (DD/MM/YYYY) Day, month ('June' to 'September'), year (2012) - Weather data observations
- **Temp**: Temperature at noon (maximum temperature) in Celsius degrees (Range: 22 to 42)
- **RH**: Relative Humidity in % (Range: 21 to 90)
- **Ws**: Wind speed in km/h (Range: 6 to 29)
- **Rain**: Total precipitation for the day in mm (Range: 0 to 16.8)
- **FFMC**: Fine Fuel Moisture Code index from the FWI system (Range: 28.6 to 92.5)
- **DMC**: Duff Moisture Code index from the FWI system (Range: 1.1 to 65.9)
- **DC**: Drought Code index from the FWI system (Range: 7 to 220.4)
- **ISI**: Initial Spread Index index from the FWI system (Range: 0 to 18.5)
- **BUI**: Buildup Index index from the FWI system (Range: 1.1 to 68)
- **FWI**: Fire Weather Index (Range: 0 to 31.1)
- **Classes**: Two classes - **Fire** and **Not Fire**

## Objectives
- Develop a multiple linear regression model to predict the Fire Weather Index (FWI).
- Analyze the relationship between weather attributes and fire occurrences.
- Evaluate model performance using appropriate metrics.

## Technologies Used
- Python
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

## Installation
To set up the project, clone this repository and install the required libraries:

```bash
git clone https://github.com/Anitha-Balachandran/ForestFirePrediction.git
cd ForestFirePrediction
pip install -r requirements.txt
