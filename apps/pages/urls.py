from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.pages_index_view,name='home')
]