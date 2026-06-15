readings = []
try:
    read_file = open("04/air_quality.txt", "r")
    air_quality_data = read_file.readlines()

    for i, data in enumerate(air_quality_data, start=1):
        try:
            readings.append(float(data.strip()))
        except ValueError:
            print(f"Invalid data found in line {i}: {data.strip()}")
            continue

        print(f"Reading {i:<5}: {data.strip()} µg/m³")

    average = sum(readings) / len(readings)
    print(f"\nTotal Readings     : {len(readings)}")
    print(f"Average Air Quality: {average:.2f} µg/m³")

    if average > 100:
        print("Air quality is poor. Consider taking precautions.")
    elif average > 50:
        print("Air quality is moderate. Be cautious if you have respiratory issues.")
    else:
        print("Air quality is good. Enjoy your day!")

except FileNotFoundError:
    print("The file could not be found.")
