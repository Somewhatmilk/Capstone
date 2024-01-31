import { AutoTokenizer } from '@xenova/transformers';

// Set access token directly in code (keep it private!)
process.env.HF_TOKEN = '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';  // Replace with your actual token

const tokenizer = await AutoTokenizer.from_pretrained('jinaai/jina-embeddings-v2-base-en');


const text = 'Hello world!';
const encoded = tokenizer.encode(text);
console.log(encoded);