# Density Fullstack Homework Assignment

## Goal
Your goal is to build a web application that displays the latest "heartbeat" from a number of sensors.

## Assignment
Your task is to accomplish the following:
- Use Flask (or some similar Python web framework) to build a web application
- Scaffold a database that includes sensors and heartbeats
- Expose an endpoint that can receive "heartbeats" indicating that the sensor is alive and checking in
- Deliver a webpage where a user can view live, updating heartbeats from the sensors


Notes:
    # tutorial: https://pythonforundergradengineers.com/flask-iot-server-web-API.html

    # Success 
    # record heartrate
    # one is to generate heartrates from number of sensors
    # display the latest heartbeats
    # HTTP is closed request - client just talking to server
    # Set interval, update button
    # Web sockets - real time updates from a client -- two way exchange -server can start conversation
    # socket.io
    # return an array of objects with an id of sensor id
    # latest heartrate value

    # dont need user model
    # seed four or five sensors in database
    # spin up another application in pure python for the sensor - one file python function
    # to be able to go to run a sensor script sensor.py that takes in the id to initailize it with (pass it in in the script)
    # inside sensor python file should just know address of where file is running -- will connect to server -- hit route on flask app on regular intervals
    # flask app receives data
    # send a fake user id with it 
    # if it's been longer since the sensor has been received
    # polling to check that number again
    # design 

#     # set interval for timing to check sensor
#     # set variables equal to the response from the sensor
#     # if the variables are both not none,
#     payload = {
#         'sensor_id': sensor_id,
#         'bpm': bpm,
#         'timestamp': timestamp
#     }
#     # use requests library to set the requests object to the post address
#     # use the reuqests library to send the payload