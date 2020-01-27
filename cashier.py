# # product_list[ {"name": "appales",
#         "price":.2,
#         "quantity":4
#     },
#     {   
#         "name": "carrot",
#     "price": .1,
#     "quantity": 1

#     },
#     {"name": "flour",
#         "price":.1.3,
#         "quantity":4
#     },
#     {
#     "name": "water bottles",
#         "price": 0.05,
#         "quantity": 10
#     },
# ]
# cart[]

# def shopping_list(product_list):
#     counter = 1
#     for product in product_list
#     print(" %d. %s" % (countrer,product['name']))
#     print("- Color: %s" % product['color'])
#     print("- Price: %f" % product['price'])
#         counter+=1
# list["Item:", "Price:", "Quantity,"]

# cart.append(item_name)
    # item_price = int(input("Price: "))
    # item_quantity = int(input("Quantity: "))
    # item_name = input("Item (enter 'done' when finished): ")

cart =[]    
def shopping(cart):
    item_name = input("Item (enter 'done' when finished): ")
    while item_name != "done":
        price = float(input("price: "))
        quantity = int(input("quantity: "))
        item = {"name": item_name, 
            "price": price, 
            "quantity": quantity
            }
        cart.append(item)
        item_name = input("Item (enter 'done' when finished): ")
        return cart

def checkout(cart):
    print("---------")
    print("Recipt")
    print("---------")
    total =0.0

    for product in cart: 
        print("%d %s %f" % (item["quantity"], item["name"], item["price"]))  
        total += (item["price"]* item["quantity"])
    print("---------")
    print("Total price: %fKWD " % (total))
        
cart = shopping(cart)
checkout(cart)




    




# print(Item, Price, Quantity)


   
