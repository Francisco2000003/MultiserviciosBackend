# backend/urls.py  (o tu urls principal)
from django.urls import path
from correos.views import ContactAPIView

urlpatterns = [
    # ...
    path("contacto/", ContactAPIView.as_view(), name="api-contacto"),
]
