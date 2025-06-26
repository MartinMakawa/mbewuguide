import json
import numpy as np
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from joblib import load
from .expert_logic import get_crop_guidance


from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    role = request.data.get("role")  # Optional

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    user.save()

    return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)


model = load('crops/crop_model_v1.pkl')  # adjust path if needed

@csrf_exempt
def crop_recommendation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            features = np.array([
                data['N'], data['P'], data['K'],
                data['temperature'], data['humidity'],
                data['ph'], data['rainfall']
            ]).reshape(1, -1)

            prediction = model.predict_proba(features)[0]
            top_indices = np.argsort(prediction)[::-1][:3]

            class_names = model.classes_
            top_crops = [
                {
                    "crop": class_names[i],
                    "probability": round(float(prediction[i]), 2),
                    "expert_info": get_crop_guidance(class_names[i])
                }
                for i in top_indices
            ]
            return JsonResponse({"recommendations": top_crops})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Only POST requests allowed."})
