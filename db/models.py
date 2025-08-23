from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql import func
from sqlalchemy import Integer, String, Float, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship


class User (Base):
    __tablename__ = "users"

    id = Column (Integer, primary_key=True, index=True)
    username = Column (String, index=True, unique=True, nullable=False)
    hashed_password = Column (String, nullable=False)
    is_active = Column (Boolean, default=True)
    predictions = relationship ("Prediction", back_populates="user")





class Prediction (Base):
    __tablename__ = 'predictions'

    id = Column (Integer, primary_key=True, index=True)
    features = Column (Text, nullable=False)
    probability = Column (Float, nullable=False)
    prediction = Column (Integer, nullable=False)
    timestamp = Column (DateTime(timezone=True), server_default=func.now())

    user_id = Column (Integer, ForeignKey("users.id"))
    user = relationship ("User", back_populates="predictions")
