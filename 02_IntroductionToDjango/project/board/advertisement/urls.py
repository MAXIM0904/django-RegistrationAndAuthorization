from django.urls import path
from .import views


urlpatterns = [
    path("", views.advertisement_list, name="advertisement_list"),
    path("advertisement_list", views.advertisement_list, name="advertisement_list"),
    path("skill_1C", views.skill_1C, name="skill_1C"),
    path("skill_data_scientist", views.skill_data_scientist, name="skill_data_scientist"),
    path("skill_graphic", views.skill_graphic, name="skill_graphic"),
    path("skill_java", views.skill_java, name="skill_java"),
    path("skill_python", views.skill_python, name="skill_python")
]