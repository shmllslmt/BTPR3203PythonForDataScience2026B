category_totals = {}
donors = []

try:
    donation_file = open("04/donations.csv", "r")
    donation_data = donation_file.readlines()

    del donation_data[0]  # Remove header

    for i, data in enumerate(donation_data, start=1):
        try:
            donor_name, amount, category = data.strip().split(",")
            amount = float(amount)
            donors.append((donor_name))

            if category in category_totals.keys():
                category_totals[category] += amount
            else:
                category_totals[category] = amount

            print(f"{donor_name:<20} RM{amount:.2f}\t{category}")
        except ValueError:
            print(f"Invalid data found in line {i}: {data.strip()}")
            continue
    
    print("\n" + "="*45)
    print("CATEGORY BREAKDOWN")
    print("="*45)

    for category, total in category_totals.items():
        print(f"{category:<20} RM{total:.2f}")

    print("-"*45)
    print(f"Total donations: RM{sum(category_totals.values()):.2f}")
    print(f"Total donors: {len(donors)}")

except FileNotFoundError:
    print("The file could not be found.")