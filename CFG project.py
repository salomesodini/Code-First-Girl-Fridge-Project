import requests

def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '343f7b6d'
    app_key = 'a055d09b732f5e46211e1bdd1ddf4693'
    result = requests.get(f"https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}")
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])
        print()

run()
