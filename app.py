from fastapi import FastAPI
from pydantic import BaseModel
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import os, json

app = FastAPI(title="HacsWallet")

DATA_DIR = "./data"
os.makedirs(DATA_DIR, exist_ok=True)

class Tx(BaseModel):
    sender: str
    recipient: str
    amount: float

@app.get("/wallet/create")
def create_wallet():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    priv_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    pub_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    addr = pub_bytes.hex()[:40]
    wallet_path = os.path.join(DATA_DIR, f"{addr}.json")

    with open(wallet_path, "w") as f:
        json.dump({"private_key": priv_bytes.decode(), "public_key": pub_bytes.decode(), "balance": 100}, f)

    return {"address": addr, "balance": 100}

@app.get("/wallet/balance/{address}")
def get_balance(address: str):
    path = os.path.join(DATA_DIR, f"{address}.json")
    if not os.path.exists(path):
        return {"error": "Wallet not found"}
    with open(path) as f:
        data = json.load(f)
    return {"address": address, "balance": data["balance"]}

@app.post("/wallet/send")
def send(tx: Tx):
    sender_path = os.path.join(DATA_DIR, f"{tx.sender}.json")
    recipient_path = os.path.join(DATA_DIR, f"{tx.recipient}.json")

    if not os.path.exists(sender_path) or not os.path.exists(recipient_path):
        return {"error": "Sender or recipient not found"}

    with open(sender_path) as f:
        sender_data = json.load(f)
    with open(recipient_path) as f:
        recipient_data = json.load(f)

    if sender_data["balance"] < tx.amount:
        return {"error": "Insufficient balance"}

    sender_data["balance"] -= tx.amount
    recipient_data["balance"] += tx.amount

    with open(sender_path, "w") as f:
        json.dump(sender_data, f)
    with open(recipient_path, "w") as f:
        json.dump(recipient_data, f)

    return {"status": "success", "tx": tx.dict()}

@app.get("/chain/height")
def get_chain_height():
    return {"height": 1}
