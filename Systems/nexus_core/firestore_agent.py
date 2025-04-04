# nexus_core/firestore_agent.py

from google.cloud import firestore
import os

# Load project credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secrets/nova_service_account.json"  # or wherever it lives

db = firestore.Client()

def save_memory(collection: str, document_id: str, data: dict):
    """Save a memory to Firestore"""
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.set(data)

def get_memory(collection: str, document_id: str):
    """Retrieve a memory from Firestore"""
    doc_ref = db.collection(collection).document(document_id)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

def delete_memory(collection: str, document_id: str):
    """Delete a memory from Firestore"""
    db.collection(collection).document(document_id).delete()
