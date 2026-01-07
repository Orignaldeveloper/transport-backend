from fastapi import FastAPI
from backend.database import collection

from pydantic import BaseModel

app = FastAPI()

# Define the structure of a cash memo
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

# Route to save cash memo
@app.post("/cash-memo")
def save_cash_memo(memo: CashMemo):
    result = collection.insert_one(memo.dict())
    return {"status": "saved successfully", "id": str(result.inserted_id)}
