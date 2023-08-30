import sys
import time
start_time = time.time()
input = (input("Please give Double Value: "))
for i in range(1000000):
   doublet_size = sys.getsizeof(input)
end_time = time.time()
calculate_time = end_time - start_time
print(f"Execution time: {calculate_time:.6f} seconds")
print(f"Memory size of Double: {doublet_size} bytes")