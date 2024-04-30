from typing import Any
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import (
load_index_from_storage,
    
    StorageContext,
    ServiceContext
)
from llama_index.vector_stores.faiss import FaissVectorStore
import json
from llama_index.core import Settings
class ContextRetrieval():
    def __init__(self,
                 db_path,
                 embed_path="./models/bge-m3"):
        
        # self.docno_to_answer = json.load(open('docno_to_answer.json','r'))
        self.embeddings = HuggingFaceEmbedding(model_name=embed_path,max_length=1024, device='cpu')
        persist_dir=db_path
        vector_store = FaissVectorStore.from_persist_dir(persist_dir)
        Settings.llm = None
        Settings.embed_model = self.embeddings
        storage_context = StorageContext.from_defaults(vector_store=vector_store, persist_dir=persist_dir)
        index = load_index_from_storage(storage_context=storage_context)
        
        self.query_enging = index.as_query_engine(similarity_top_k=5)


    def __call__(self,query) :
                
       
        response_ = self.query_enging.query(query)

  
        

        return {
          
            'query' : query,
            'prompt' : response_.response
         }