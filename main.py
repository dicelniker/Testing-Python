# Function for the starting point of the story
def start():
    print("Start of the story.")  # Placeholder for story introduction
    print("This is where you describe the context of the adventure.")
    decision_point_1()

# Function for the first decision point
def decision_point_1():
    print("\nYou are at a decision point.")  # Placeholder for the decision description
    print("1. Route 1.")  # Placeholder for option 1
    print("2. Route 2.")  # Placeholder for option 2
    print("3. Route 3.")  # Placeholder for option 3

    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        route_1()  # Call function for route 1
    elif choice == "2":
        route_2()  # Call function for route 2
    elif choice == "3":
        route_3()  # Call function for route 3
    else:
        print("Invalid choice. Please try again.")
        decision_point_1()

# Function for route 1
def route_1():
    print("You chose route 1.")  # Placeholder for route 1 description
    print("1. Sub-route 1.")  # Placeholder for sub-route 1
    print("2. Sub-route 2.")  # Placeholder for sub-route 2

    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("Outcome 1 for route 1.")  # Placeholder for outcome 1
    elif choice == "2":
        print("Outcome 2 for route 1.")  # Placeholder for outcome 2
        decision_point_1()  # Returns to decision point 1
    else:
        print("Invalid choice. Please try again.")
        route_1()


# Start the story
start()
