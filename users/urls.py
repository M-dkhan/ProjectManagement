from django.urls import path
from .views import sign_up, form

urlpatterns = [
    path('signup/', sign_up, name="sign-up"),
    path('form/', form, name='form')
]
