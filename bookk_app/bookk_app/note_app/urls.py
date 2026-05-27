from django.urls import path
from .views import home_page,contact_page,profile_page,grades,add_user
urlpatterns = [
    path("home_page",home_page),
    path("contact_page",contact_page),
    path("profile_page",profile_page),
    path("grade/<int:marks>",grades),
    path("user_form",add_user),
]