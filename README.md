# Weather Data Project

## Description
This project is designed to fetch, process, and analyze weather data via the OpenWeather API.
It includes Python scripts that perform data collection, database management, and the utility functions that organize the weather data from OpenWeather.

## Current Status
Work in progress. Primary scripts are functional. Future updates to focus on:
- Error handling
- More database functionality
- Improving data analysis features
- Possibly traffic data

## Structure 
- 'scripts/' -- contains the main scripts and utility functions
- 'data/' -- currently a placeholder folder for storing fetched/processed data
- 'requirements.txt' -- lists versions of relevant software in order to reproduce my venv

## Design Decisions
- FIXME: decisions for things that came befoe initial Git commit
- Separation of concerns: I separated API handling, data transformation, and database logic, into separate scripts for clarity, scalability, and maintainability
- Daily weather data pulls: I decided to pull weather data once a day at 12:00pm. This lends itself to extensions in the future if desired (for example, pulling data for the morning and evening as well)
- Single table for all cities: My initial plan was to make one table per city, but I realized from a design standpoint that it'd be much more appropriate to store weather data within a single table. I came to this conclusion because each city stores the exact same set of data, so weather data is the entity at play here; also, opting for a single table prevented my Python code (main.py and database_utils.py) from becoming reptitive with multiple weather-pulling functions and insertion statements
- Composite primary key: upon making the decision to use a single table for multiple cities, I realized that 'date' would no longer be a suitable primary key (multiple rows would contain the same date because more than one city is being pulled). In order to uniquely identify any row, I needed the value of both the 'city' and the 'date' columns
- Rerun capabilities via 'ON DUPLICATE KEY UPDATE' clause: this was added for the event in which I accidentally run main.py too early in the day and hence need to safely rerun the code