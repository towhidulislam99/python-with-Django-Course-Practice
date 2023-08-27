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


Space_cost = 50

staff_cost = 60

Total_cost_Black = Transportation_cost_C1 + Utility_cost_C1 + Space_cost + staff_cost
Total_cost_vanila = Transportation_cost_C2 + Utility_cost_C2 + Space_cost + staff_cost
Total_cost_red = Transportation_cost_C3 + Utility_cost_C3 + Space_cost + staff_cost
Total_cost_lemon = Transportation_cost_C4 + Utility_cost_C4 + Space_cost + staff_cost
Total_cost_chocolate = Transportation_cost_C5 + Utility_cost_C5 + Space_cost + staff_cost

Total_cost_Black_Purchase = Total_cost_Black * 5
Total_cost_vanila_Purchase = Total_cost_vanila * 7
Total_cost_red_Purchase = Total_cost_red * 10
Total_cost_lemon_Purchase = Total_cost_lemon * 5
Total_cost_chocolate_Purchase = Total_cost_chocolate * 9


black_forest =  780
vanila_cake = 600
red_velved = 800
lemon_spongecake =650
chocolate_cake = 660

discountPrice_Black = (black_forest*5)/100
discountPrice_Vanila = (vanila_cake*5)/100
discountPrice_Red = (red_velved*5)/100
discountPrice_Lemon = (lemon_spongecake*7)/100
discountPrice_Chocolate = (chocolate_cake*7)/100

TotalDiscountPrice_Black = black_forest - discountPrice_Black
TotalDiscountPrice_Vanila = vanila_cake - discountPrice_Vanila
TotalDiscountPrice_Red = red_velved - discountPrice_Red
TotalDiscountPrice_Lemon = lemon_spongecake - discountPrice_Lemon
TotalDiscountPrice_Chocolate = chocolate_cake - discountPrice_Chocolate

TotalDiscountPrice_Black_Sell = TotalDiscountPrice_Black * 5
TotalDiscountPrice_Vanila_Sell = TotalDiscountPrice_Vanila * 7
TotalDiscountPrice_Red_Sell = TotalDiscountPrice_Red * 10
TotalDiscountPrice_Lemon_Sell = TotalDiscountPrice_Lemon * 5
TotalDiscountPrice_Chocolate_Sell = TotalDiscountPrice_Chocolate * 5

Totalamountof_Purchase = Total_cost_Black_Purchase + Total_cost_vanila_Purchase + Total_cost_red_Purchase + Total_cost_lemon_Purchase + Total_cost_chocolate_Purchase
Totalamountof_Sell = TotalDiscountPrice_Black_Sell + TotalDiscountPrice_Vanila_Sell + TotalDiscountPrice_Red_Sell + TotalDiscountPrice_Lemon_Sell + TotalDiscountPrice_Chocolate_Sell

TotalamountofProfit_Sell = Totalamountof_Sell - Totalamountof_Purchase

Total_Profit_Percentage = (TotalamountofProfit_Sell*100)/Totalamountof_Purchase

print("Total Amount Of Profit After Sell: ", TotalamountofProfit_Sell)
print("Estimate % of Profit: ", Total_Profit_Percentage)

