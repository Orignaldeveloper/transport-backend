from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import collection
from pydantic import BaseModel

app = FastAPI()

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Transport backend running"}

class CashMemo(BaseModel):
    lr_no: str
    date: str
    sender_name: str
    receiver_name: str
    from_location: str
    to_location: str
    material: str
    weight: float
    freight_amount: float
    vehicle_number: str

@app.post("/cash-memo")
def save_cash_memo(memo: CashMemo):
    result = collection.insert_one(memo.dict())
    return {"status": "saved successfully", "id": str(result.inserted_id)}
