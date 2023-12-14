from flask import Flask, render_template, request
from boxoffice_api import BoxOffice

app = Flask(__name__)

# Initialize BoxOffice with OMDb API key
box_office = BoxOffice(api_key="your-IMDB-API-key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get user input from the form
    movie_name = request.form.get('movie_name')  # Use get() to handle the absence of 'movie_name'
    date = request.form['date']

    # Use the BoxOffice library to get data
    if movie_name:
        print(f"Searching for movie: {movie_name}")
        result = box_office.search_movie(movie_name)
        print(f"Result: {result}")
    elif date:
        print(f"Getting daily data for date: {date}")
        result = box_office.get_daily(date)
        print(f"Result: {result}")
    else:
        return render_template('index.html', error='Please provide either a movie name or a date.')

    # Add prediction values to each movie in the result
    for movie in result:
        # Use 'imdbRating' as an example. Replace it with the actual key for the rating in your data
        rating_str = movie.get('imdbRating', 'N/A')

        # Check if the value is 'N/A'
        if rating_str.lower() != 'n/a':
            try:
                rating = float(rating_str)
            except ValueError:
                rating = 0.0
        else:
            rating = 0.0

        # Replace this with your actual prediction logic
        prediction_value = calculate_prediction_value(rating)
        prediction = get_prediction_label(prediction_value)
        movie['PredictionValue'] = prediction_value
        movie['Prediction'] = prediction

    return render_template('result.html', result=result)

def calculate_prediction_value(rating):
    # Replace this with your actual calculation logic based on IMDb rating
    return rating * 10

def get_prediction_label(value):
    # Implement your logic to get the prediction label based on the value
    if value >= 70:
        return 'High'
    elif 30 <= value < 70:
        return 'Medium'
    else:
        return 'Low'

if __name__ == '__main__':
    app.run(debug=True)
