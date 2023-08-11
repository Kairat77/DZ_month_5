from . import views
from django.urls import path
urlpatterns = [
    path('', views.director_view),
    path('<int:id>/',views.director_id_view),
    path('',views.movies_view),
    path('<int:id>/',views.movies_id_view),
    path('',views.review_view),
    path('<int:id>/',views.review_id_view)
]
