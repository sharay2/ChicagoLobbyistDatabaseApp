# Stephen Harayo, 675165774, sharay2
# CS 341
# Project 2 – Chicago Lobbyist Database App
# This project is meant to find information on certain lobbyists from a database,
# and inserts new registration years and new salutation for lobbyists
import sqlite3
import objecttier

##################################################################  
#
# command1 - finds information of the lobbyists related to the given name
#
def command1(dbConn):
    user = input("\nEnter lobbyist name (first or last, wildcards _ and % supported): ")
    results = objecttier.get_lobbyists(dbConn, user)

    print("\nNumber of lobbyists found:", len(results))

    # checking number of results
    if len(results) == 0:
        return
    elif len(results) > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...")
        return
    # print each lobbyist's information
    for row in results:
        print(row.Lobbyist_ID, ":", row.First_Name, row.Last_Name, "Phone:", row.Phone)
    print()

##################################################################  
#
# command2 - finds information of one specific lobbyist related to the given name
#
def command2(dbConn):
    user = input("\nEnter Lobbyist ID:")
    print()

    result = objecttier.get_lobbyist_details(dbConn, user)
    # check if lobbyist exists
    if not result:
        print("No lobbyist with that ID was found.")
        return
    # printing all information on specific lobbyist
    print(user, ":")
    print("  Full Name:",result.Salutation, result.First_Name, result.Middle_Initial, result.Last_Name, result.Suffix)
    print("  Address:", result.Address_1, result.Address_2,",", result.City,",", result.State_Initial, result.Zip_Code, result.Country)
    print("  Email:", result.Email)
    print("  Phone:", result.Phone)
    print("  Fax:", result.Fax)

    print("  Years Registered:", end=" ")
    for year in result.Years_Registered:
        print(year, end=", ")
    print()

    print("  Employers:", end=" ")
    for employer in result.Employers:
        print(employer, end=", ")
    print()

    print(f"  Total Compensation: ${result.Total_Compensation:,.2f}")
    print()

##################################################################  
#
# command3 - finds information on the top N lobbyists during a specific year
#
def command3(dbConn):
    n = int(input("\nEnter the value of N: "))
    # checks if N is negative
    if n < 1:
        print("Please enter a positive value for N...\n")
        return

    year = input("Enter the year: ")
    print()

    results = objecttier.get_top_N_lobbyists(dbConn, n, year)
    num = 1
    # prints the top lobbyist's info
    for row in results:
        print(num, ".", row.First_Name, row.Last_Name)
        print("  Phone:", row.Phone)
        print(f"  Total Compensation: ${row.Total_Compensation:,.2f}")
        print("  Clients:", end=" ")
        for client in row.Clients:
            print(client, end=", ")
        print()
        num+=1

    print()

##################################################################  
#
# command4 - finds a specific lobbyist and registers them for a new year
#
def command4(dbConn):
    year = input("\nEnter year: ")
    id = input("Enter the lobbyist ID: ")

    result = objecttier.add_lobbyist_year(dbConn,id,year)
    # checks if lobbyist exists and info was added to the database
    if result != 1:
        print("\nNo lobbyist with that ID was found.\n")
        return
    
    print("\nLobbyist successfully registered.\n")

##################################################################  
#
# command5 - finds a specific lobbyist and changes their salutation
#
def command5(dbConn):
    id = input("\nEnter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")
    print()

    result = objecttier.set_salutation(dbConn,id,salutation)
    # checks if lobbyist exists and info was added to the database
    if result != 1:
        print("\nNo lobbyist with that ID was found.\n")
        return
    
    print("\nSalutation successfully set.\n")

##################################################################  
#
# main
#
dbConn = sqlite3.connect("Chicago_Lobbyists.db")
print('** Welcome to the Chicago Lobbyist Database Application **')

# gathering data on database
numLobbyists = objecttier.num_lobbyists(dbConn)
numEmployers = objecttier.num_employers(dbConn)
numClients = objecttier.num_clients(dbConn)

print("General Statistics: ")
print(f"  Number of Lobbyists: {numLobbyists:,}")
print(f"  Number of Employers: {numEmployers:,}")
print(f"  Number of Clients: {numClients:,}")
print()

while True:
    x = input("Please enter a command (1-5, x to exit): ")
    if x == "1":
        command1(dbConn)
    elif x == "2":
        command2(dbConn)
    elif x == "3":
        command3(dbConn)
    elif x == "4":
        command4(dbConn)
    elif x == "5":
        command5(dbConn)
    elif x == "x":
        break
    else:
        print("**Error, unknown command, try again...")


#
# done
#
