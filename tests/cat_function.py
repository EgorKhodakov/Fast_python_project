import requests




def get_fact_of_cat():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    return response
