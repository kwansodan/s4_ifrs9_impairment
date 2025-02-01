from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
import pickle
import pandas as pd
from backend.utils.loan_functions import upload_file

from database import db_operations
from database.db import get_db

router = APIRouter()

# # Load pre-trained logistic regression model
# with open("models/logistic_model.pkl", "rb") as file:
#     model = pickle.load(file)

@router.post("/predict")
def predict_probability(input_data: dict):
    df = pd.DataFrame([input_data])
    probability = model.predict_proba(df)[:, 1]
    return {"probability_of_default": probability[0]}

# # Route to handle file upload
# @router.post('/upload')
# async def upload_file(file: UploadFile = File(...)):
#     result = await upload_file(file)


@router.post("/amortised_balance_calc")
def function():
    pass

@router.post("/ead_calculator")
def function():
    pass


@router.post("/default_determinor")
def function():
    pass

@router.post("/loss_given_default")
def function():
    pass

@router.post("/recoverable_from_guarantee")
def function():
    pass

@router.post("/effective_interest_calc")
def function():
    pass

@router.post("/loan_scheduler")
def function():
    pass

@router.get("/pd_determiner")
def function():
    pass

@router.get("/lifetime_ecl")
def function():
    pass

@router.get("/loan_stager")
def function():
    pass

@router.post("/users/")
def create_user_endpoint(fname: str,lname: str, work_email: str,email_verified: str,last_login: str, db: Session = Depends(get_db)):
    user = db_operations.create_user(db=db, fname=fname, lname=lname, work_email=work_email, email_verified=email_verified, last_login=last_login )
    return {"id": user.id, "fname": user.fname, "lname": user.lname, "work_email": user.work_email, "email_verified": user.email_verified, "last_login": user.last_login}

@router.get("/users/{user_id}")
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}





































































