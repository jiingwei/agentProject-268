import chromadb
from sentence_transformers import SentenceTransformer


# =========================
# 1. 加载 Embedding 模型
# =========================

# model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
# 这里需要和embedding.py使用到的模型是一致的
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# =========================
# 2. 连接已经保存的 Chroma
# =========================

client = chromadb.PersistentClient(
    path="./data/chroma_db"
)


# =========================
# 3. 获取 Collection
# =========================

collection = client.get_collection(
    name="company_handbook"
)


# =========================
# 4. 用户问题
# =========================

query = "新员工试用期是多久？"


# =========================
# 5. 将问题转换成向量
# =========================

query_embedding = model.encode(
    query
).tolist()


print("=" * 60)
print("用户问题：")
print(query)

print("=" * 60)
print("查询向量维度：")
print(len(query_embedding))
print("=" * 60)



# =========================
# 6. 向量检索
# =========================

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)


# =========================
# 7. 输出检索结果
# =========================

print("=" * 60)
print("用户问题：")
print(query)

print("=" * 60)
print("检索结果：")

for i, document in enumerate(results["documents"][0]):
    print(f"\n--- Chunk {i + 1} ---")
    print(document)

print("=" * 60)