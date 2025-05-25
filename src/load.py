import csv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load(data):
    try:
        output_path = os.path.abspath("output.csv")
        logger.info(f"Attempting to write to: {output_path}")
        
        with open(output_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['City', 'Count'])
            for city, count in data.items():
                writer.writerow([city, count])
        
        logger.info("Successfully wrote output.csv")
        logger.info(f"File exists: {os.path.exists(output_path)}")
        logger.info(f"File size: {os.path.getsize(output_path)} bytes")
        
    except Exception as e:
        logger.error(f"Failed to write file: {str(e)}")
        raise