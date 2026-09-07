from sentence_transformers import SentenceTransformer
import chromadb
# from langchain_core.tools import tool

# =========================================
# 1. 加载 Embedding 模型
# =========================================

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

model = SentenceTransformer(MODEL_NAME)


# =========================================
# 2. 连接 Chroma 数据库
# =========================================

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_collection(
    name="company_handbook"
)


# =========================================
# 3. 定义知识库搜索工具
# =========================================
# @tool
def search_company_handbook(query: str) -> str:
    """
    在公司员工手册知识库中搜索相关内容。
    """

    print("\n[Tool] knowledge_search 开始执行")
    print(f"[Tool] 用户问题：{query}")

    # 将用户问题转换成向量
    query_embedding = model.encode(query).tolist()

    print("[Tool] 查询向量生成完成")
    print(f"[Tool] 向量维度：{len(query_embedding)}")

    # 查询 Chroma
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    documents = results["documents"][0]

    print(f"[Tool] 找到 {len(documents)} 个相关 Chunk")

    # 整理检索结果
    answer = "\n\n".join(documents)

    print("[Tool] knowledge_search 执行完成")

    return answer


if __name__ == "__main__":
    # query = "新员工试用期是多久？"
    query = "感冒需要住院多久？"

    result = search_company_handbook(query)

    print("\n==============================")
    print("最终检索结果：")
    print("==============================")
    print(result)
