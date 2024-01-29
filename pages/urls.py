from django.urls import path
from pages.views import home_pages_views, create_email_view

app_name = 'pages'

urlpatterns = [
    path('email/', create_email_view, name='create_email'),
    path('', home_pages_views)
]