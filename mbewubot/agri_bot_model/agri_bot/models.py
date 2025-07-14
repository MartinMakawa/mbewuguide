from django.db import models


class Query(models.Model):
    """Model to store user queries and responses"""
    query_text = models.TextField()
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Query: {self.query_text[:50]}..." 