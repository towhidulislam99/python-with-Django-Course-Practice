import sys
import time
user_integer = input("Please give  Value Integer: ")
user_float = float(input("Please give  Value Float: "))
user_double = float(input("Please give  Value Double: "))
user_character = input("Please give  Value Charecter: ")
user_string = input("Please give  Value String: ")
print("\n")

start_time1 = time.time()
for i in range(1000000):
   int_size = sys.getsizeof(user_integer)
end_time1 = time.time()
claculate_time = end_time1 - start_time1


start_time2 = time.time()
for i in range(1000000):
  float_size = sys.getsizeof(user_float)
end_time2 = time.time()
claculate_time2 = end_time2 - start_time2


start_time3 = time.time()
for i in range(1000000):
   double_size = sys.getsizeof(user_double)
end_time3 = time.time()
claculate_time3 = end_time3 - start_time3


start_time4 = time.time()
for i in range(1000000):
   char_size = sys.getsizeof(user_character)
end_time4 = time.time()
claculate_time4 = end_time4 - start_time4


start_time5 = time.time()
for i in range(1000000):
   string_size = sys.getsizeof(user_string)
end_time5 = time.time()
claculate_time5 = end_time5 - start_time5

print(f"Execution time Intager: {claculate_time:.6f} seconds")
print(f"Memory size Intager : {int_size} bytes")
print("\n")

print(f"Execution time Float: {claculate_time2:.6f} seconds")
print(f"Memory size Float : {float_size} bytes")
print("\n")

print(f"Execution time Double: {claculate_time3:.6f} seconds")
print(f"Memory size Double : {double_size} bytes")
print("\n")

print(f"Execution time Charecter: {claculate_time4:.6f} seconds")
print(f"Memory size Charecter : {char_size} bytes")
print("\n")

print(f"Execution time String: {claculate_time5:.6f} seconds")
print(f"Memory size String : {string_size} bytes")
print("\n")


