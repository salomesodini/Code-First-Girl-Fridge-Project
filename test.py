import requests

def recipe_search(ingredient, time=None):
    app_id = '343f7b6d'
    app_key = 'a055d09b732f5e46211e1bdd1ddf4693'

    if time:
        time_in_minutes = int(time) * 60  # Convert hours to minutes
        result = requests.get(
            f"https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}&time={time_in_minutes}")
    else:
        result = requests.get(f"https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}")

    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    time = input('How much time do you have in hours (optional): ')

    results = recipe_search(ingredient, time)

    if not results:
        print("No recipes found for this ingredient and in this time.")
    else:
        for result in results:
            recipe = result['recipe']
            print(recipe['label'])
            print(recipe['url'])
            print()


run()