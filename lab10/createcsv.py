import csv

# Sample data
data = [
    ("John", "Doe", "1234567890"),
    ("Jane", "Smith", "0987654321"),
    ("Alice", "Johnson", "5555555555"),
    ("Asylniet", "Zh", "1234567890"),
    ("J", "Smith", "0987654321"),
    ("A", "Johnson", "5555555555"),
    ("A", "bbbbbbn", "5555555555")
]

# File path to save the CSV file
filename = "data.csv"

# Writing data to the CSV file
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["First Name", "Last Name", "Phone Number"])  # Writing header
    writer.writerows(data)  # Writing rows of data

print("CSV file created successfully:", filename)
