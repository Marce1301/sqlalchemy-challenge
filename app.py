# Import the dependencies.
import numpy as np
import datetime
import sqlalchemy
import os

#from sqlalchemy.sql import func
from datetime import datetime, timedelta
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify 


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
#First root route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Note: to access values between a start and end date enter both dates using format: YYYY-mm-dd/YYYY-mm-dd"
    )
# Flask Routes

@app.route("/api/v1.0/precipitation")
def precipitations():
    session = Session(engine)
    """return a list of precipitation (prcp) and date (date) data"""

    precipitation_query_results = session.query(measurement.prcp, measurement.date).all()

    session.close()

    precipitaton_query_values = []
    for prcp, date in precipitation_query_results:
        precipitation_dict = {}
        precipitation_dict["precipitation"] = prcp
        precipitation_dict["date"] = date
        precipitaton_query_values.append(precipitation_dict)

    return jsonify(precipitaton_query_values) 


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    """return a list of stations data"""
    stations_query_results = session.query(station.station, station.id).all()

    session.close()

    stations_query_values = []
    for stations, id in stations_query_results:
        station_dict = {}
        station_dict['station'] = stations
        station_dict['id'] = id
        stations_query_values.append(station_dict)

    return jsonify(stations_query_values) 


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    """Return a list of dates and temps observed for the most active station for the last year of data from the database""" 
    latest_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    latest_date_str = latest_date.date  # extract the date value as a string
    return jsonify({"latest_date": latest_date_str})

    session.close()


@app.route("/api/v1.0/<start>")

def start_date(start):
    try:
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400

    session = Session(engine) 
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""

    start_date_tobs_results = session.query(func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).all()

    session.close()

    start_date_tobs_values =[]
    for min, avg, max in start_date_tobs_results:
        start_date_tobs_dict = {}
        start_date_tobs_dict["min"] = min
        start_date_tobs_dict["average"] = avg
        start_date_tobs_dict["max"] = max
        start_date_tobs_values.append(start_date_tobs_dict)
    
    return jsonify(start_date_tobs_values)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a specified start date and end date."""
    try:
        start_end = datetime.datetime.strptime(start, '%Y-%m-%d').date()

    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 404

    session = Session(engine)
    """Return a list of min, avg and max tobs between start and end dates entered"""

    start_end_date_tobs_results= session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

    session.close()

    start_end_tobs_date_values = []
    for min, avg, max in start_end_date_tobs_results:
        start_end_tobs_date_dict = {}
        start_end_tobs_date_dict["min_temp"] = min
        start_end_tobs_date_dict["avg_temp"] = avg
        start_end_tobs_date_dict["max_temp"] = max
        start_end_tobs_date_values.append(start_end_tobs_date_dict) 
    

    return jsonify(start_end_tobs_date_values) 
           
if __name__ == '__main__':
    app.run(debug=True) 


