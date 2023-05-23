import requests

BASE_URL = "http://localhost:8000"

def test_is_related_to_recipes():
    url = f"{BASE_URL}/is_related_to_recipes"
    data = {"text": "can you give me nutritional values for carrot juice?"}
    response = requests.post(url, json=data)
    print(response.text)

def test_is_not_related_to_recipes():
    url = f"{BASE_URL}/is_related_to_recipes"
    data = {"text": "This is not a recipe"}
    response = requests.post(url, json=data)
    print(response.text)

test_is_not_related_to_recipes()
test_is_related_to_recipes()
