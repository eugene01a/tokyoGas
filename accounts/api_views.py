from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from .models import Pref


class UserRegistrationAPIView(APIView):
    # API endpoint to register a user via JSON payload.
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Registration complete.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrefListAPIView(APIView):
    # Return target metadata for frontend pref dropdowns.
    def get(self, request, *args, **kwargs):
        prefs = Pref.objects.order_by('name').values('id', 'name')
        return Response(list(prefs), status=status.HTTP_200_OK)
