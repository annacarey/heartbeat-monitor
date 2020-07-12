import React, { useState, useEffect } from 'react';
  
function Dashboard() {

    // Update if using a new server
    const serverAddress = 'http://127.0.0.1:5000'

    // Declare state variables to store heartrate readings
    const [heartrateReadings, setHeartrateReadings] = useState([]);

    useEffect(() => {
        fetch(`${serverAddress}/get_heartrate_readings/2`).then(res => res.json()).then(data => {
            console.log(data.heartrates)
            setHeartrateReadings(data.heartrates)
          });
      }, []);

    return (
    <div id= "dashboard">
        <h2>Welcome, Anna</h2>
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