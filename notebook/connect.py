from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os   

# Cargar variables de entorno
load_dotenv()

MONGO_URI = os.getenv('MONGODB_URI_ATLAS')
DB_NAME_ATLAS = os.getenv('MONGODB_DATA')

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client[DB_NAME_ATLAS]
    print("✅ Conexión exitosa a MongoDB Atlas")

    colecciones = db.list_collection_names()
    print('Base de Datos:', DB_NAME_ATLAS)
    print('Colecciones:', colecciones)

except errors.ServerSelectionTimeoutError as e:
    print("❌ No se pudo conectar al servidor:", e)

except errors.OperationFailure as e:
    print("❌ Error de autenticación:", e)

except Exception as e:
    print('⚠️ Error desconocido:', e)
