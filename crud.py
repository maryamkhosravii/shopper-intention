from db import models
from sqlalchemy.orm import Session
import json
import auth



def create_user (db: Session, username: str, password: str):

    hashed_password = auth.get_password_hash (password)

    db_user = models.User (username=username, hashed_password=hashed_password)
    
    db.add (db_user)
    db.commit()
    db.refresh (db_user)
    return db_user



def get_user (db: Session, username: str):
    return db.query(models.User).filter(models.User.username==username).first()




def create_predictions (db:Session, user_id:int, features:dict, probability:float, prediction:int):
    
    db_pred = models.Prediction (features=json.dumps(features), probability=probability, prediction=prediction, user_id=user_id)

    db.add (db_pred)
    db.commit()
    db.refresh (db_pred)
    return db_pred