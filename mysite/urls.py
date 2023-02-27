"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from skill.api.router import router as skill_router
from project.api.router import router as project_router
from experience.api.router import router as experience_router
from education.api.router import router as education_router
from contact.api.router import router as contact_router
from blog.api.router import router as blog_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(skill_router.urls)),
    path("api/", include(project_router.urls)),
    path("api/", include(experience_router.urls)),
    path("api/", include(education_router.urls)),
    path("api/", include(contact_router.urls)),
    path("api/", include(blog_router.urls)),
]
