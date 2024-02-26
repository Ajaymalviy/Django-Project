from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

######------for listing documents of collection --------------
from django.http import JsonResponse
from appointment_system.models import Company  # Import your Django model
from bson import json_util  # Import BSON to JSON converter

def list_documents(request):
    # Fetch all documents from the MongoDB collection
    documents = Company.objects.all().values()

    # Convert queryset to list of dictionaries
    documents_list = list(documents)
    print(documents_list)

    # Serialize the data into JSON format
    serialized_data = json_util.dumps(documents_list)
    print(documents_list)

    # Return JSON response
    return JsonResponse(serialized_data, safe=False)
