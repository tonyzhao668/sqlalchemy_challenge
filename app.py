import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################

#file_path ="hawaii.sqlite"
#engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False )



# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table

Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to Tony's Hawaii API<br/>"
        f"Query date must be in the format of 'yyyy-mm-dd', thanks.<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/'2016-09-16'</br>" #the date is sample date
        f"/api/v1.0/start/end/'2017-08-18'/2017-09-11'" #the dates is sample dates
    )


@app.route("/api/v1.0/precipitation")
def date_preci():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the set of dates and corresponding precipitation"""
    # Query all the dates and precipitation
    precipi = session.query(Measurement.date, func.avg(Measurement.prcp)).\
             group_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the data and precipitantion and return jsonified dictionary
    
    date_pre_dict = {}
    for p in precipi:
        if p[0] and p[1]:
            date_pre_dict.update({p[0] : p[1]})
    return jsonify(date_pre_dict)

    

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of station data including the station, name, latitude, longitude, and elevation of each station"""
    # Query all stations
    sels = [Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation]
    total_stations = session.query(*sels).all()


    session.close()

    # Create a dictionary from the station data and append to a list of all_passengers
    t_station = {}
    for s in total_stations:
        detail = []
        for i in range(1, 5):
            detail.append(s[i])
        t_station.update({s[0]: detail})

    return jsonify(t_station)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Query the dates and temperature observations of the most active station for the last year of data."""
    """The date period will be from 22/08/16 to 22/08/17, the most active station is 'USC00519281'""" 

    last_dateminus1 = dt.date(2017, 8, 22)
    oneyearbefore_date = dt.date(2017, 8, 22) - dt.timedelta(days=365)

    temperature_year = session.query(Measurement.date, func.avg(Measurement.tobs)).\
             filter(Measurement.date.between(oneyearbefore_date, last_dateminus1)).\
             filter(Measurement.station =='USC00519281').group_by(Measurement.date).all()

    
    session.close()

    # Create a dictionary from the data and tobs 
    tob_dict = {}
    for t in temperature_year:
        if t[0] and t[1]:
            tob_dict.update({t[0]:t[1]})
    

    return jsonify(tob_dict)
    

@app.route("/api/v1.0/start/<start>")
def startdate(start):
    #calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


    start_date = start
    
    session = Session(engine)

    ts = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
         func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    session.close()

    
    return jsonify(f"The future  TMIN, TAVG, TMAX of your started date are {ts}")

@app.route("/api/v1.0/start/end/<start>/<end>")
def start_end(start, end):
     # Create a dictionary from the row data and append to a list of all_passengers

    start_date = start
    end_date = end
    # start_date = '2015-02-08'
    # end_date = '2015-03-08'
    session = Session(engine)

    se = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),\
            func.max(Measurement.tobs)).filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).all()
    
    
    session.close()


    return jsonify(f"The TMIN, TAVG, TMAX of your selected peroid are {se}")
    #return jsonify(f"{start_date}, {end_date}")


if __name__ == '__main__':
    app.run(debug=True)
