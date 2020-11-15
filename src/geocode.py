
import requests

def geocode(address):
    """
    Saca las coordenadas de una dirección que le des.
    """
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    try:
        return {
            "type":"Point",
            "coordinates":[float(data["longt"]),float(data["latt"])]}
    except:
        return data