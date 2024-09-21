import requests

def recipe_search(ingredient, health, diet, calories, time):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = "df314b43"
    app_key = "13f73d9697a4dbfc19f1ec21532b0ad2"
    # API request URL now includes the 'time' parameter
    result = requests.get(
        "https://api.edamam.com/search?q={}&app_id={}&app_key={}&diet={}&health={}&calories={}&time={}".format(
            ingredient, app_id, app_key, diet, health, calories, time
        )
    )
    data = result.json()
    return data["hits"]

def run():
    # User inputs for search parameters
    ingredient = input("Enter an ingredient: ")  # e.g., tomato
    health = input("Enter health requirements: ")  # e.g., dairy-free
    diet = input("Enter dietary specifications: ")  # e.g., high-protein
    calories = input("Enter calorie range (e.g., 0-2000) or maximum calories: ")  # e.g., 0-2000 or 500
    time = input("Enter maximum cooking time in minutes: ")  # e.g., 30

    # Handle calorie input: can be a range (e.g., "0-2000") or a single maximum value (e.g., "500")
    if '-' in calories:
        # If it's a range, split it into min and max
        calorie_min, calorie_max = map(int, calories.split('-'))
    else:
        # If it's a single value, treat it as the maximum, with 0 as the minimum
        calorie_min, calorie_max = 0, int(calories)

    # Perform the API search
    results = recipe_search(ingredient, health, diet, calories, time)

    # Process and display the results
    for result in results:
        recipe = result["recipe"]
        recipe_calories = round(recipe["calories"])

        # Filter recipes based on the calorie range
        if calorie_min <= recipe_calories <= calorie_max:
            print(recipe["label"])
            print(recipe["url"])
            print(recipe_calories)
            print()


run()
