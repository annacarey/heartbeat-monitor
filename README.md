# Heartrate Monitoring App with "Sensor" Simulation

## Goal
Goal was to build a web application that displays the latest "heartbeats" from a number of sensors using Flask.

## Instructions
1. Fork and clone the repository
2. Cd into the app directory and run python init_db.py to initialize database and seed data
4. If you need to make changes to anything in the React frontend, cd into static directory and run npm build to update the bundle.js file
5. Cd .. and run python -m flask run to startup your application server
6. Update the server endpoint in the Dashboard.js and sensor.py file according to what your server address is
7. In another terminal window run python sensor.py sensor_name according to what sensor you want to use from your init_db.py file

## Setup

### Database
* My SQLite tables are: users, sensors, and heartrate_readings
* heartrate_readings has a one to many relationship with both users and sensors (so each heartrate_reading has user_id and sensor_id foreign keys)
* Notes on the sensor model:
    * The sensor model has an 'active' attribute that is a boolean. Currently, I am not using this attribute, but the idea is that if my program was connected to real sensors, I could set the attribute to "false" if the program hadn't received a response in a particular amount of time
* Notes on the user model:
    * Creating a user model wasn't necessary to achieve my goal
    * I did not implement signup or login functionality yet and just have the home.html template as a pageholder for when I do implement them. I would need to username/password to my schema.
    * Currently, you can seed new users in the init_db.py file and access the user's dashboard info by going to the '/<int> user_id' route

### Simulating a Sensor
* In order to show my program was connected to a sensor, I decided to simulate a sensor by creating a separate Python program that serves as its own sensor "server"
* I seeded three sensors in my database
* When I run the file in my terminal with a command line argument of the server's name, I am simulating a new reading on the specified sensor
* The sensor 'server' in the sensor.py file takes in the sensor's name and then makes a POST request to my Flask server. The request includes bpm, user_id, and the sensor's name. For now, you can set the bpm manually, but eventually that would be actual sensor data. The user's id is also currently just updated manually
* Other considerations:
    * I started to look into websockets for this project, but since I was new to Python/Flask, I chose to use the command line approach to indicate a reading
    * I also considered looking into libraries that can connect to Arduino and/or RasberryPi sensor data such as the serial library

### Flask Setup
* Basic setup for a Flask app with one main Python file, a database, seed file, and three templates
* My client endpoints in Flask are '/' and '/<int:user_id>'
    * '/' is the dummy homepage with a login/signup form that is not yet implemented
    * '/<int:user_id>' is the user's dashboard that renders the Dashboard React component. More on that later
* Other important routes:
    * '/heartrate', a POST route that allows my sensors to post a reading to the database
    * '/get_heartrate_readings/<int:user_id>' is used by the frontend to get the user's heartrate readings

### React Setup
* I chose to use React for my frontend so that I could more easily extend my application's frontend and because it was easier for me to make fetch requests on an interval
* The Dashboard template connects to a very small React application via a script that is created with Webpack and Babel. 
* One important note is that I am passing the user's id down as a props to the root component in index.js which is then passed to the Dashboard component. I needed the user id for my fetch request. I'm interested in thinking through alternatives to make sure the Dashboard component knows about which user's page is currently loading
* If I extended the frontend, I would connect the React component to the base template
* The Dashboard component uses hooks to set the first name of the current user and their heartrate readings. I used the useEffect method to make an initial fetch to the Flask server for the user's heartrate info and then set an interval for every five seconds to check the server for an updated reading
* There is a lot of ways I could have shown updated heartrate readings on the client side including web sockets as mentioned above. I could have had the client communicate directly with a sensor. Instead, I chose to have the server communicate with the sensor to both store the sensor data in the database and render the updated data on the frontend with at most a five second delay


### Testing
* In the tests folder, there is an initial setup with pytest to create an instance of my app. I am new to testing and this is my highest priority of new skills to learn, but because I was new to Flask/Python, I decided to leave the testing for a later extension.
* In an ideal world, I would set up unit tests for each of my database models to make sure my database is set up properly, for each of my methods in my app.py file, and for my React component as well.
* Currently there is a testing route in my app.py to show some of my initial testing process to make sure my database was working properly

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
If you want to contact me, you can reach out at anna@annajcarey.com.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


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