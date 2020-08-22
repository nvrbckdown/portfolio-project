from django.urls import path
from .views import allblog_view


urlpatterns = [
	path('', allblog_view, name='allblog'),
]