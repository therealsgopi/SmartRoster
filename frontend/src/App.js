import './App.css';
import { useState, useEffect } from 'react';
import axios from 'axios'
import { ExportToCsv } from 'export-to-csv';

function App() {

  const options = { 
    filename: "attendance_report.csv",
    fieldSeparator: ',',
    quoteStrings: '"',
    decimalSeparator: '.',
    showLabels: true, 
    showTitle: false,
    useTextFile: false,
    useBom: true,
    // useKeysAsHeaders: true,
    headers: ['Register Number', 'Status'] // <-- Won't work with useKeysAsHeaders present!
  };

  const csvExporter = new ExportToCsv(options);

  const [image, setImage] = useState([]);
  const [attendanceData, setAttendanceData] = useState({"regno": [], "status": []})

  // useEffect(() => {
  //   const fetchParseData = async () => {
  //     Papa.parse(marked_attendance, {
  //       download: true,
  //       delimiter: ",",
  //       complete: ((result) => {
  //         setAttendanceData(result.data)
  //       })
  //     })
  //   }
  //   fetchParseData()
  // }, [])

  useEffect(() => {
    console.log("image updated")
  }, [image])
  

  const generateCSV = () => {
    if(attendanceData['regno'].length === 0) {
      alert("Add class image to generate index report!")
    } else {
      var csvFormattedData = []
      for(var index = 0; index<attendanceData['regno'].length; index++) {
        csvFormattedData.push([attendanceData['regno'][index], attendanceData['status'][index]])
      }
      // console.log(csvFormattedData)
      csvExporter.generateCsv(csvFormattedData);
  }
  }
  

  function handleImport(e) {
    setImage([URL.createObjectURL(e.target.files[0])]);
}

const sendData = async(e) => {
  e.preventDefault();
  axios.post("http://127.0.0.1:8000/mark-attendance", 
  image, {
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json;charset=UTF-8",
  },
    })
    .then(({data}) => {
      setAttendanceData({"regno": data["regno"], "status": data["status"]});
  });
}

  return (
    <div className="App">
      <div id="VIT_logo">
        <img
            src={require("./Assets/VIT_logo.png")}
            alt="VIT-logo"
            id="VIT-Logo"
                  />
      </div>
      <div className='attendance-controls'>
        <div className='controls'>
          <input id="control-button" type="file" onChange={handleImport} />
          <button id="control-button" onClick={(e) => {sendData(e);}}>Upload</button>
          <button id="control-button" onClick={() => {setImage([]); setAttendanceData({"regno": [], "status": []})}}>Clear</button>
          <button id="control-button" onClick={() => {generateCSV()}}>Download attendance</button>
        </div>
      </div>
      {image.length !== 0 ? <img src={image} id="image" alt="classroom"/> : <span></span>}
      {attendanceData["regno"].length !== 0 ? 
        <table id="attendance_table">
          <tr>
            <th>Regsister Number</th>
            <th>Status</th>
          </tr>
          {attendanceData["regno"].map((record, index) => (
            <tr id = {index}>
              <td>{record}</td>
              <td>{attendanceData["status"][index]}</td>
            </tr>
          ))}
        </table>
        :
        <span></span>
        }
    </div>
  );
}

export default App;
