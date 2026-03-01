from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

import get_tokenized

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

data = get_tokenized.sentences()

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=data,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

print(f"Embeddings: {result}")


