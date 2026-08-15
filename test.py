import pandas as pd 

data = pd.read_csv("air_quality.csv") #stores the table into a variable called data

print(data.head(8)) #creates first 5 rows
print(list(data.columns)) #creates first 4 columns


print(f"\nAverage PM2.5: {data['pm2.5'].mean():.2f}") # avg
print("Highest PM2.5:", data["pm2.5"].max()) #maximum
print("Lowest PM2.5:", data["pm2.5"].min()) #minimum

import matplotlib.pyplot as plt

data["date"] = pd.to_datetime(data["date"]) #changes the data column into real dates python can understand

plt.plot(data["date"], data["pm2.5"], marker="o") #puts a dot on each point
plt.xlabel("Date") #titles the x axis date
plt.ylabel("PM2.5") #titles the y axis with pm2.5
plt.title("Simi Valley Air Quality") #titles the whole graph 
plt.xticks(rotation=45) #tilts the dates so they are easier to read
plt.tight_layout() #automatically fixes spacing



period_averages = data.groupby("period")["pm2.5"].mean()

print("\nAverage PM2.5 by period:")

for period, average in period_averages.items():
    print(f"{period.capitalize()}: {average:.2f}")
print("\n")


plt.figure() #tells python to start a new graph

period_averages.plot(kind="bar")
plt.xlabel("Fire Period")
plt.ylabel("Average PM2.5")
plt.title("PM2.5 Before, During, and After the Fire")
plt.xticks(rotation=0)
plt.tight_layout()




plt.show() #displays the graphs
  
