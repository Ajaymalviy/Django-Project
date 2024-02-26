from django.urls import include, path
from appointment_system.views import  list_documents  # Import your view
from mysite import urls as mysite_urls

urlpatterns = [
    # other URL patterns
    path('', include(mysite_urls)),
]

# urlpatterns = [
#     path('hello/', hello_world, name='hello_world'),
# ]


urlpatterns = [
    path('list_documents/', list_documents, name='list_documents'),
]
from django.urls import path
from appointment_system.views import index

urlpatterns = [
    path('', index, name='index'),
]
