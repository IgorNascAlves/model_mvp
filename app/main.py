from typing import Union
from fastapi import FastAPI

from models_utils import load_model, make_prediction

app = FastAPI()
loaded_model = load_model()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/game_prediction/{item_id}")
def read_item(Q: int, fieldGoalsMade: int, fieldGoalsAttempted: int, threePointersMade: int,
    threePointersAttempted: int, freeThrowsMade: int, freeThrowsAttempted: int, reboundsOffensive: int,
    reboundsDefensive: int, assists: int, steals: int, blocks: int, turnovers: int, foulsPersonal: int, points: int):

    return make_prediction(loaded_model, Q, fieldGoalsMade, fieldGoalsAttempted, threePointersMade,
    threePointersAttempted, freeThrowsMade, freeThrowsAttempted, reboundsOffensive,
    reboundsDefensive, assists, steals, blocks, turnovers, foulsPersonal, points)