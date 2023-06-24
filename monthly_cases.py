import datetime
import matplotlib.pyplot as plt
import main


dates = main.dates_Aze 
case_numbers = main.new_Cases_Aze  

# Convert date strings to datetime objects
dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]

# Create a dictionary to store monthly totals
monthly_totals = {}

# Iterate over the dates and case numbers to calculate monthly totals
for date, cases in zip(dates, case_numbers):
    month_year = date.strftime("%Y-%m")  # Extract the month and year
    if month_year in monthly_totals:
        monthly_totals[month_year] += cases
    else:
        monthly_totals[month_year] = cases

# Sort the monthly totals by date
sorted_totals = sorted(monthly_totals.items(), key=lambda x: datetime.datetime.strptime(x[0], "%Y-%m"))

# Extract the sorted dates and case numbers
sorted_dates = [date for date, _ in sorted_totals]
sorted_cases = [cases for _, cases in sorted_totals]

# Generate the bar chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_dates, sorted_cases)
plt.xlabel('Month')
plt.ylabel('Total Cases')
plt.title('Monthly COVID-19 Cases in Azerbaijan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
