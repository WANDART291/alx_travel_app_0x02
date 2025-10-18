# alx_travel_app/urls.py (Project-level)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # KEEP THIS LINE
    path('admin/', admin.site.urls),
    
    # 🚨 ADD THIS LINE BACK 🚨
    path('api/listings/', include('listings.urls')), 
]
