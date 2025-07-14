from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from .ml_model import AgriBotModel
from .models import Query

# Initialize the model globally
agri_bot_model = AgriBotModel()


@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    model_status = agri_bot_model.is_model_loaded()
    return Response({
        'status': 'healthy',
        'model_loaded': model_status,
        'message': 'AgriBot API is running'
    })


@api_view(['POST'])
def ask_question(request):
    """API endpoint to ask questions to the agri bot"""
    try:
        data = request.data
        question = data.get('question', '').strip()
        
        if not question:
            return Response({
                'error': 'Question is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Get answer from the model
        answer = agri_bot_model.get_answer(question)
        
        # Save to database
        Query.objects.create(
            query_text=question,
            response_text=answer
        )
        
        return Response({
            'question': question,
            'answer': answer,
            'model_loaded': agri_bot_model.is_model_loaded()
        })
        
    except Exception as e:
        return Response({
            'error': f'An error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def search_content(request):
    """API endpoint to search for similar content"""
    try:
        data = request.data
        query = data.get('query', '').strip()
        top_k = data.get('top_k', 5)
        
        if not query:
            return Response({
                'error': 'Query is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Search using the model
        results = agri_bot_model.search(query, top_k=top_k)
        
        return Response(results)
        
    except Exception as e:
        return Response({
            'error': f'An error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_history(request):
    """API endpoint to get query history"""
    try:
        queries = Query.objects.all()[:20]  # Get last 20 queries
        
        history = []
        for query in queries:
            history.append({
                'id': query.id,
                'question': query.query_text,
                'answer': query.response_text,
                'created_at': query.created_at.isoformat()
            })
        
        return Response({
            'history': history,
            'total_count': len(history)
        })
        
    except Exception as e:
        return Response({
            'error': f'An error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def model_info(request):
    """API endpoint to get model information"""
    try:
        model_loaded = agri_bot_model.is_model_loaded()
        
        info = {
            'model_loaded': model_loaded,
            'model_type': 'FAISS Vector Search',
            'description': 'Agricultural knowledge base with semantic search capabilities'
        }
        
        if model_loaded and agri_bot_model.text_chunks:
            info['total_documents'] = len(agri_bot_model.text_chunks)
            info['index_size'] = agri_bot_model.index.ntotal if agri_bot_model.index else 0
        
        return Response(info)
        
    except Exception as e:
        return Response({
            'error': f'An error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 