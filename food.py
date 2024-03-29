# CRUD 
# C - Create 
# R - Read
# U - Update
# D - Delete

# HTTP REQUESTS/RESPONSE
# Create - Post
# Read - Get
# Update - Put
# Delete - Delete
from fastapi import FastAPI, Body

app = FastAPI()

FOODS = [{'name': 'Matooke', 'price':2000}, {'name':"Fish", 'price':5000}]



@app.get('/menu')
def get_all_foods():
    return FOODS

@app.get('/menu/{food_name}')
def get_single_food(food_name):
    for food in FOODS:
        if food.get('name').casefold() == food_name.casefold():
            return food
        return {'error': 'Food not found'}


@app.post('/menu')
def add_new_food(body=Body()):
    return FOODS.append(body)

@app.delete('/menu/{food_name}')
def delete_food(food_name):
    for food in FOODS:
        if food.get('name').casefold()== food_name.casefold():
            FOODS.remove(food)
            return {'success':'Food Deleted successfully'}
        return {'error':'Food not in list'}


#users, name, picture, phone

#departments - name

#items - name, quantity, picked_up_by, picked_up_datetime, return_datetime, returned_by

