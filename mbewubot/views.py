import os
import pickle
import faiss
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sentence_transformers import SentenceTransformer
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use the exact same absolute paths that work in Jupyter
MODEL_DIR = r"C:\Users\MARTY\Documents\mbewuguide-prototype\mbewuguide_backend\mbewubot\agri_bot_model"

index_path = os.path.join(MODEL_DIR, "faiss_index.index")
chunks_path = os.path.join(MODEL_DIR, "text_chunks.pkl")

# Log the paths and check if files exist
logger.info(f"FAISS index path: {index_path}")
logger.info(f"Text chunks path: {chunks_path}")
logger.info(f"FAISS index exists: {os.path.exists(index_path)}")
logger.info(f"Text chunks exist: {os.path.exists(chunks_path)}")

# Load model and chunks on startup with error handling
try:
    index = faiss.read_index(index_path)
    logger.info("FAISS index loaded successfully!")
except Exception as e:
    logger.error(f"Failed to load FAISS index: {e}")
    index = None

try:
    with open(chunks_path, "rb") as f:
        chunks = pickle.load(f)
    logger.info(f"Text chunks loaded successfully! Number of chunks: {len(chunks)}")
except Exception as e:
    logger.error(f"Failed to load text chunks: {e}")
    chunks = None

try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    logger.info("SentenceTransformer model loaded successfully!")
except Exception as e:
    logger.error(f"Failed to load SentenceTransformer model: {e}")
    model = None

# Small talk dictionary
DEFAULT_RESPONSES = {
    "hi": "Hello! How can I assist you with agriculture today?",
    "how are you": "I'm doing well — ready to help you farm smarter!",
    "thanks": "You're welcome!",
    "what's your name": "I'm MbewuBot — your smart agriculture assistant!",
    "bye": "Goodbye! Come back anytime."
}

@csrf_exempt
def ask_mbweubot(request):
    if request.method == "POST":
        # Check if models are loaded
        if index is None or chunks is None or model is None:
            logger.error("Models not loaded properly")
            return JsonResponse({"answer": "🤖 Sorry, the model is not loaded properly. Please try again later."}, status=500)
        
        body = json.loads(request.body.decode("utf-8"))
        question = body.get("question", "").lower().strip()

        # Handle small talk
        for key in DEFAULT_RESPONSES:
            if key in question:
                return JsonResponse({"answer": DEFAULT_RESPONSES[key]})

        # Embed question
        try:
            query_embedding = model.encode([question])
            D, I = index.search(np.array(query_embedding, dtype='float32'), k=3)

            if D[0][0] > 1.0:
                return JsonResponse({"answer": "🤖 Sorry, I don't have enough information on that yet."})

            selected = [chunks[i] for i in I[0]]
            answer = " ".join(selected)
            words = answer.split()
            if len(words) > 100:
                answer = " ".join(words[:100]) + "..."

            return JsonResponse({"answer": answer})
        except Exception as e:
            logger.error(f"Error processing question '{question}': {e}")
            return JsonResponse({"answer": "🤖 Sorry, there was an error processing your question. Please try again."}, status=500)
    
    return JsonResponse({"error": "POST request required."}, status=400)
