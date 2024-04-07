from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  

from .models import SavedProduct, SavedService, SavedEvent
from .serializer import SavedProductSerializer, SavedServiceSerializer, SavedEventSerializer

class SavedProductList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        saved_product = SavedProduct.objects.filter(user=request.user)
        serializer = SavedProductSerializer(saved_product, many=True)
        return Response(serializer.data)

class SavedProductDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        try:
            saved_product = SavedProduct.objects.get(user=request.user, item_id=item_id)
            serializer = SavedProductSerializer(saved_product)
            return Response(serializer.data)
        except saved_product.DoesNotExist:
            return Response({'message': 'Saved item not found'}, status=404)

class SaveProduct(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SavedProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400)  




#services
class SavedServiceList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        saved_service = SavedService.objects.filter(user=request.user)
        serializer = SavedServiceSerializer(saved_service, many=True)
        return Response(serializer.data)

class SavedServiceDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        try:
            saved_service = SavedService.objects.get(user=request.user, item_id=item_id)
            serializer = SavedServiceSerializer(saved_service)
            return Response(serializer.data)
        except SavedService.DoesNotExist:
            return Response({'message': 'Saved service not found'}, status=404)

class SaveService(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SavedServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400)  




    
#events
class SavedEventList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        saved_event = SavedEvent.objects.filter(user=request.user)
        serializer = SavedEventSerializer(saved_event, many=True)
        return Response(serializer.data)

class SavedEventDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id, ):
        try:
            saved_event = SavedEvent.objects.get(user=request.user, item_id=item_id)
            serializer = SavedEventSerializer(saved_event)
            return Response(serializer.data)
        except SavedEvent.DoesNotExist:
            return Response({'message': 'Saved event not found'}, status=404)

class SaveEvent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SavedEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400)
