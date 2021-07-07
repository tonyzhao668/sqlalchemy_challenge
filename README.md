# sqlalchemy_challenge

By Tony Zhao DBCUWA20

Date 23/02/2021

### Background

To help with trip planning, to do some climate analysis on the area Hawaii! The following outlines what need to be done.

## Step 1 - Climate Analysis and Exploration, done!

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided [hawaii.sqlite](Resources/hawaii.sqlite) files to complete the climate analysis and data exploration.

* I have chosen a start date 2011-02-28 and end date 2011-03-05 for the trip. 

* Use SQLAlchemy `create_engine` to connect to the sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.

* **Precipitation during 22/08/16 to 2208/17**

  ![precipitation](Images/precipitation.PNG)

* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order.

  * Which station has the highest number of observations?

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.
  
  * **Temperature Histogram**

    ![station-histogram](Images/tem_hist.PNG)

- - -

## Step 2 - Climate App, done!

After the initial analysis, design a Flask API based on the queries that have just developed above.

* Use Flask to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of the dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

- - -

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Use SQLAlchemy or pandas's `read_csv()` to perform this portion.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. 

### Temperature Analysis II

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for my trip using the matching dates from the previous year.

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * **The peak-to-peak (TMAX-TMIN) value as the y error bar (YERR)**

    ![temperature](Images/tripavgtemp.PNG)

### Daily Temperature Average

* Calculate the temperature per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Use the function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

* Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

* **Trip Daily Temperature**
  ![daily-normals](Images/triptemp.PNG)


## Remarks:
* The last date found in the system database is 2017-08-23, to prevent the last date's data abnormal, the required 12 months have been
  from 2016-08-22 to 2017-08-22.
* So the one year before date was 2016-08-22
* My choosed vacation/trip dates were 2011-02-28 to 2011-03-05
* For everyday's precipitation/tobs, I have used avg, due to one day could be several observations.




