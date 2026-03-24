import numpy as np

Temperature = np.array([33,32,34,22,25,30,22])
print(Temperature)
print()
print("Average Temperature:",np.mean(Temperature))
print()
print("Lowest Temperature:",np.min(Temperature))
print()
print("Highest Temperature:",np.max(Temperature))
print()

Average = np.mean(Temperature)
above_avg = np.sum(Temperature > Average)
below_avg = np.sum(Temperature < Average)
print("Days above Average:", above_avg)
print("Days below average:", below_avg)
print()

hot_days = np.sum(Temperature > 33)
print("Hot days (>33°C):", hot_days)

