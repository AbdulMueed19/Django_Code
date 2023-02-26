from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("flights/", include("flights.urls")),
    path('Hello/', include('Hello.urls')),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('authentication/', include('authentication.urls')),

]

