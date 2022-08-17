item1 = "Apple"
item2 = "Mango"
item3 = "Banana"
item4 = "PineApple"
print(item1)
print(item2)
print(item3)
print(item4)
items = ["Apple", "Mango", "Pineapple", "Banana", "WaterMelon"]
print(items[0])
print(items[0:3])
print(items[-1])
items[0]="Appricot"
items[1]="Goeva"
print(items)
# Now I want to print Pineapple, banana and watermelon
print(items[2:])
items.append("Butter")
print(items)
items.insert(0,"Izhar Ul Haq")
print(items)
food = ["flour", "Gee", "Samoosa"]
drinks = ["pepsi", "juice", "water"]
print(food+drinks)
print(food[0]+" "+drinks[0])
print(len(items))
print("izhar" in items)
print("izhar Ul Haq" in items)
print("Banana" in items)
