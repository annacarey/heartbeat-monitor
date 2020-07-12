import React, { useState, useEffect } from 'react';
  
function Dashboard(props) {
    // Update if using a new server
    const serverAddress = 'http://127.0.0.1:5000'

    // Declare state variables to store heartrate readings
    const [heartrateReadings, setHeartrateReadings] = useState([]);
    const [firstName, setFirstName] = useState(['']);

    // Fetch request to Flask API to get the current user's heartrate readings
    const getUserHeartrate = () => {
        fetch(`${serverAddress}/get_heartrate_readings/${parseInt(props.userid)}`).then(res => res.json()).then(data => {
            setHeartrateReadings(data.heartrates)
            setFirstName(data.user.first_name)
          })
    }

    useEffect(() => {
        // Get user's heartrate data on initial render
        getUserHeartrate()

        // On every five second interval, get the heartrate data and component rerenders
        const interval = setInterval(() => {
            getUserHeartrate()
          }, 5000);
          return () => clearInterval(interval);
        
      }, []);

    return (
    <div id= "dashboard">
        <h2>Welcome, {firstName}</h2>
        <h3>Current Heartrate:</h3>
        <h3>Heartrates History: </h3>
        <table>
            <tr>
              <th>Date</th>
              <th>BPM</th>
            </tr>
        {heartrateReadings.map(heartrateReading => 
            <tr>
                <td>{heartrateReading.created}</td>
                <td>{heartrateReading.bpm}</td> 
            </tr>
        )}
        </table>
    </div>
    )
}

export default Dashboard