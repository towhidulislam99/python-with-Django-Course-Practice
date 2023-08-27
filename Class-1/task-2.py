black_forest =  180
vanila_cake = 150
red_velved = 220
lemon_spongecake =165
chocolate_cake = 170

Transportation_cost_C1 = black_forest + 150
Transportation_cost_C2 = vanila_cake + 150
Transportation_cost_C3 = red_velved + 150
Transportation_cost_C4 = lemon_spongecake + 150
Transportation_cost_C5 = chocolate_cake + 150

Utility_cost_C1 = (Transportation_cost_C1 *3 ) /100
Utility_cost_C2 = (Transportation_cost_C2 * 3) / 100
Utility_cost_C3 = (Transportation_cost_C3 * 3) / 100
Utility_cost_C4 = (Transportation_cost_C4 * 3) / 100
Utility_cost_C5 = (Transportation_cost_C5 * 3) / 100

print(Utility_cost_C1, Utility_cost_C2, Utility_cost_C3, Utility_cost_C4, Utility_cost_C5)

Space_cost = 50

staff_cost = 60

Total_cost_Black = Transportation_cost_C1 + Utility_cost_C1 + Space_cost + staff_cost
Total_cost_vanila = Transportation_cost_C2 + Utility_cost_C2 + Space_cost + staff_cost
Total_cost_red = Transportation_cost_C3 + Utility_cost_C3 + Space_cost + staff_cost
Total_cost_lemon = Transportation_cost_C4 + Utility_cost_C4 + Space_cost + staff_cost
Total_cost_chocolate = Transportation_cost_C5 + Utility_cost_C5 + Space_cost + staff_cost

print(Total_cost_Black, Total_cost_vanila, Total_cost_red, Total_cost_lemon, Total_cost_chocolate)

