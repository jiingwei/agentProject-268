from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from langchain_text_splitters import RecursiveCharacterTextSplitter


# =========================
# 1. 路径
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENT_PATH = (
    BASE_DIR
    / "data"
    / "documents"
    / "company_handbook.txt"
)

CHROMA_PATH = (
    BASE_DIR
    / "data"
    / "chroma_db"
)


# =========================
# 2. 读取文档
# =========================

text = DOCUMENT_PATH.read_text(
    encoding="utf-8"
)


# =========================
# 3. 文档切分
# =========================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)

chunks = splitter.split_text(text)


print("=" * 60)
print(f"文档切分完成，共 {len(chunks)} 个 Chunk")
print("=" * 60)


# =========================
# 4. 加载 Embedding 模型
# =========================

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


# =========================
# 5. 生成向量
# =========================

embeddings = model.encode(
    chunks
)


print("Embedding 完成")


# =========================
# 6. 创建 Chroma
# =========================

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)


# 创建一个 Collection
collection = client.get_or_create_collection(
    name="company_handbook",
    metadata={
        "hnsw:space": "cosine"
    }
)


# =========================
# 7. 保存数据
# =========================

ids = [
    f"chunk_{i}"
    for i in range(len(chunks))
]


collection.upsert(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist(),
)


print("=" * 60)
print("Chroma 向量数据库创建完成")
print(f"数据库位置：{CHROMA_PATH}")
print(f"Collection：company_handbook")
print(f"保存 Chunk 数量：{collection.count()}")
print("=" * 60)