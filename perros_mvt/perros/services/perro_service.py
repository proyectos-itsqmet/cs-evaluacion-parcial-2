import requests

from ..models import Perro

def get_perros():
    response = requests.get("https://dogapi.dog/api/v2/breeds", params = {"page[size]": 40})
    if response.status_code != 200:
        print(f"Error al obtener los perros: {response.status_code}")
        return []
    return response.json()["data"]

def load_perros():
    if Perro.objects.count():
        return f"Ya existen {Perro.objects.count()} perros"

    perros = get_perros()
    for perro in perros:
        atributos = perro["attributes"]
        imagenes = atributos["images"]
        Perro.objects.create(
            nombre = atributos["name"],
            descripcion = atributos["description"],
            imagen = imagenes[0]["medium"] if imagenes else "",
            temperamento = ", ".join(atributos.get("traits", {}).get("temperament", [])),
            origen = atributos.get("origin", {}).get("country", ""),
            otros_nombres = ", ".join(atributos.get("other_names", [])),
        )
    return f"Se cargaron {Perro.objects.count()} perros"
