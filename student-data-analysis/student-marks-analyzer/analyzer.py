import numpy as np

marks = [60,70,80,90,50,40,77,88,44]

#converting list to numpy array-----
arr = np.array(marks)

total = np.sum(arr)
print("Total Marks" , total)

avg = np.mean(arr)
print ("Average" , avg)

highest = np.max(arr)
print("Highest Marks" , highest)

lowest = np.min(arr)
print("Lowest Marks" , lowest)







