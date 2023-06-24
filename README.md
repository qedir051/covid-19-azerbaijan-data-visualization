# covid-19-azerbaijan-data-visualization

This repository contains Python code for analyzing COVID-19 data in Azerbaijan. The data used in this analysis is up until March 2022.

## Data Source

The COVID-19 data used in this analysis is sourced from 'covid-data.csv'. Please refer to their documentation for more details about the data collection methods and updates.

## Library Dependencies

The analysis scripts require the following Python libraries to be installed:

- Python
- Matplotlib
- datetime
- CSV

Make sure you have these libraries installed before running the scripts. You can install them using the following command:

pip install matplotlib datetime csv


## Analysis Scripts

### 1. Daily Cases Line Plot

The script `Line_Plot_of_Daily_Cases.py` imports the data from the `main.py` file and generates a line plot showing the daily new cases in Azerbaijan. The plot is created using the `matplotlib` library.

[Line Plot of Daily Cases](images/dailycases.png)

### 2. Monthly Cases Bar Chart

The script `monthly_cases.py` imports the data from `main.py` and generates a bar chart illustrating the monthly total cases in Azerbaijan. The chart provides insights into the monthly trends of COVID-19 cases.

[Monthly Cases](images/monthcases.png)

## Instructions

To run the analysis scripts, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Place the `covid-data.csv` file in the same directory as the analysis scripts.
4. Install the required Python libraries by running the command mentioned in the "Library Dependencies" section.
5. Run the scripts using the command `python main.py` for the daily cases line plot and `python monthly_cases.py` for the monthly cases bar chart.

Note: Please ensure that the necessary data file (`covid-data.csv`) is present in the same directory as the scripts before running them.

## Results

The generated visualizations provide insights into the COVID-19 situation in Azerbaijan up until March 2022. The line plot showcases the daily new cases, while the bar chart illustrates the monthly total cases. These visualizations help understand the trends and patterns of COVID-19 in Azerbaijan during the specified timeframe.


