from django.urls import path
from crudapp import views

urlpatterns = [
    path('guide/', views.guide_list.as_view()),
    path('guide/<int:pk>/', views.guide_list_details.as_view()),
    path('destination/',views.destinations_list,name='destinations_list'),
    path('destination/<int:pk>/',views.list_by_id,name='list_by_id'),
    path('post/',views.post_destinations,name='post_destinations'),
    path('update/<int:pk>/',views.update_destinations,name='update_destinations'),
]