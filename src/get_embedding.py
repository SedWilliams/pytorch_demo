from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import numpy as np

import get_tokenized

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

data = get_tokenized.words()

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=data[1:100],
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

result_list = np.array(result.embeddings)

first_result = np.array(result.embeddings[0].values) if result.embeddings else np.zeroes((1,1), dtype=float)

print(f"Embeddings: {result}")
print(f"Embedding shape:{first_result.shape}")


