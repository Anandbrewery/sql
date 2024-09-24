item=input("item name: ")
price=float(input("price: "))
qty=int(input("quantity: "))
total=price*qty
print(f"You have bought {qty} x {item}/s")
print(f"Your total is : ${total}")