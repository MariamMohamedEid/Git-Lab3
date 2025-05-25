import logging

logging.basicConfig(filename='logs/etl.log', level=logging.INFO)

def transform(data):
    try:
        # Extract cities from nested 'address' field
        cities = [user['address']['city'] for user in data]
        
        # Count users per city (e.g., {"Paris": 5})
        city_counts = {city: cities.count(city) for city in set(cities)}
        
        logging.info("Data transformed successfully")
        return city_counts  # Return aggregated data

    except KeyError as e:
        logging.error(f"Transformation error: {e}")
        raise  # Re-raise exception to fail the workflow