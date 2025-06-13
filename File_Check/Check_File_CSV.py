import csv as c

# Initialize the find list
find = []

# Read from "Files to look for.csv" and populate the find list
with open("Files to look for.csv", mode='r', newline='') as looking:
    reader = c.reader(looking)
    header = next(reader)  # Skip the header
    for row in reader:
        if row:  # Ensure row is not empty
            find.append(row[0].strip())

# Define the header for the output file
output_header = ["File", "Research"]

# Track which files have been processed
processed_files = set()

# Write to "Research.csv"
with open('Research.csv', mode='w', newline='') as outfile:
    writer = c.writer(outfile)
    writer.writerow(output_header)

    # Read from "File data.csv" and write filtered data to "Research.csv"
    with open("File data.csv", mode='r', newline='') as datafile:
        data_reader = c.reader(datafile)
        data_header = next(data_reader)  # Skip the header
        
        for row in data_reader:
            if not row:  # Ensure row is not empty
                continue

            # Strip whitespace and check conditions
            file_id = row[0].strip()
            status = row[1].strip()

            if file_id in find:
                # Check conditions and write appropriate messages to the output file
                if status == "In":
                    writer.writerow([
                        file_id,
                        f"This file was checked in by {row[3]} on {row[2]}"
                    ])
                elif status == "Perm out":
                    writer.writerow([
                        file_id,
                        f"This file was Permed out by {row[3]} on {row[2]}"
                    ])
                elif status == "Checked out":
                    writer.writerow([
                        file_id,
                        f"This file was checked out to {row[4]} by {row[3]} on {row[2]}"
                    ])
                elif status == "Destroyed":
                    writer.writerow([
                        file_id,
                        f"This file was Destroyed by {row[3]} on {row[2]}"
                    ])
                
                processed_files.add(file_id)

# Handle files that were not found
for f in find:
    if f not in processed_files:
        with open('Research.csv', mode='a', newline='') as outfile:
            writer = c.writer(outfile)
            writer.writerow([
                f,
                "This file was not found"
            ])
