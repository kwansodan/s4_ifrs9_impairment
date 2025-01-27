from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from routes.api import router
from dotenv import load_dotenv
import os
from database.db import engine, Base

load_dotenv()

app = FastAPI()

# Register API routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "IFRS 9 Impairment Tool API is running"}

@app.post("/hey")
def root():
    return {"message": "IFRS 9 Impairment Tool API is running"}




# Create tables
Base.metadata.create_all(bind=engine)