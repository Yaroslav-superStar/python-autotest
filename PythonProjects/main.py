import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "8d6c92cdbeefbf263ae5444445484ca3"
HEADER = {"Content-Type" : "application/json", "trainer_token": TOKEN}
Body_registration= {
    "trainer_token": TOKEN,
    "email": "ayroslav.20@mail.ru",
    "password": "4357123Zz"}

body_confirmation= {
    "trainer_token": TOKEN
}

body_create= {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change= {
    "pokemon_id": "69967",
    "name": "Bober",
    "photo_id": 5
}

body_poceboll= {
    "pokemon_id": "69967"
}

response = requests.post(url = f"{URL}/trainers/reg", headers = HEADER, json=Body_registration)
print(response.text)

response_confirmation= requests.post(url=f"{URL}/trainers/confirm_email", headers= HEADER, json=body_confirmation)
print(response_confirmation.text)

response_create= requests.post(url=f"{URL}/pokemons", headers = HEADER, json=body_create)
print(response_create.text)


response_change= requests.put(url=f"{URL}/pokemons", headers = HEADER, json=body_change)
print(response_change.text) 


response_poceboll= requests.post(url=f"{URL}/trainers/add_pokeball", headers = HEADER, json=body_poceboll)
print(response_poceboll.text)
