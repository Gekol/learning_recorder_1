from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.base import View

def register(request):
    if request.method != "POST":
        form = UserCreateForm()
    else:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST["password1"])
            login(request, authenticated_user)
            return HttpResponseRedirect("/problems")
    return render(request, "register.html", {"form": form})

class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "register.html"

    success_url = "/problems"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")