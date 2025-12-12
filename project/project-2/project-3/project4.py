name = input("Enter your name mr/mr.s: ")
age = int(input("Enter your age: "))
seat_catogery = input("Enter seat catogery(SL, AC-3, AC-2, AC-1): ")

seat_price = {
      "SL": 100,
      "AC-3": 350,
      "AC-2": 500,
      "AC-1": 650
}
if age <= 6:
      price = 0
else:
      price = seat_price.get(seat_catogery.upper(), None)

      if price is None:
            print("invalid seat catogery!")
            exit()

print("\n...congrats your ticket booked....")
print("Name:", name)
print("Age:", age)
print("seat catogery:", seat_catogery.upper())
print("Ticket price: ", price)


