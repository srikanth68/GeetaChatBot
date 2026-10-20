import json
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_PATH = "data/geetachunks.json"
EMBEDDINGS_PATH="data/embeddings.npy"
IDS_PATH="data/ids.json"
MODEL_NAME="baai/BGE-SMALL-EN-V1.5"

def main() -> None:
    with open(CHUNKS_PATH,encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [f'{chunk["topic"]}.{chunk["text"]}' for chunk in chunks]
    ids = [chunk["id"] for chunk in chunks]

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(texts,normalize_embeddings=True)

    np.save(EMBEDDINGS_PATH,embeddings)

    with open(IDS_PATH,"w",encoding="utf-8") as f:
        json.dump(ids,f)
    print(embeddings.shape)

if __name__ == "__main__":
    main()


        

