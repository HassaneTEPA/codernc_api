import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

url = "https://data.gouv.nc/api/explore/v2.1/catalog/datasets/offres-demploi/records?where=titreoffre%20like%20%22d%C3%A9veloppeur%22%20"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data in the response
    data = response.json()

    # Now 'data' contains the parsed JSON data
    # You can access and manipulate the data as needed
    offers = []
    for item in data["results"]:
        parsed_item = {
            'offer_title': item['titreoffre'],
            'employer_name': item.get('employeur_nomentreprise', ''),
            'job_location': item.get('communeemploi', ''),
            'contract_type': item.get('typecontrat', ''),
            'start_date': item.get('apourvoirle', ''),
            'experience_required': item.get('experience', ''),
            'education_level': item.get('niveauformation', ''),
            'diplome': item.get('diplome', ''),
            'description': item.get('informationcomplementaire', ''),
            'contact_email': item.get('contact_mail', ''),
            'contact_telephone': item.get('contact_telephone', ''),
            'driver_license': item.get('permis', ''),
            'competences': item.get('competences_multivalue', ''),
            'activites': item.get('activites_multivalue')
        }
        offers.append(parsed_item)


# Define a route to get a list of all items
@app.route('/api/offers', methods=['GET'])
def get_items():
    return jsonify(offers)


if __name__ == '__main__':
    app.run(debug=True)
