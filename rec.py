import requests

def search_meals(query):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['meals']
    else:
        return None

# Example usage
meals = search_meals('salad')
if meals is not None:
    for meal in meals:
        print(meal['strMeal'])
else:
    print('No meals found')
