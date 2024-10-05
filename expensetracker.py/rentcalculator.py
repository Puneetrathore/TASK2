def rent_calculator():
    # Step 1: Define variables
    try:
        rent_amount = float(input("Enter the monthly rent amount: "))
        utilities = float(input("Enter the average monthly utilities amount: "))
        lease_duration = int(input("Enter the lease duration in months: "))
        
        # Step 3: Calculate total cost
        total_rent = (rent_amount + utilities) * lease_duration
        
        # Step 4: Display the result
        print(f"\nTotal cost for {lease_duration} months: ${total_rent:.2f}")
    except ValueError:
        print("Please enter valid numbers.")

# Run the calculator
rent_calculator()
