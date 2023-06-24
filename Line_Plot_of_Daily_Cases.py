import main
import matplotlib.pyplot as plt


plt.title("Daily New Cases in Azerbaijan")

plt.scatter(range(len(main.dates_Aze)), main.new_Cases_Aze,s=20)

plt.xticks(range(len(main.dates_Aze)),main.dates_Aze,rotation=45)
plt.xlabel("Date")

# Get the current axes object
ax = plt.gca()

# Reduce x-axis label size
ax.set_xticklabels(ax.get_xticks(), fontsize=7)  # Adjust the fontsize value 



plt.yticks(range(0, max(main.new_Cases_Aze) + 1, 500))  # Set the y-axis tick locations at intervals of 500
plt.ylabel("New Cases")
plt.ylim(ymin=0, ymax=8000)  # Set the y-axis limits

# Add a pause every 30 ticks
tick_interval = 30
x_ticks = range(len(main.dates_Aze))
plt.xticks(x_ticks[::tick_interval], main.dates_Aze[::tick_interval], rotation=45)

plt.grid(True)

plt.show()