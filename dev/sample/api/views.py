from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import HelloWorldSerializer, PersonSerializer, MathOperationSerializer
from .models import Person
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
"""
Django API creation method 1: 
Create an API using function based APIView.
    - create a function with api_view decorator
    - check request.method to get the HTTP verb
    - add as view to urls.py
"""
@api_view(["GET", "POST"])
def vista_de_el_hola_mundo(request):
    if request.method == "GET":
        return Response({"mensaje": "¡Hola! mundo."})
    else:
        nombre = request.data.get("nombre")
        if not nombre:
            return Response({"error": "Falta el nombre"})
        return Response({"mensaje": "¡Hola! {}. ¿Como estás?".format(nombre)})

"""
Django API creation method 2: 
Create an API by extending APIView.
    - extend APIView class
    - override methods such as get, post etc. and add own implementation
    - add as view to urls.py
"""
class NamasteVishwaKaDrishya(APIView):
    def get(self, request):
        return Response({"message": "Namaste Viwhwa!"}, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        naam = request.data.get('naam')
        if not naam:
            return Response({"error": "Naam gayab hain."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"sandesh": "Namaste {}! Kaise ho?".format(naam)})

"""
Django API creation method 3: 
Create an API by extending APIView and using serializer.
    - extend APIView class
    - override methods such as get, post etc. and add own implementation
    - add as view to urls.py
"""
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"}, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        serializer = HelloWorldSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data

            name = valid_data.get('name')
            age = valid_data.get('age')

            if age:
                return Response({"message": "Hello {}, you're {} years old.".format(name, age)})
            else:
                return Response({"message": "Hello {}, we don't know your age.".format(name)})
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        if not name:
            return Response({"error": "Name missing"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Hello {}! How are you?".format(name)})


"""
Django API creation method 4:
Create an API by extending APIView and using serializers and models.
Serializer is created by extending serializers.Serializer
"""
class PersonView(APIView):
    def get(self, request):
        people = Person.objects.all()
        serialized_people = PersonSerializer(people, many=True)
        return Response(serialized_people.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            person_instance = Person.objects.create(**serializer.data)
            return Response({"message": "Created person with id {}".format(person_instance.id)})
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
