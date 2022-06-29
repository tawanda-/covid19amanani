import React, { useEffect, useState } from "react";
import "./Dashboard.css";
import Table from "../components/Table";

function Dashboard() {
  const [dataset, setdataset] = useState([]);
  const [headings, setHeadings] = useState([]);

  useEffect(() => {
    const url = "http://localhost:5000/country";

    const fetchData = async () => {
      try {
        const response = await fetch(url);
        const capitaJson = await response.json();
        setHeadings(Object.keys(capitaJson[0]))
        setdataset(capitaJson)
      } catch (error) {
        console.log("error", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col-md-1"></div>
        <main className="col-md-10">
          <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
            <h1 className="h2">Dashboard</h1>
          </div>
          <Table headings={headings} dataset={dataset} />
        </main>
        <div className="col-md-1"></div>
      </div>
    </div>
  );
}

export default Dashboard;
