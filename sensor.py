import sys
import requests

# Endpoint base. Change based on where server is running
server_address = 'http://127.0.0.1:5000/heartrate'

# Set sensor name to command line argument
sensor_name = sys.argv[1]

# Set user name to dummy user
user_id = 2

# Set bpm to value from sensor (dummy data for now)
bpm = 50

# Add variables to a payload
payload = {'bpm': bpm, 'sensor_name': sensor_name, 'user_id': user_id}

# Send a post request to 
r = requests.post(server_address, json = payload)
print (r.text)