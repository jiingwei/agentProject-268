from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter


# 找到项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 找到知识库文件
FILE_PATH = BASE_DIR / "data" / "documents" / "company_handbook.txt"


# 读取文档
text = FILE_PATH.read_text(encoding="utf-8")

print("=" * 60)
print("====== ↓↓↓ 原始文档 ↓↓↓ ======")
print(text)


# 创建文本切分器
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)


# 切分文档
chunks = splitter.split_text(text)


print("=" * 60)
print(f"文档被切分成 {len(chunks)} 个 Chunk")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)