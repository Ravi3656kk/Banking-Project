import random
seat_price = {
      "SL": 600,
      "AC-3": 1400,
      "AC-2": 2400,
      "AC-1": 300
}
avilable_seat = list(1,100)

while avilable_seat:
      print("\n...congrats your ticket is booked...")
      name = input("Enter your name: ")
      age = int(input("Enter your age "))
      category = input("Enter seat category(SL,AC-1, AC-2, AC-3): ")

      if category not in seat_price:
            print("invaled seat category. try again")
            if age < 6:
                  price = 0
            else:
                  price = seat_price[category]

            seat_number = random.choice(avilable_seat)
            avilable_seat.remove("seat_number")

            print("\n......ticket booked........")
            print("Name", name)
            print("Age", age)
            print("seat cathery", category)
            print("seat number:", seat_number)
            print ("ticket price: ", price)
            print(f"{len(avilable_seat)} seat(s) reamaning.")   

            more = input("\n want to book another ticket? (yes/no): ").lower()
            if more != "yes":
                  break
            if not avilable_seat:
                  print("\n all seat are booked.try again latter.")

    