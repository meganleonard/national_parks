import sqlite3
import requests

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('national_parks.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS national_parks')

# Create the national_parks table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS national_parks (
                    id INTEGER PRIMARY KEY,
                    fullName TEXT,
                    description TEXT,
                    latitude REAL,
                    longitude REAL,
                    states TEXT,
                    activities TEXT,  -- Add activities field as a TEXT column
                    directionsInfo TEXT,
                    operatingHours TEXT,
                    name TEXT,
                    designation TEXT
                )''')

# Commit changes to the table schema
conn.commit()

# Define API endpoint
endpoint = "https://developer.nps.gov/api/v1/parks?"

# Define parameters for API request
parameters = {
    "api_key": "wvmgBqERADr7Yw8HhxgWJGhdwODa8R1FYweZK6rk", 
    "fields": "fullName,description,latitude,longitude,activities,topics,states,operatingHours,name,designation",  # Select specific fields
    "designation": "National Park"  # Filter parks by designation
}

# Make GET request to the API
response = requests.get(endpoint, params=parameters)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data_all = response.json()['data']  # Extract data from the API response
    
    # Iterate over the list of parks and insert data into the database
    for park in data_all:
        # Extract relevant attributes from the park object
        park_name = park.get('fullName', '')
        description = park.get('description', '')
        latitude = park.get('latitude', None)
        longitude = park.get('longitude', None)
        states = ', '.join(park.get('states', []))
        activities = ', '.join(activity.get('name', '') for activity in park.get('activities', []))  # Extract activity names
        designation = park.get('designation', '')

        # Insert data into the national_parks table
        cursor.execute('''INSERT INTO national_parks 
                        (fullName, description, latitude, longitude, states, activities, designation)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (park_name, description, latitude, longitude, states, activities, designation))

    # Commit changes and close connection
    conn.commit()
else:
    print(f"Error: {response.status_code}")

# Check Data
cursor.execute("SELECT * FROM national_parks")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
