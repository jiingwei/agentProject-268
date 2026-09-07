from sentence_transformers import SentenceTransformer


# 加载 Embedding 模型
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


# 准备几个测试文本
texts = [
    "新员工试用期为3+5个月。",
    "新员工需要经过一段时间的试用。",
    "公司的正常工作时间为周一至周五。",
    "今天晚上吃什么？",
]


# 转换成向量
embeddings = model.encode(texts)


print("=" * 60)
print("Embedding 完成")
print(f"文本数量：{len(texts)}")
print(f"向量维度：{embeddings.shape[1]}")
print("=" * 60)


for i, embedding in enumerate(embeddings):
    print(f"\n文本 {i + 1}：{texts[i]}")
    print(f"向量前10个数字：{embedding[:10]}")