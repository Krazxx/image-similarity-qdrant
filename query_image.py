# query_image.py
from sentence_transformers import SentenceTransformer
from PIL import Image
from qdrant_client import QdrantClient

model = SentenceTransformer("clip-ViT-B-32")
qdrant = QdrantClient(path="data")
collection = "car_logos"

query_path = "images/query.jpg"
query_image = Image.open(query_path).convert("RGB")
query_vector = model.encode(query_image, convert_to_tensor=False).tolist()

results = qdrant.search(
    collection_name=collection,
    query_vector=query_vector,
    limit=3
)

for r in results:
    print("\nMatch →")
    print("Image:", r.payload["image_name"])
    print("Path:", r.payload["path"])
    print("Score:", r.score)
