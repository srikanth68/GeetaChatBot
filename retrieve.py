import json

import numpy as np
from sentence_transformers import SentenceTransformer

EMBEDDINGS_PATH = "data/embeddings.npy"
IDS_PATH = "data/ids.json"
MODEL_NAME = "baai/BGE-SMALL-EN-V1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages:"

_model = SentenceTransformer(MODEL_NAME)
_embeddings = np.load(EMBEDDINGS_PATH)
with open(IDS_PATH, "r") as f:
    _ids = json.load(f) 

def retrieve(query: str, k: int = 5) -> list[tuple[str, float]]:
    query_vector = _model.encode(QUERY_PREFIX + query, normalize_embeddings=True)
    scores = _embeddings @ query_vector
    top_indices = np.argsort(-scores)[:k]
    return [(_ids[i], float(scores[i])) for i in top_indices]

if __name__ == "__main__":
    results = retrieve("I failed even after working hard")

    for verse_id, score in results:
        print(verse_id,round(score, 3))

        