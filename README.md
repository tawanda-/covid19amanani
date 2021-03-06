<p align="center">
	<img src="https://github.com/tawanda-/covid19amanani/blob/master/frontend/web/src/logo.png" alt="logo" width=30%/>
	<h2 align="center">Covid 19 Amanani</h2>
</p>

<p align="center">
	<img src="https://img.shields.io/badge/python-v3.10.5-yellow.svg" alt="python" />
	<img src="https://img.shields.io/badge/react-v18.2.0-blue.svg" alt="react" />
	<img src="https://img.shields.io/badge/flask-v2.1.3-green" alt="flask" />
	<img src="https://img.shields.io/badge/PostgreSQL-v14.2-red.svg" alt="react" />
</p>

<p align="center">
	<a href="#description">Description</a> •
	<a href="#tech">Tech</a> •
	<a href="#installation">Installation</a> •
	<a href="#license">License</a> •
</p>

<hr>

## Description

Amanani is an isiXhosa word when translated to English means numbers. IsiXhosa is one of the official languages of South Africa. So the literal transalation of Covid-19 amanani is Covid-19 numbers.

## Tech

### Data API

[COVID-19-API](https://github.com/M-Media-Group/Covid-19-API) provides the covid 19 data.

### Stack

[![](https://mermaid.ink/img/pako:eNpVz80KwjAMB_BXCTlvL7CDsC_Bm7iBh9VDXOMcbu1os4MM393OiWBO4Z8fIVmwtZoxwc7RdIe6UAZCpc3eWSOl0QmcmFqBM1-BpukCcbzLNpQ1GbUPXs1-IP-AU1nVkB4PH5RvKG-O1kvn2ENBQlfy_Ldj7VOMcGQ3Uq_DJcs6USh3HllhElrNN5oHUajMK9B50iRc6l6sw-RGg-cIaRZbPU37CzZV9BQ-G7_p6w00nEu5)](https://mermaid.live/edit#pako:eNpVz80KwjAMB_BXCTlvL7CDsC_Bm7iBh9VDXOMcbu1os4MM393OiWBO4Z8fIVmwtZoxwc7RdIe6UAZCpc3eWSOl0QmcmFqBM1-BpukCcbzLNpQ1GbUPXs1-IP-AU1nVkB4PH5RvKG-O1kvn2ENBQlfy_Ldj7VOMcGQ3Uq_DJcs6USh3HllhElrNN5oHUajMK9B50iRc6l6sw-RGg-cIaRZbPU37CzZV9BQ-G7_p6w00nEu5)

### Design Philosophy

The MVC pattern was used in designing the flask application. Which is essentially a simple REST server providing an interface for clients to get data

The main actors involved in handling client requests are:
 - Blueprint acts as controller, liasing with other actors to ensure client request is processed.
 - Data access objects(DAO), sits between the database and blueprint/controller, main responsibility is to query data from database annd send response to    controller. The dao also interacts with model classes.

## Installation

### Using Docker:

In terminal run the following command:

    docker-compose up
    
To access the website go to: http://localhost:5000

### Manual Installation:

#### Backend

##### Python requirements

Python > 3.10

Postgres server

##### Flask Setup

In the root folder run the following commands:
1. Create a virtual environment:

    ````
    python3 venv venv
    ````
    
  - Initialise the virtual environment:
    
    ````
    . venv/bin/activate
    ````

2. Install dependencies:

    ````
    pip install -r /backend/api/requirements.txt
    ````
    
3. Setup flask variables

    ````
    export FLASK_APP=api
    
    export FLASK_ENV=development
    ````
    
4. Create database tables and load data

 - Update postgres connection string, open file 'backend/api/db.py' in text editor and update host from "postgres" to "localhost"
 
   From:

   > def get_db(autocommit=False):
    if 'db' not in g:
        g.db = psycopg.connect(
                            host='postgres',
			   
    To:

    > def get_db(autocommit=False):
    if 'db' not in g:
        g.db = psycopg.connect(
                            host='localhost',

                         

    ````
    cd backend
    ````

    ````
    flask init-db
    ````
    
    ````
    flask get-data -t latest
    ````
    
    ````
    flask get-data -t vaccine
    ````
    
 5. Start flask server

    ````
    flask run
    ````
     
    To check if all is well go to http://localhost:5000/country/test this page returns "hello":"world".

    Api Endpoints:  

	<http://localhost:5000/country> "For all countries get the latest data {deaths, confirmed, vaccinated}".<br> 	
	<http://localhost:5000/country/{iso2}> "Get this country ref:<iso2>  latest data {deaths, confirmed, vaccinated}". <br>	
	<http://localhost:5000/country/all/percapita> "Get per capita values (deaths, confirmed, vaccinated) for all countries". <br>
	<http://localhost:5000/country/{iso2}/percapita> "Get per capita for this country ref:<iso2> (deaths, confirmed, vaccinated)".  <br>

     To access the main website go to: http://localhost:5000
    
#### Frontend Development

##### React setup:

 1. Change directory to folder frontend/web. 

    ````
    cd {location of app}/frontend/web
    ````
     
     
 2. Install dependencies  

    ````
    npm install
    ````
    
 3. Start the development server:  
 
     ````
     npm start
     ````

     The website is accessible on http://localhost:3000. 

  4. To Build the website:  

     ````
     npm run build
     ````

## License

MIT
