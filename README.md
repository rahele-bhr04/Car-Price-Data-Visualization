# Car Price Data Visualization

## Overview
This project explores the relationship between various car features (such as engine size, fuel type, and year) and their prices using data visualization techniques.  
The goal is to uncover patterns, trends, and insights by creating clear and informative plots.
Plots are stored in charts folder.

## Project Structure
```
├── data/              
│     └── cars.csv
├── charts/            # Saved plots (.png files)
├── notebook.ipynb     # Main analysis notebook
├── analysis.py        # Main analysis python file
├── requirements.txt   # List of Python packages needed
└── README.md          # Project description
```

## Visualizations
- **Price distribution(hist plot)**
- **Car features vs price(heatmap)**
- **Year vs price(box plot, line plot)**
- **Power vs price(reg plot)**
- **Brands distribution(bar plot)**
- **Transmission type, kilometers driven, and car price(scatter plot)**
- **Average mileage by number of seats and transmission type(cat plot)**
- **Car price distribution by owner type**
- **Engine size vs. price vs. fuel type ---(bubble chart)**

**Sample Plot:**
```markdown
![Car Price Distribution](https://github.com/rahele-bhr04/Car-Price-Data-Visualization/blob/main/charts/price_ownerType.png?raw=true)
```

## Requirements
Install the required libraries using:
```bash
pip install -r requirements.txt
```

Main libraries used:
- pandas
- matplotlib
- seaborn
- plotly


## How to Run
1. Clone this repository.
2. Install the required packages.
3. Open the `analysis_notebook.ipynb` file using Jupyter Notebook or `analysis.py` using python.
4. Run all (cells) to generate the visualizations.

## Author
[https://github.com/rahele-bhr04]