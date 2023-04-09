## Sqlalchemy-challenge
Project 10 where I’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of a climate database

# Introduction
Considering to treat to a long holiday vacation in Honolulu, Hawaii this project help with the trip planning, with a climate analysis about the area. 
The following sections outline the steps that I need to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data
In this part there will be used SQLAlchemy ORM queries, Pandas, and Matplotlib.   The create_engine() function will be used to connect to  SQLite database and  SQLAlchemy automap_base() function will help  to reflect the tables into classes. After reflecting the tables the references will be saved as "station" and "measurement" classes.
The exploratory analysis for part 1 will be dividied into tow parts : 1) Precipitation Analysis and 2)Station Analysis
 # Precipitation Analysis
The steps done in this part of the challenge were :
* Find the most recent date in the data set
* Get the previous 12 months of precipitation data by querying the previous 12 months of data.
* Select only the "date" and "prcp" values.
* Load the query results into a Pandas DataFrame, and set the index to the "date" column.
* Sort the DataFrame values by "date".
*  Plot the results by using the DataFrame plot method (Pandas Plotting with Matplotlib to plot the data).
*  Use Pandas to calcualte the summary statistics for the precipitation data

# Station Analysis
In this part of the challenge the steps done were:
* Design a query to calculate the total number stations in the dataset, useing the func.count .
* Design a query to find the most active stations & List the stations and the counts in descending order.
* Using the most active station id from the previous query, calculate the lowest, highest, and average temperature using func.min, func.max, and func.avg . 
* Using the most active station id, query the last 12 months of temperature observation data (TOBS) for this station and plot the results as a histogram.

Close the session.

# Part 2: Design Your Climate App
Design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
 
All available api routes:
 
*       /api/v1.0/precipitation
*       /api/v1.0/stations
*       /api/v1.0/tobs
*       /api/v1.0/start
*       /api/v1.0/start/end

Precipitation 
* Convert the query results from your precipitation analysis to a dictionary using date as the key and prcp as the value.
* Return the JSON representation of your dictionary

Stations
* Return a JSON list of stations from the dataset.

Tobs 
* Query the dates and temperature observations of the most-active station for the previous year of data.
* Return a JSON list of temperature observations for the previous year.

Start and start_end
* Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
* Here the user wil have to set in the URL the dates in format YYYY-MM-DD

Do not forgeting to close Sessions.

#References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml

Help retrived from : 
https://stackoverflow.com/questions/69894583/get-missing-1-required-positional-argument-to-date
