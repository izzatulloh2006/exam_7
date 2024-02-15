from django.urls import path
from .views import UserList, DeleteUser , user_list
from apps.utils import send_email
from django.http import HttpResponse


def send_email_task(req):
    return HttpResponse(send_email('Xabar', 'Izzatulloh', ['fayzullaxojaevi@gmail.com']).get('message'))



urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('delete/<int:user_id>/', DeleteUser, name='delete_user'),
    path('users/', user_list, name='user_list'),
]








