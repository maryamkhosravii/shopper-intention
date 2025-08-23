from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class UserCreate (BaseModel):
    username: str
    password: str


class UserRead (BaseModel):
    id: int
    username: str
    is_active : bool
    

class config:
    orm_mode = True



class InputData (BaseModel):

    PageValues: float
    Administrative: float
    Administrative_Duration: float
    Informational: float
    Informational_Duration: float
    ProductRelated_Duration: float
    BounceRates:float
    SpecialDay: float
    Month: str
    VisitorType: str



class PredictionOut (BaseModel):

    id: int
    features: str
    probability: float
    prediction: int
    timestamp: datetime



class config:
    orm_mode = True
