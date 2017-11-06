from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GenerateRandomUserFormView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomUserForm

    # def form_valid(self, form):
    #     print(form)
    #     total = form.cleaned_data.get('total')
    #     create_random_user_accounts.delay(total)
    #     messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
    #     return redirect('users_list')

class GenerateRandomUserView(APIView):

    def post(self, request, format=None):
        print(request)
        total = request.data.get('total')
        create_random_user_accounts.delay(total)
        # messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        message = {}
        message["a"] = "succsess"
        Response(message, status=status.HTTP_201_CREATED)