from pymongo import MongoClient
import certifi

MONGO_URL = "mongodb+srv://transport_user:transport123@transport-cluster.aqzl8dv.mongodb.net/?appName=transport-cluster"

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client.transport_db
collection = db.cash_memos
