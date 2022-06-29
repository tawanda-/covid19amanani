import React, {useEffect, useState} from "react";
import { Chart } from "react-google-charts";

export const options = {
    region: "002", // Africa
    colorAxis: { colors: ["#00853f", "black", "#e31b23"] },
    backgroundColor: "#81d4fa",
    datalessRegionColor: "#f8bbd0",
    defaultColor: "#f5f5f5",
  };

  export const selectOptions = [
    {value: '', text: 'Select Dataset'},
    {value: 'vaccinated', text: 'Vaccinated'},
    {value: 'confirmed', text: 'Infected'},
    {value: 'deaths', text: 'Deaths'},
  ];

  export const titleOptions = {
    'vaccinated':'Vaccinated per capita',
    'confirmed':'Infected per capita',
    'deaths':'Deaths per capita'
  }

function Capita(){
    const [data, setData] = useState({})
    const [title, setTitle] = useState('')
    const [dataset, setDataset] = useState({})
    const [selected, setSelected] = useState(selectOptions[1].value)

    const handleChange = event => {
        console.log(data[event.target.value])
        setDataset(data[event.target.value])
        setTitle(titleOptions[event.target.value])
        setSelected(event.target.value)
    };

    useEffect(() => {
        const url = "http://localhost:5000/country/all/percapita";

        const fetchData = async () => {
            try {
                const response = await fetch(url);
                const capitaJson = await response.json();
                setData(capitaJson)
                setDataset(capitaJson[selectOptions[1].value])
                setTitle(titleOptions[selectOptions[1].value])
            } catch (error) {
                console.log("error", error);
            }
        };

        fetchData();
      }, []);

      return(
        <div className="container">
            <div className="row align-items-start">
                <div class="col-3">
                    <select class="form-select form-select-lg" value={selected} onChange={handleChange}>
                        {selectOptions.map(option => (
                        <option key={option.value} value={option.value}>
                            {option.text}
                        </option>
                        ))}
                    </select>
                </div>
                <div class="col-6">
                    <h5>{title}</h5>
                    <Chart
                        chartType="GeoChart"
                        width="100%"
                        height="400px"
                        data={dataset}
                        options={options}
                    />
                </div>
                <div class="col-3"></div>
            </div>
        </div>
      );

}

export default Capita; 