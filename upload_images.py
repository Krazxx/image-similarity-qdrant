# upload_images.py
from sentence_transformers import SentenceTransformer
from PIL import Image
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import os, uuid

model = SentenceTransformer("clip-ViT-B-32")
qdrant = QdrantClient(path="data")
collection = "car_logos"

qdrant.recreate_collection(
    collection_name=collection,
    vectors_config=VectorParams(size=512, distance=Distance.COSINE),
)

image_folder = "images"
points = []

for image_name in os.listdir(image_folder):
    if not image_name.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    path = os.path.join(image_folder, image_name)
    img = Image.open(path).convert("RGB")
    vector = model.encode(img, convert_to_tensor=False).tolist()

    points.append(
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={"image_name": image_name, "path": path}
        )
    )

qdrant.upsert(collection_name=collection, points=points)
print(f"Uploaded {len(points)} images into Qdrant!")
