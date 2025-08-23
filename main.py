import crud, auth
from db import models, schemas
from db.database import engine, SessionLocal, get_db
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from predict import make_prediction
import pandas as pd
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware




models.Base.metadata.create_all (bind=engine)

app = FastAPI (title="Online Shoppers Prediction API")

app.add_middleware (CORSMiddleware,
                    allow_origins=["*"],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
                    
                    )


oauth2_scheme = OAuth2PasswordBearer (tokenUrl='token', scheme_name="JWT")




def get_current_user (token: str = Depends (oauth2_scheme), db: Session = Depends (get_db)):
    try:
        payload = auth.jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get ("sub")
        if username is None:
            raise HTTPException (status_code=401, detail="Invalid Token")
    except:
        raise HTTPException (status_code=401, detail="Invalid Token")
    user = crud.get_user (db, username=username)
    if user is None:
        raise HTTPException (status_code=401, detail="User Not Found")
    return user






@app.post ("/users/", response_model=schemas.UserRead)
def create_new_user (user: schemas.UserCreate, db: Session=Depends (get_db)):
    db_user = crud.get_user (db, user.username)
    if db_user:
        raise HTTPException (status_code=400, detail="username already registered")
    return crud.create_user(db, user.username, user.password)




@app.post("/token")
def login (form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user (db, form_data.username)
    if not user or not auth.verify_password (form_data.password, user.hashed_password):
        raise HTTPException (status_code=400, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_eXPIRE_MINUTES)
    access_token = auth.create_access_token (data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}



@app.post ("/predict/", response_model=schemas.PredictionOut)
def predict (input_data: schemas.InputData, db: Session = Depends(get_db), current_user: models.User = Depends (get_current_user)):
    df = pd.DataFrame ([input_data.model_dump()])
    prob, label = make_prediction(df)
    db_pred = crud.create_predictions(db, current_user.id, input_data.model_dump(), prob, label)
    return db_pred