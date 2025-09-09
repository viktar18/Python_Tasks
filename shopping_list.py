#List of five items to buy
items_list = ["Bread","Tea","Milk","Sugar","Suya"]
print(f"The first and last item on my shopping list is {items_list[0]} and {items_list[4]}")

#Adding 2 more items to the shopping list
items_list.append("Coffe")
items_list.append("Butter")

#Dictionary for the five list
items_dict = {
"Bread":2000,
"Tea":1500,
"Milk":1000,
"Sugar":800,
"Suya":1500
}

#To find the price of the most expensive item.
higest_price = max(items_dict.values())
print(f"The price of the most expensive item is: {higest_price}")

#Finding the total cost of the items
total_cost = sum(items_dict.values())

#A tuple of my 3 favorite items
favorite_items = ("Suya","Bread","Milk")
print(f"The 3 favorite items on my shopping list is: {favorite_items}")

#Displaying the items in my shopping list in alphabetical order.
items_list.sort()
print(items_list)

