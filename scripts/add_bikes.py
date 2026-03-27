from datetime import datetime
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# --------------------------
# MongoDB connection
# --------------------------
load_dotenv("stack.env")
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_HOST = "localhost"
MONGO_PORT = os.environ.get("MONGO_PORT")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/")
db = client[DATABASE_NAME]

bikes = [
    {
        "id": "0",
        "type": "ROUTE",
        "label": "Bike label 0",
        "prix": {
            "achat": 1000.0,
            "potentiel": 1200.0,
            "annonce": None,
            "vendu": None
        },
        "status": [
            {
                "status": "DEVIS",
                "date": datetime(2024, 4, 26, 0, 0, 0)
            }
        ],
        "services": [
            {"category": "Démontage", "label": "Complet", "temps_estim": 60, "temps_reel": None},
            {"category": "Nettoyage", "label": "Complet", "temps_estim": 360, "temps_reel": None},
            {"category": "Montage", "label": "Complet", "temps_estim": 60, "temps_reel": None},
            {"category": "Réglage", "label": "Complet", "temps_estim": 60, "temps_reel": None},
        ],
        "pieces": [
            {"label": "Guidoline", "prix_estim": 15.0, "qt_estim": 1, "prix_reel": None, "qt_reel": None},
            {"label": "Patins", "prix_estim": 10.0, "qt_estim": 2, "prix_reel": None, "qt_reel": None},
        ]
    },
    {
        "id": "1",
        "type": "VILLE",
        "label": "Bike label 1",
        "prix": {
            "achat": 100.0,
            "potentiel": 200.0,
            "annonce": None,
            "vendu": None
        },
        "status": [
            {"status": "DEVIS", "date": datetime(2024, 4, 26, 0, 0, 0)},
            {"status": "RENOVATION", "date": datetime(2024, 4, 27, 0, 0, 0)},
        ],
        "services": [
            {"category": "Démontage", "label": "Complet", "temps_estim": 60, "temps_reel": 30},
            {"category": "Nettoyage", "label": "Complet", "temps_estim": 360, "temps_reel": 460},
            {"category": "Montage", "label": "Complet", "temps_estim": 60, "temps_reel": 60},
            {"category": "Réglage", "label": "Complet", "temps_estim": 60, "temps_reel": 90},
        ],
        "pieces": [
            {"label": "Guidoline", "prix_estim": 15.0, "qt_estim": 1, "prix_reel": 30.0, "qt_reel": 1},
            {"label": "Patins", "prix_estim": 10.0, "qt_estim": 2, "prix_reel": None, "qt_reel": None},
        ]
    },
    {
        "id": "2",
        "type": "ELECTRIQUE",
        "label": "Bike label 2",
        "prix": {
            "achat": 100.0,
            "potentiel": 200.0,
            "annonce": 250.0,
            "vendu": 220.0
        },
        "status": [
            {"status": "DEVIS", "date": datetime(2024, 4, 26, 0, 0, 0)},
            {"status": "RENOVATION", "date": datetime(2024, 4, 27, 0, 0, 0)},
            {"status": "ANNONCE", "date": datetime(2024, 4, 28, 11, 6, 0)},
            {"status": "VENDU", "date": datetime(2024, 4, 29, 10, 3, 6)},
        ],
        "services": [
            {"category": "Démontage", "label": "Complet", "temps_estim": 60, "temps_reel": 10},
            {"category": "Nettoyage", "label": "Complet", "temps_estim": 360, "temps_reel": 10},
            {"category": "Montage", "label": "Complet", "temps_estim": 60, "temps_reel": 10},
            {"category": "Réglage", "label": "Complet", "temps_estim": 60, "temps_reel": 10},
        ],
        "pieces": [
            {"label": "Guidoline", "prix_estim": 15.0, "qt_estim": 1, "prix_reel": 30.0, "qt_reel": 1},
            {"label": "Patins", "prix_estim": 10.0, "qt_estim": 2, "prix_reel": None, "qt_reel": None},
        ]
    }
]

collection = db["Bikes"]
collection.insert_many(bikes)
print("Bikes added successfully!")