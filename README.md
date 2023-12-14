# box-office-predictor
Flask-based web app for predicting box office results using the OMDb API. Enter a date to get predictions based on IMDb ratings. Explore search results with detailed movie information and predictive insights.
# Box Office Prognosticator

## Overview
The Box Office Prognosticator is a Flask web app that predicts box office results based on IMDb ratings. Users can enter a movie name or a specific date to get predictions. The app utilizes the OMDb API for movie data and the BoxOffice library for predictive insights.

## Libraries Used
- **Flask:** A web framework for Python.
- **BoxOffice API:** A custom library for fetching box office data. You can find more information about the BoxOffice API ]
- https://github.com/Stink-Po/boxoffice_api/blob/master/Readme.md

## Obtaining API Keys
To use the BoxOffice API, you need an OMDb API key. Obtain your free key from [OMDb API](https://www.omdbapi.com/apikey.aspx).

****Project Structure****
create a folder which should look like this.and open full folder in you VS CODE or other.
app.py: Main Flask application file.                     
templates/: Folder containing HTML templates:
                                         -----|index.html: Home page template.
                                         -----| result.html: Search results template.

**How to Run**
Navigate to the project directory and open cmd:

cd box-office-prognosticator

Run the Flask app:
python app.py

Open your web browser and go to http://localhost:5000 to access the app.


***Usage***
Enter a specific date on the home page.
Click "Check Prediction" to fetch movie data for that date.
View the search results with predictive insights.

