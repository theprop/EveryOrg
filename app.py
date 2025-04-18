# app.py
# Flask application with a Pinterest-like UI displaying nonprofit images.
# Uses single-word causes (e.g., "Gorillas"). On hover, shows "Click here to see non-profits".
# On click, JavaScript in the browser fetches nonprofits from Every.org API and displays links.
# Runs on Ubuntu 20.04 with 2 vCPUs, 4GB RAM, compatible with Gunicorn/Nginx.

from flask import Flask, render_template

app = Flask(__name__)

# Nonprofit data: cause, image, CC license
nonprofits = [
    {"cause": "Gorillas", "image": "gorillas.jpg", "license": "CC BY-SA 4.0, Photo by Charles J. Sharp"},
    {"cause": "Elephants", "image": "elephants.jpg", "license": "CC BY 2.0, Photo by Thomas Fuhrmann"},
    {"cause": "Rainforests", "image": "rainforests.jpg", "license": "CC BY 2.0, Photo by Rhett A. Butler"},
    {"cause": "Birds", "image": "birds_general.jpg", "license": "CC BY-SA 4.0, Photo by Bernard DUPONT"},
    {"cause": "Monkeys", "image": "monkeys.jpg", "license": "CC BY-SA 4.0, Photo by Derek Keats"},
    {"cause": "Arctic", "image": "arctic.jpg", "license": "CC BY 2.0, Photo by NOAA"},
    {"cause": "Cancer", "image": "cancer_research.jpg", "license": "CC0, None required"},
    {"cause": "Climate", "image": "climate_change.jpg", "license": "CC0, None required"}
]

@app.route('/')
def index():
    return render_template('index.html', nonprofits=nonprofits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
