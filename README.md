# sqlalchemy_challenge

By Tony Zhao DBCUWA20

Date 23/02/2021

Remarks:
* The last date found in the system database is 2017-08-23, to prevent the last date's data abnormal, the required 12 months have been
  from 2016-08-22 to 2017-08-22.
* So the one year before date was 2016-08-22
* My choosed vacation/trip dates were 2011-02-28 to 2011-03-05
* For everyday's precipitation/tobs, I have used avg, due to one day could be several observations.
* Thank you very much for your review and comments.
* My comment to this homework is that, it is well organized and with quite good challenges.


The following requirements have been done:

Step 1 - Climate Analysis and Exploration
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Done.

Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.

Precipitation Analysis
Design a query to retrieve the last 12 months of precipitation data.
Select only the date and prcp values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.
Use Pandas to print the summary statistics for the precipitation data.

* Done


Station Analysis
Design a query to calculate the total number of stations.
Design a query to find the most active stations.
List the stations and observation counts in descending order.
Which station has the highest number of observations?

* Done

Design a query to retrieve the last 12 months of temperature observation data (TOBS).
Filter by the station with the highest number of observations.
Plot the results as a histogram with bins=12.

* Done

Step 2 - Climate App
Design a Flask API based on the queries that I have just developed.
Use Flask to create my routes.

Routes
/ Home page.
List all routes that are available.

/api/v1.0/precipitation
Convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.

/api/v1.0/stations
Return a JSON list of stations from the dataset.

/api/v1.0/tobs
Query the dates and temperature observations of the most active station for the last year of data.
Return a JSON list of temperature observations (TOBS) for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    
* Done