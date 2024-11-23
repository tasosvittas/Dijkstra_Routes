import csv
csv_data = []
with open('routes.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) < 5:  # Skip malformed or empty rows
            print(f"Skipping malformed row: {row}")  # Debugging
            continue
        #gia kanonikopoihsh twn from_city kai to_city row[0].strip().upper()
        from_city = row[0].strip().upper()
        to_city = row[1].strip().upper()
        travel_mode = row[2].strip()
        time = float(row[3])
        cost = float(row[4])
        csv_data.append((from_city, to_city, travel_mode, time, cost))
print(csv_data)