import numpy as np

def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    step = chunk_size - overlap
    indices = np.arange(0, len(tokens), step)
    
    # Complete chunks lo
    chunks = [tokens[i:i+chunk_size] for i in indices 
              if i + chunk_size <= len(tokens)]
    
    # Agar koi chunk nahi bana (tokens < chunk_size) toh incomplete add karo
    if not chunks and len(tokens) > 0:
        chunks = [tokens[:chunk_size]]
    
    return chunks


print(text_chunking(["a","b","c","d","e","f"], 3, 0))