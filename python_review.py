import random
temperatures = []
for i in range(7):
	temperatures.append(random.randint(26,40))
days_of_the_week = ["Sunday","Monday","Tuesday","Wednsday","Thursday","Friday","Saturday"]
good_days_count = 0
filtered_days = []
for i in range(7):
	if temperatures[i] %2==0:
		good_days_count= good_days_count +1
	else:
		filtered_days.append(days_of_the_week[i])
Highest_temp = max(temperatures)
Highest_temp_day = temperatures.index(Highest_temp)
print(days_of_the_week[Highest_temp_day])
print(Highest_temp)

Lowest_temp = min(temperatures)
Lowest_temp_day = temperatures.index(Lowest_temp)
print(days_of_the_week[Lowest_temp_day])
print(Lowest_temp)


average = sum(temperatures)/7

above_avg = []

for p in range(7):
	if temperatures[p] > average:
		above_avg.append(temperatures[p])


print("The weather report:")
for i in range(7):
	print(str(days_of_the_week[i]) + ":" + str(temperatures[i]))
print(f"Shelly has {good_days_count} good days")
print(f"The hottest temperature was : {Highest_temp} on {days_of_the_week[Highest_temp_day]}")
print(f"The hottest temperature was : {Lowest_temp} on {days_of_the_week[Lowest_temp_day]}")
print(f"The average temperature is {average}")
print(f"days above average {above_avg}")

