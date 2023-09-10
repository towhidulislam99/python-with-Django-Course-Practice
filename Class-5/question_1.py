# import math

# sample_data = [2, 4, 4, 4, 5, 5, 7, 9]

# sample_mean = sum(sample_data) / len(sample_data)

# summation = sum((x - sample_mean) ** 2 for x in sample_data)


# standard_deviation = math.sqrt(summation / (len(sample_data) - 1))

# print(standard_deviation)

import math
sample_data = [2, 4, 4, 4, 5, 5, 7, 9]
n = len(sample_data)
sample_mean = sum(sample_data) / n
summation = 0;
for x in sample_data:
    summation += (x-sample_mean) ** 2
standard_deviation =  math.sqrt (summation / (n-1))
round_standard_deviation = math.floor(standard_deviation)
print("{:.2f}".format(standard_deviation))
print("{:.1f}".format(round_standard_deviation))



