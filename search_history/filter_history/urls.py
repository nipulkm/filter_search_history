from django.urls import path
from filter_history import views

urlpatterns = [
	path('history/', views.history, name='history'),
	#path('history/filter', views.history, name='history')
]
