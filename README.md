# 🚗🔍 Image Similarity Search using CLIP + Qdrant
A professional image similarity search engine using:

- **CLIP (ViT-B/32)** for image embeddings  
- **Qdrant** for vector storage and similarity search  
- **Python** for indexing & querying images  

---

## 🏆 Features
- Convert images into vector embeddings using CLIP  
- Store vectors in Qdrant local database  
- Run similarity search using a query image  
- Fast cosine similarity ranking  
- Clean folder structure  
- Beginner‑friendly project design  

---

## 📁 Project Structure
```
image-similarity-qdrant/
│
├── images/
│     ├── audi.png
│     ├── bmw.png
│     ├── supra.png
│     ├── query.jpg
│
├── data/
│     └── (auto-created by Qdrant, ignored by GitHub)
│
├── upload_images.py          # Index images into Qdrant
├── query_image.py            # Search images
│
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── .gitignore                # Ignore data & cache
```

---

## 📦 Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/image-similarity-qdrant.git
cd image-similarity-qdrant
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works
1. Load image → Convert to vector (512‑dim) using CLIP  
2. Store vectors inside Qdrant  
3. Query: Encode query image → Search top matches  
4. Qdrant returns highest cosine‑similarity results  

---

## 🚀 Usage

### 1️⃣ Upload images to Qdrant
```bash
python upload_images.py
```

### 2️⃣ Run similarity search
```bash
python query_image.py
```

You will see:
```
Match →
Image: bmw.png
Path: images/bmw.png
Score: 0.9123
```

---

## 🧪 Use Cases
- Car logo recognition  
- Visual search engines  
- Image clustering  
- Duplicate image detection  
- Machine learning experiments  

---

## 🤝 Contributing
Contributions and improvements are welcome!

---

## 📜 License
MIT License — free to use and modify.

---

## ⭐ Support
If this project helps you, please ⭐ star the repository!
