try:
    found_file = open("04/found_file.txt", "a")

    while True:
        found_item = input("Enter an item you found (or 'done' to finish): ")

        if found_item.lower() == 'done':
            break

        found_file.write(found_item+"\n")

    found_file.close()

    print("="*45)
    print("LOST AND FOUND ITEMS")
    print("="*45)

    read_file = open("04/found_file.txt", "r")
    read_items = read_file.readlines()

    for item in read_items:
        print(item.strip())

    print(f"Total items found: {len(read_items)}")
    read_file.close()

except FileNotFoundError:
    print("The file could not be found.")