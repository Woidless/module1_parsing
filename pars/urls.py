from django.urls import path, re_path

from . import views, parsing


urlpatterns = [
    path('api/v1/list/', views.HotelViewSet.as_view({'get':'list'})),
    path('parsing/', parsing.parsing_of_website, name='parsing'),
]
