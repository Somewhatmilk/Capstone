from transformers import AutoModel
from numpy.linalg import norm


token="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"
cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en',token=token, trust_remote_code=True) # trust_remote_code is needed to use the encode method
# embeddings = model.encode(['How is the weather today?', 'What is the current weather like today?'])
# print(cos_sim(embeddings[0], embeddings[1]))