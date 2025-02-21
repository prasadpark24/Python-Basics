
total_amount = 0

def calculate_total_cost(item_count, item_price, parcel_cost, chutney_cost, needs_parcel, needs_chutney):
    total = item_count * item_price
    if needs_chutney:
        total += chutney_cost
    if needs_parcel:
        total += parcel_cost
    return total

def idly():
    global total_amount
    print("Price of one Idly is 8 Rupees")
    idly_count = int(input("How many Idlys do you want: "))
    needs_chutney = input("Do you need Coconut/Tomato Chutney? (Yes/No): ").lower() == "yes"
    needs_parcel = input("Do you need a parcel? (Yes/No): ").lower() == "yes"
    
    item_cost = calculate_total_cost(idly_count, 8, 5, 2, needs_parcel, needs_chutney)
    total_amount += item_cost
    print(f"The Total cost for {idly_count} Idlys is: {item_cost} Rupees\n")

def dosai():
    global total_amount
    print("Price of one Dosai is 25 Rupees")
    dosai_count = int(input("How many Dosai do you want: "))
    needs_chutney = input("Do you need Coconut/Tomato Chutney? (Yes/No): ").lower() == "yes"
    needs_parcel = input("Do you need a parcel? (Yes/No): ").lower() == "yes"
    
    item_cost = calculate_total_cost(dosai_count, 25, 5, 2, needs_parcel, needs_chutney)
    total_amount += item_cost
    print(f"The Total cost for {dosai_count} Dosai is: {item_cost} Rupees\n")

def pongal():
    global total_amount
    print("Price of one set of Pongal is 30 Rupees")
    pongal_count = int(input("How many sets of Pongal do you need: "))
    needs_chutney = input("Do you need Coconut Chutney/Sambar? (Yes/No): ").lower() == "yes"
    needs_parcel = input("Do you need a parcel? (Yes/No): ").lower() == "yes"
    
    item_cost = calculate_total_cost(pongal_count, 30, 5, 3, needs_parcel, needs_chutney)
    total_amount += item_cost
    print(f"The Total cost for {pongal_count} sets of Pongal is: {item_cost} Rupees\n")

def poori():
    global total_amount
    print("Price of two Pooris is 25 Rupees")
    poori_sets = int(input("How many sets of Pooris do you need (1 set = 2 Pooris): "))
    needs_chutney = input("Do you need Sambar/Masala? (Yes/No): ").lower() == "yes"
    needs_parcel = input("Do you need a parcel? (Yes/No): ").lower() == "yes"
    
    item_cost = calculate_total_cost(poori_sets, 25, 5, 2, needs_parcel, needs_chutney)
    total_amount += item_cost
    print(f"The Total cost for {poori_sets * 2} Pooris is: {item_cost} Rupees\n")

def veg_biriyani():
    global total_amount
    print("Price of Veg Biriyani is 100 Rupees")
    count = int(input("How many packs of Veg Biriyani do you need: "))
    needs_parcel = input("Do you need a parcel? (Yes/No): ").lower() == "yes"
    
    item_cost = calculate_total_cost(count, 100, 5, 0, needs_parcel, False)
    total_amount += item_cost
    print(f"The Total cost for {count} Veg Biriyani is: {item_cost} Rupees\n")

def chicken_biriyani():
    global total_amount
    print("Price of Chicken Biriyani is 150 Rupees")
    count = int(input("How many packs of Chicken Biriyani do you need: "))
    needs_parcel = input("Do you need a parcel? (Yes/No): ").lower() == "yes"
    
    item_cost = calculate_total_cost(count, 150, 5, 0, needs_parcel, False)
    total_amount += item_cost
    print(f"The Total cost for {count} Chicken Biriyani is: {item_cost} Rupees\n")

def mutton_biriyani():
    global total_amount
    print("Price of Mutton Biriyani is 200 Rupees")
    count = int(input("How many packs of Mutton Biriyani do you need: "))
    needs_parcel = input("Do you need a parcel? (Yes/No): ").lower() == "yes"
    
    item_cost = calculate_total_cost(count, 200, 5, 0, needs_parcel, False)
    total_amount += item_cost
    print(f"The Total cost for {count} Mutton Biriyani is: {item_cost} Rupees\n")

def breakfast():
    while True:
        print("\nBreakfast Menu:")
        print("1. Idly\n2. Dosai\n3. Pongal\n4. Poori\n5. Return to Main Menu")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            idly()
        elif choice == 2:
            dosai()
        elif choice == 3:
            pongal()
        elif choice == 4:
            poori()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")

def lunch():
    while True:
        print("\nLunch Menu:")
        print("1. Veg Biriyani\n2. Chicken Biriyani\n3. Mutton Biriyani\n4. Return to Main Menu")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            veg_biriyani()
        elif choice == 2:
            chicken_biriyani()
        elif choice == 3:
            mutton_biriyani()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please try again.")

def main():
    global total_amount
    while True:
        print("\nWelcome to Online Food Corner!")
        print("1. Breakfast\n2. Lunch\n3. View Total and Exit")
        option = int(input("Enter your choice: "))
        
        if option == 1:
            breakfast()
        elif option == 2:
            lunch()
        elif option == 3:
            print(f"The overall total amount to be paid is: {total_amount} Rupees")
            print("Thank you for visiting! Have a nice day!")
            break
        else:
            print("Invalid choice! Please try again.")

main()
