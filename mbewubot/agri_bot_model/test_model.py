import os
import pickle
import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class AgriBotTester:
    """Test class for the agricultural bot model"""
    
    def __init__(self, model_dir="C:\\Users\\MARTY\\agri_bot_model"):
        self.model_dir = model_dir
        self.index = None
        self.text_chunks = None
        self.vectorizer = None
        self._load_model()
    
    def _load_model(self):
        """Load the FAISS index and text chunks"""
        try:
            # Load FAISS index
            index_path = os.path.join(self.model_dir, 'faiss_index.index')
            print(f"Loading FAISS index from: {index_path}")
            self.index = faiss.read_index(index_path)
            print(f"✓ FAISS index loaded successfully! Index size: {self.index.ntotal}")
            
            # Load text chunks
            chunks_path = os.path.join(self.model_dir, 'text_chunks.pkl')
            print(f"Loading text chunks from: {chunks_path}")
            with open(chunks_path, 'rb') as f:
                self.text_chunks = pickle.load(f)
            print(f"✓ Text chunks loaded successfully! Total chunks: {len(self.text_chunks)}")
            
            # Initialize TF-IDF vectorizer for query processing
            print("Initializing TF-IDF vectorizer...")
            self.vectorizer = TfidfVectorizer(
                max_features=1000,
                stop_words='english',
                ngram_range=(1, 2)
            )
            
            # Fit the vectorizer on the text chunks
            if self.text_chunks:
                self.vectorizer.fit(self.text_chunks)
                print("✓ TF-IDF vectorizer fitted successfully!")
                
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            self.index = None
            self.text_chunks = None
            self.vectorizer = None
    
    def search(self, query, top_k=5):
        """Search for similar content based on the query"""
        if not self.index or not self.text_chunks or not self.vectorizer:
            print("❌ Model not loaded properly")
            return None
        
        try:
            print(f"🔍 Searching for: '{query}'")
            
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
            
            return results
            
        except Exception as e:
            print(f"❌ Search error: {str(e)}")
            return None
    
    def get_answer(self, query):
        """Get a comprehensive answer based on the query"""
        search_results = self.search(query, top_k=3)
        
        if not search_results:
            return "I'm sorry, I couldn't find relevant information for your query."
        
        # Combine the top results into a comprehensive answer
        answer_parts = []
        for result in search_results:
            answer_parts.append(result['content'])
        
        # Create a comprehensive answer
        combined_answer = " ".join(answer_parts)
        
        # Clean up the answer (remove excessive whitespace, etc.)
        combined_answer = " ".join(combined_answer.split())
        
        return combined_answer
    
    def is_model_loaded(self):
        """Check if the model is properly loaded"""
        return self.index is not None and self.text_chunks is not None
    
    def print_model_info(self):
        """Print information about the loaded model"""
        print("=" * 50)
        print("🤖 AGRICULTURAL BOT MODEL INFO")
        print("=" * 50)
        
        if self.is_model_loaded():
            print(f"✅ Model Status: LOADED")
            print(f"📊 FAISS Index Size: {self.index.ntotal}")
            print(f"📝 Total Text Chunks: {len(self.text_chunks)}")
            print(f"🔧 Vectorizer Features: {self.vectorizer.get_feature_names_out().shape[0]}")
            
            # Show some sample text chunks
            print(f"\n📖 Sample Text Chunks:")
            for i, chunk in enumerate(self.text_chunks[:3]):
                print(f"  {i+1}. {chunk[:100]}...")
                
        else:
            print("❌ Model Status: NOT LOADED")
        
        print("=" * 50)

# Test function
def test_agri_bot():
    """Main test function"""
    print("🚀 Starting AgriBot Model Test...")
    
    # Initialize the tester
    tester = AgriBotTester()
    
    # Print model info
    tester.print_model_info()
    
    if not tester.is_model_loaded():
        print("❌ Model failed to load. Please check your file paths.")
        return
    
    # Test some sample queries
    test_queries = [
        "What is organic farming?",
        "How to grow tomatoes?",
        "Pest control methods",
        "Soil preparation",
        "Crop rotation benefits"
    ]
    
    print(f"\n🧪 Testing {len(test_queries)} sample queries...")
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Test {i}: '{query}' ---")
        
        # Get search results
        results = tester.search(query, top_k=3)
        
        if results:
            print(f"✅ Found {len(results)} results:")
            for j, result in enumerate(results, 1):
                print(f"  {j}. Score: {result['similarity_score']:.3f}")
                print(f"     Content: {result['content'][:100]}...")
        else:
            print("❌ No results found")
        
        # Get comprehensive answer
        answer = tester.get_answer(query)
        print(f"🤖 Answer: {answer[:200]}...")
    
    print(f"\n🎉 Test completed successfully!")

# Run the test if this script is executed directly
if __name__ == "__main__":
    test_agri_bot() 