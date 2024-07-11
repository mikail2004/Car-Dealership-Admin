#Authors:
#1. Mikail Usman
#2. Yusuf Yildirim
'''----------------Import Modules----------------'''
import dealer_tool as dealer

'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")

vehicles = dealer.initialize()
#This While loop will keep asking for user inputs until the they simply press enter.
while True:
    dealer.display_menu()  
    option=input("Command (Enter to exit): ")
    
    if option=="":
        break
    elif option=="1":
        dealer.display(vehicles)  #Calls a function from dealer_tool to display all vehicle information
    elif option=="2":
        dealer.info(vehicles) #Calls a function from dealer_tool to run calculations for statistics (mean, etc)
    elif option=="3":
        index = input("Which vehicle do you want to remove (enter number):")
        #Checks if the index inputted by the user is an acceptable value and then uses it as an index for the vehicles list to find and delete the requested model
        if int(index) >= 1 and int(index) <= len(vehicles):
            del(vehicles[int(index)-1])
        else:
            print("Vehicle not found!")
    elif option == "4":
        vehicles = dealer.add_new_vehicle(vehicles)
    elif option == "5":
        index1 = input("First Vehicle (enter number): ")
        index2 = input("Second Vehicle (enter number): ")
        if (int(index1) >= 1 and int(index1) <= len(vehicles)) and int(index2) >= 1 and int(index2) <= len(vehicles):
            dealer.compare(vehicles[int(index1)], vehicles[int(index2)])
    elif option == "6":
        min = input("Please select a minimum price: ")
        max = input("Please select a maximum price: ")
        dealer.search(vehicles, min, max)
    elif option == "7":
        indexNum = int(input("Which vehicle would you like to discount? (Enter number): "))
        discount = int(input("What percent would you like to disocunt the vehicle? (0-100): "))
        if (indexNum) < 1 and (indexNum) > len(vehicles):
            print("Vehicle not found!")
        elif (discount < 1 and discount > 100):
            print("Invalid Discount!")
        else:
            newPrice = dealer.discount(vehicles[indexNum], discount)
            vehicles[indexNum][4] = str(newPrice)



# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")