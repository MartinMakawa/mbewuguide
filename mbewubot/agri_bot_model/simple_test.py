#!/usr/bin/env python3
"""
Simple test script for the Agricultural Bot Model
Run this script to test your FAISS model and text chunks
"""

import os
import pickle
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

def test_model():
    """Test the agricultural bot model"""
    
    # Model directory
    model_dir = r"C:\Users\MARTY\agri_bot_model"
    
    print("🚀 Testing Agricultural Bot Model")
    print("=" * 50)
    
    try:
        # Check if files exist
        index_path = os.path.join(model_dir, 'faiss_index.index')
        chunks_path = os.path.join(model_dir, 'text_chunks.pkl')
        
        print(f"Checking files in: {model_dir}")
        print(f"FAISS index exists: {os.path.exists(index_path)}")
        print(f"Text chunks exists: {os.path.exists(chunks_path)}")
        
        if not os.path.exists(index_path) or not os.path.exists(chunks_path):
            print("❌ Model files not found!")
            return
        
        # Load FAISS index
        print("\n📊 Loading FAISS index...")
        index = faiss.read_index(index_path)
        print(f"✅ FAISS index loaded! Size: {index.ntotal}")
        
        # Load text chunks
        print("\n📝 Loading text chunks...")
        with open(chunks_path, 'rb') as f:
            text_chunks = pickle.load(f)
        print(f"✅ Text chunks loaded! Count: {len(text_chunks)}")
        
        # Show sample chunks
        print(f"\n📖 Sample text chunks:")
        for i, chunk in enumerate(text_chunks[:3]):
            print(f"  {i+1}. {chunk[:100]}...")
        
        # Initialize vectorizer
        print(f"\n🔧 Initializing TF-IDF vectorizer...")
        vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2)
        )
        
        # Fit vectorizer
        vectorizer.fit(text_chunks)
        print(f"✅ Vectorizer fitted! Features: {len(vectorizer.get_feature_names_out())}")
        
        # Test a simple query
        print(f"\n🧪 Testing sample query...")
        test_query = "organic farming"
        
        # Vectorize query
        query_vector = vectorizer.transform([test_query])
        query_array = query_vector.toarray().astype('float32')
        
        # Search
        distances, indices = index.search(query_array, 3)
        
        print(f"Query: '{test_query}'")
        print(f"Found {len(indices[0])} results:")
        
        for i, (distance, idx) in enumerate(zip(distances[0], indices[0])):
            if idx < len(text_chunks):
                similarity = 1 - distance
                print(f"  {i+1}. Score: {similarity:.3f}")
                print(f"     Content: {text_chunks[idx][:100]}...")
        
        print(f"\n🎉 Model test completed successfully!")
        print(f"✅ Your agricultural bot model is working!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_model() 