from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MathOperationSerializer
from .tasks import calculate_factorial


class MathOperationsView(APIView):
    def get(self, request):
        return Response({"allowed_operations": ["factorial",]})

    def post(self, request):
        serializer = MathOperationSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            if valid_data.get('operation').lower() == 'factorial':
                calculate_factorial.delay(int(valid_data.get('data')))
                return Response()
        else:
            return Response({"error": serializer.errors})
