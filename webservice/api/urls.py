from django.urls import path, include

urlpatterns = [
    path('admin/', include('api.admin.urls')),
    path('frontend/', include('api.frontend.urls'))
]
