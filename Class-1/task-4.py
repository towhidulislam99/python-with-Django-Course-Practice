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

print("Discount-Price-Black:", TotalDiscountPrice_Black, "Discount-Price-Vanila:", TotalDiscountPrice_Vanila, "Discount-Price-Red:",TotalDiscountPrice_Red, "Dicount-Price-Lemon:", TotalDiscountPrice_Lemon, "Discount-Price-Chocolate:", TotalDiscountPrice_Chocolate)


