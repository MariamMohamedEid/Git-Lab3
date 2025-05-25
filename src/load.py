import csv
import logging

logging.basicConfig(filename='logs/etl.log', level=logging.INFO)

def load(data):
    with open('./output.csv', 'w') as f:  # Create/overwrite 'output.csv'
        writer = csv.writer(f)
        writer.writerow(['City', 'Count'])  # Write header row
        
        # Write each city and its count as a row
        for city, count in data.items():
            writer.writerow([city, count])
    
    logging.info("Data saved to output.csv")