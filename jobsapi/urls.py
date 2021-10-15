from django.urls import path
from .views import Joblist, JobDetailView

urlpatterns = [
    path('', Joblist.as_view()),
    path('<int:id>/', JobDetailView.as_view()),
]