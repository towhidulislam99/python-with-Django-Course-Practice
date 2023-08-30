import sys
import time
start_time = time.time()
input = float (input("Please give Floating Value: "))
for i in range(1000000):
   float_size = sys.getsizeof(input)
end_time = time.time()
calculate_time = end_time - start_time
print(f"Execution time: {calculate_time:.6f} seconds")
print(f"Memory size of Float: {float_size} bytes")