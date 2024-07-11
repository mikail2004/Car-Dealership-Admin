#Authors:
#1. Mikail Usman
#2. Yusuf Yildirim
'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")

#### To complete (all functions below)

def initialize():
    vehicle1 = ["Toyota", "Camry", "2018", "45000", "20000"]
    vehicle2 = ["Ford", "Escape", "2019", "30000", "23500"]
    vehicle3 = ["Honda", "Accord", "2017", "60000", "16200"]
    vehicle4 = ["Chevrolet", "Silverado", "2020", "25000", "41000"]
    vehicle5 = ["BMW", "3 Series", "2016", "60000", "20500"]
    vehicle6 = ["Nissan", "Rogue", "2019", "40000", "17800"]
    vehicle7 = ["Hyundai", "Sonata", "2018", "42000", "16500"]
    vehicle8 = ["Jeep", "Wrangler", "2021", "15000", "32000"]
    vehicle9 = ["Ford","Mustang","2015","50000","22000"]
    vehicle10 = ["Volksagen","Golf","2017","38000","17800"]
    vehicles=[vehicle1,vehicle2, vehicle3, vehicle4, vehicle5, vehicle6, vehicle7, vehicle8, vehicle9, vehicle10] #Creates a 2D list with all vehicles as rows
    return vehicles

def display(vehicles):
    #Displays vehicle info with a special format using a for loop and \t
    print("\t" + "Make" + "\t" + "Model" + "\t" + "Year" + "\t" + "Mileage" + "\t" + "Price ($)")
    print("---------------------------------------------------")
    for i in range(len(vehicles)):
        print(str(i+1) + "\t" + vehicles[i][0] + "\t" + vehicles[i][1] + "\t" + vehicles[i][2] + "\t" + vehicles[i][3] + "\t" + vehicles[i][4])

def info(vehicles):
    #Iterates through the vehicle list, to create a new list that stores vehicle prices -> To be used for calculations
    priceList = []
    sum = 0
    count = 0
    tier1 = 0
    tier2 = 0
    tier3 = 0
    tier4 = 0
    tier5 = 0
    for i in range(len(vehicles)):
        price = int(vehicles[i][4])
        priceList += [price]
        sum += price
        count += 1
        if price < 10000:
            tier1 += 1
        elif price >= 10000 and price < 20000:
            tier2 += 1
        elif price >= 20000 and price < 30000:
            tier3 += 1
        elif price >= 30000 and price < 40000:
            tier4 += 1
        elif price >= 40000:
            tier5 += 1
    mean = sum/count
    print("#Vehicles "+ str(len(priceList)))
    #Each vehicle ratio is known a tier, to rank by price.
    print("<10,000: "+ str(tier1/count*100)+"%")
    print("10,000s: "+ str(tier2/count*100)+"%")
    print("20,000s: "+ str(tier3/count*100)+"%")
    print("30,000s: "+ str(tier4/count*100)+"%")
    print(">=40,000: "+ str(tier5/count*100)+"%")
    print()
    print("Mean Price: "+str(mean))

def add_new_vehicle(vehicles):
    #Takes all attributes of a vehicle as input and then creates a new list to create a row, which is then added to the original list (vehicles)
    make = input("Enter Make: ")
    model = input("Enter Model: ")
    year = input("Enter Year: ")
    mileage = input("Enter Mileage: ")
    price = input("Enter Price: ")
    newVehicle = [make, model, year, mileage, price]
    vehicles += [newVehicle]
    return vehicles

def compare(vehicle1, vehicle2):
    #Compares make, prices and year of the vehicles provided using their index values relative to their position in the original vehicles list
    print(vehicle1[0] + " " + vehicle1[1] + " vs " + vehicle2[0] + " " + vehicle2[1])
    if vehicle1[0] == vehicle2[0]:
        print("The two vehicles are the same make.")
    elif vehicle1[0] != vehicle2[0]:
        print("The two vehicles are different makes.")
    if int(vehicle1[2]) == int(vehicle2[2]):
        print("The two vehicles were made the same year.")
    elif int(vehicle1[2]) > int(vehicle2[2]):
        print("The first vehicle is newer.")
    elif int(vehicle1[2]) < int(vehicle2[2]):
        print("The second vehicle is newer.")
    if int(vehicle1[4]) == int(vehicle2[4]):
        print("The two vehicles cost the same.")
    elif int(vehicle1[4]) > int(vehicle2[4]):
        print("The first vehicle costs more.")
    elif int(vehicle1[4]) < int(vehicle2[4]):
        print("The second vehicle costs more.")

def search(vehicles, min, max):
    #Searches though the vehicles list using a conditional statement that looks between min and max range.
    count = 0
    print(f"Vehicles that cost between {min} and {max}:")
    for i in range(len(vehicles)):
        if int(vehicles[i][4]) >= int(min) and int(vehicles[i][4]) <= int(max):
            print(vehicles[i][0] + " " + vehicles[i][1] + " " + vehicles[i][4])
            count+=1
    print("Total number of vehicles: "+str(count))

def discount(vehicle, price):
    #Calculates the discount, and then sets it to the price attribute of the vehicle by updating the main vehicle list
    discount = int(vehicle[4])*(price/100)
    newPrice = int(vehicle[4])-discount
    print("Vehicle: "+vehicle[0]+" "+vehicle[1])
    print("Price: "+vehicle[4])
    print("Discount: "+str(discount))
    print("New Price: "+str(newPrice))
    return newPrice