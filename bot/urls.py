from .views import cygbotview
from django.conf.urls import url
urlpatterns = [
                url(r'^90293269/?$', cygbotview.as_view())
]
