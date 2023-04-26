import json
import csv
def toDict(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)
    
def getItem(data: dict):
    """
    data = { 
        "type": "Feature", 
        "properties": { 
            "letter": "A", 
            "gender": "M", 
            "name": "Abadjon", 
            "origin": "Arabcha", 
            "meaning": "Mangu, cheksiz, abadiy, umri uzoq" }, 
        
        "geometry": null 
            },

    Returns:
        dict: data = {
            "gender": "M",
            "name": "Abadjon",
            "origin": "Arabcha",
            "meaning": "Mangu, cheksiz, abadiy, umri uzoq"
        }
    """
    gender = data['properties']['gender']
    name = data['properties']['name']
    origin = data['properties']['origin']
    meaning = data['properties']['meaning']
    return {
        "gender": gender,
        "name": name,
        "origin": origin,
        "meaning": meaning
    }

def writeToCsv(data: list, func):
    with open('uzbNames.csv', 'w', newline="") as f:
        fieldbame = ["gender", "name", "origin", "meaning"]
        writer = csv.DictWriter(f, fieldnames=fieldbame)

        writer.writeheader()
        for item in data:
            writer.writerow(func(item))

if __name__ == "__main__":

    data = toDict('data.json')

    writeToCsv(data, getItem)