import os
import pickle
import numpy as np
import faiss
from django.conf import settings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class AgriBotModel:
    """Service class to handle the agricultural bot model operations"""
    
    def __init__(self):
        self.index = None
        self.text_chunks = None
        self.vectorizer = None
        self._load_model()
    
    def _load_model(self):
        """Load the FAISS index and text chunks"""
        try:
            # Load FAISS index
            index_path = os.path.join(settings.MODEL_FILES_DIR, 'faiss_index.index')
            if os.path.exists(index_path):
                self.index = faiss.read_index(index_path)
            else:
                # Fallback to original location
                self.index = faiss.read_index('faiss_index.index')
            
            # Load text chunks
            chunks_path = os.path.join(settings.MODEL_FILES_DIR, 'text_chunks.pkl')
            if os.path.exists(chunks_path):
                with open(chunks_path, 'rb') as f:
                    self.text_chunks = pickle.load(f)
            else:
                # Fallback to original location
                with open('text_chunks.pkl', 'rb') as f:
                    self.text_chunks = pickle.load(f)
            
            # Initialize TF-IDF vectorizer for query processing
            self.vectorizer = TfidfVectorizer(
                max_features=1000,
                stop_words='english',
                ngram_range=(1, 2)
            )
            
            # Fit the vectorizer on the text chunks
            if self.text_chunks:
                self.vectorizer.fit(self.text_chunks)
                
        except Exception as e:
            print(f"Error loading model: {e}")
            self.index = None
            self.text_chunks = None
            self.vectorizer = None
    
    def search(self, query, top_k=5):
        """Search for similar content based on the query"""
        if not self.index or not self.text_chunks or not self.vectorizer:
            return {
                'error': 'Model not loaded properly',
                'results': []
            }
        
        try:
            # Vectorize the query
            query_vector = self.vectorizer.transform([query])
            
            # Convert to numpy array and reshape for FAISS
            query_array = query_vector.toarray().astype('float32')
            
            # Search in FAISS index
            distances, indices = self.index.search(query_array, top_k)
            
            # Get results
            results = []
            for i, (distance, idx) in enumerate(zip(distances[0], indices[0])):
                if idx < len(self.text_chunks):
                    results.append({
                        'rank': i + 1,
                        'content': self.text_chunks[idx],
                        'similarity_score': float(1 - distance),  # Convert distance to similarity
                        'index': int(idx)
                    })
            
            return {
                'query': query,
                'results': results,
                'total_results': len(results)
            }
            
        except Exception as e:
            return {
                'error': f'Search error: {str(e)}',
                'results': []
            }
    
    def get_answer(self, query):
        """Get a comprehensive answer based on the query"""
        search_results = self.search(query, top_k=3)
        
        if 'error' in search_results:
            return search_results['error']
        
        if not search_results['results']:
            return "I'm sorry, I couldn't find relevant information for your query."
        
        # Combine the top results into a comprehensive answer
        answer_parts = []
        for result in search_results['results']:
            answer_parts.append(result['content'])
        
        # Create a comprehensive answer
        combined_answer = " ".join(answer_parts)
        
        # Clean up the answer (remove excessive whitespace, etc.)
        combined_answer = " ".join(combined_answer.split())
        
        return combined_answer
    
    def is_model_loaded(self):
        """Check if the model is properly loaded"""
        return self.index is not None and self.text_chunks is not None 