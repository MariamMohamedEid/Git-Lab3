import requests
import logging

logging.basicConfig(filename='logs/etl.log', level=logging.INFO)

def extract():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info("Data extracted successfully")
        return response.json()
    else:
        logging.error(f"API failed with status code {response.status_code}")
        raise Exception("API request failed")