# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# import textrazor

# app = FastAPI()

# textrazor.api_key = "33b2474c50611d532502adafce2fae756a1e0c30f4063bd70a5f0cff"
# client = textrazor.TextRazor(extractors=["entities"])
# recipe_entity_types = ["Recipe", "Course", "Cuisine", "Ingredient", "Preparation", "Meals", "Food", "Nutrition", "Juices", "fruites","vegetables","Dosa (food)"]

# @app.get("/")
# def hello_world():
#     return {"message": "OK"}

# @app.post("/is_related_to_recipes")
# async def is_related_to_recipes(request: Request):
#     data = await request.json()
#     text = data['text']
#     try:
#         response = client.analyze(text)
#         recipe_entities = [entity for entity in response.entities() if entity.id in recipe_entity_types]
#         return JSONResponse({'result': len(recipe_entities) > 0})
#     except Exception as e:
#         print(f"Failed to analyze with error: {e}")
#         return JSONResponse({'error': 'Failed to analyze text'})

# @app.get("/kar")
# def hello_world():
#     return {"message": "Hello Karthik"}
#//______________________________
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import textrazor

app = FastAPI()

textrazor.api_key = "33b2474c50611d532502adafce2fae756a1e0c30f4063bd70a5f0cff"
client = textrazor.TextRazor(extractors=["entities"])
recipe_entity_types = ["Recipe", "Course", "Cuisine", "Ingredient", "Preparation", "Meals", "Food", "Nutrition", "Juice", "fruites","vegetables","Dosa (food)","juice","juices","vegetable","fruits","fruit","vegetables","recipe","reicipes","meals","meal"]

@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.post("/is_related_to_recipes")
async def is_related_to_recipes(request: Request):
    data = await request.json()
    text = data['text']
    try:
        response = client.analyze(text)
        print(response.entities())
        recipe_entities = [entity for entity in response.entities() if entity.id in recipe_entity_types]
        return JSONResponse({'result': len(recipe_entities) > 0})
    except Exception as e:
        print(f"Failed to analyze with error: {e}")
        return JSONResponse({'error': 'Failed to analyze text'})

@app.post("/is_related_to_recipes_flutter")
async def is_related_to_recipes_flutter(request: Request):
    data = await request.json()
    message = data['message']
    try:
        response = client.analyze(message)
        recipe_entities = [entity for entity in response.entities() if entity.id in recipe_entity_types]
        return JSONResponse({'result': len(recipe_entities) > 0})
    except Exception as e:
        print(f"Failed to analyze with error: {e}")
        return JSONResponse({'error': 'Failed to analyze text'})
