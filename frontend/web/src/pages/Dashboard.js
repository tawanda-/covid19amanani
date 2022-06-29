import React, { useEffect, useState } from "react";
import "./Dashboard.css";
import { isoOptions } from "../components/Iso";

function Dashboard() {
  const [selected, setSelected] = useState(isoOptions[0].value);

  const handleChange = (event) => {
    setSelected(event.target.value);
  };

  useEffect(() => {
    const url = "http://localhost:5000/country/all/percapita";

    const fetchData = async () => {
      try {
        const response = await fetch(url);
        const capitaJson = await response.json();
        console.log(capitaJson);
        setVaccinated(capitaJson["vaccinated"]);
        setConfirmed(capitaJson["confirmed"]);
        setDeaths(capitaJson["deaths"]);
      } catch (error) {
        console.log("error", error);
      }
    };

    //fetchData();
  }, []);

  return (
    <div class="container-fluid">
      <div class="row">
        <nav
          id="sidebarMenu"
          class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse"
        >
          <div class="position-sticky pt-3">
            <ul class="nav flex-column">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">
                  <span data-feather="home" class="align-text-bottom"></span>
                  Dashboard
                </a>
              </li>
              <li class="nav-item">
                <select
                  class="form-select"
                  value={selected}
                  onChange={handleChange}
                >
                  {isoOptions.map((k) => (
                    <option key={Object.keys(k)[0]} value={Object.keys(k)[0]}>
                      {Object.keys(k)[0]}
                    </option>
                  ))}
                </select>
              </li>
            </ul>
          </div>
        </nav>

        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
            <h1 class="h2">Dashboard</h1>
          </div>
          <canvas
            class="my-4 w-100"
            id="myChart"
            width="900"
            height="380"
          ></canvas>
        </main>
      </div>
    </div>
  );
}

export default Dashboard;
