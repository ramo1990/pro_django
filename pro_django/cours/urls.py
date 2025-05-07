from django.urls import path
from .views import CoursListView, CoursDetailView, CoursCreateView, CoursUpdateView, CoursDeleteView

app_name = 'cours'
urlpatterns = [
    path('list/', CoursListView.as_view(), name='cours-list'),
    path('detail/<int:pk>/', CoursDetailView.as_view(), name='cours-detail'),
    path('create/', CoursCreateView.as_view(), name='cours-create'),
    path('update/<int:pk>', CoursUpdateView.as_view(), name='cours-update'),
    path('delete/<int:pk>', CoursDeleteView.as_view(), name='cours-delete'),
]