from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import back.model as model

from typing import List, Optional

app = FastAPI()


class Item(BaseModel):
    content: List[int]

class TrainingItem(BaseModel):
    content: List[int]
    val: int

origines = [
    "http://localhost",
    "http://localhost:8095",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origines,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

res = ""


#On devine le chiffre
@app.post("/items/")
async def create_item(item: Item):
  tmp = model.guess(item.content)
  return JSONResponse(content=model.guess(item.content).tolist())


#On utilise le chiffre pour entrainer
@app.post("/items/training/")
async def create_training(item: TrainingItem):
  print("Value sent for training: " + str(item.val))
  model.train_model(item.val, item.content)
  return item


#On utilise les fichier pour entrainer
@app.get("/items/training/files/")
async def train_files():
  model.train_from_files()
  return "OK"
