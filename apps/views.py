from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.core.paginator import Paginator

class UserList(ListView):
    model = User
    template_name = 'base.html'


class AddUser(CreateView):
    model = User
    fields = ['rasm', 'username', 'first_name', 'last_name', 'description', 'email', 'website']
    success_url = '/users/'


def DeleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, "Sizning malumotlaringiz o'chirildi")
    return redirect('delete_user')


def user_list(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 10)  # Show 10 users per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user_list.html', {'page_obj': page_obj})





