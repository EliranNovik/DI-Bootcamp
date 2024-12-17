import random
import requests
import psycopg2
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# PostgreSQL connection setup
DB_HOST = "localhost"
DB_NAME = "countries_db"
DB_USER = "postgres"  # Replace with your PostgreSQL username
DB_PASSWORD = ""  # Replace with your PostgreSQL password

# REST API URL
REST_API_URL = "https://restcountries.com/v3.1/all"

# Fetch countries with retries and timeout
def fetch_countries():
    try:
        # Set up a session with retries
        session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        session.mount('https://', HTTPAdapter(max_retries=retries))

        # Fetch data from the REST Countries API
        response = session.get(REST_API_URL, timeout=30)
        response.raise_for_status()
        countries = response.json()
        print(f"Fetched {len(countries)} countries from the API.")
        return countries
    except requests.RequestException as e:
        print(f"Error fetching countries: {e}")
        return []

# Save data to PostgreSQL database
def save_to_database(country_data):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Insert country data into the table
        insert_query = """
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s);
        """
        for country in country_data:
            try:
                # Safely get data from the country JSON
                name = country.get("name", {}).get("common", "Unknown")
                capital = country.get("capital", [None])[0]  # Capital is a list in the API
                flag = country.get("flags", {}).get("png", "")
                subregion = country.get("subregion", "")
                population = country.get("population", 0)

                # Execute the insert query
                cursor.execute(insert_query, (name, capital, flag, subregion, population))
            except Exception as e:
                print(f"Error inserting country {country.get('name', {}).get('common', 'Unknown')}: {e}")
                continue  # Skip to the next country in case of errors

        conn.commit()
        print(f"{len(country_data)} countries saved to the database.")
        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Database error: {e}")

# Main function
def main():
    # Fetch data from the API
    countries = fetch_countries()

    if not countries:
        print("No countries fetched.")
        return

    # Randomly select 10 countries
    try:
        random_countries = random.sample(countries, 10)
    except ValueError as e:
        print(f"Error selecting random countries: {e}")
        return

    # Save the selected countries to the database
    save_to_database(random_countries)

if __name__ == "__main__":
    main()
