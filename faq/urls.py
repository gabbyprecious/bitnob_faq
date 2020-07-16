from django.urls import path, include
from faq import views


urlpatterns = [
    path("faq/", views.faq_list),
    path("faq/<int:pk>/", views.faq),
    path("search/<str:keyword>/", views.search),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
