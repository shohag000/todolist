from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import List
from django.http import JsonResponse
from .forms import UserLoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def get_login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user = form.cleaned_data.get("user")
        login(request,user)
        return redirect("list")
    return render(request,"login.html",{"form":form})


@login_required(login_url="/todo/login")
def todolist_view(request):
    list = List.objects.filter(user=request.user,is_checked=False).order_by('-id')
    context = {
        "object_list" : list,
    }
    return render(request,"list.html",context)


@login_required(login_url="/todo/login")
def add_task(request):
    user = request.user
    if request.POST:
        description = request.POST.get("disc")
        List.objects.create(user=user,description=description)
    return redirect("/todo/")


@login_required(login_url="/todo/login")
def make_complete(request):
    if request.GET:
        id = request.GET.get('id')
        todolist = List.objects.get(id=id)
        todolist.is_completed=True
        todolist.save()
        data = {
            "msg" : "successfully checked as complete",
        }
        return JsonResponse(data)
    return redirect("index")


@login_required(login_url="/todo/login")
def make_uncomplete(request):
    if request.GET:
        id = request.GET.get('id')
        todolist = List.objects.get(id=id)
        todolist.is_completed=False
        todolist.save()
        data = {
            "msg" : "successfully  checked as uncomplete",
        }
        return JsonResponse(data)
    return redirect("index")


@login_required(login_url="/todo/login")
def remove_completed_task(request):
    List.objects.filter(is_completed=True,is_checked=False).update(is_checked=True)
    return redirect("/todo/")


@login_required(login_url="/todo/login")
def delete_task(request):
    if request.GET:
        id = request.GET.get('id')
        List.objects.get(id=id).delete()

        data = {
            "msg": "successfully deleted  task",
        }
        return JsonResponse(data)

    return redirect("index")


@login_required(login_url="/todo/login")
def edit_task(request):
    if request.GET:
        list_id = request.GET.get("id")
        description = request.GET.get("description")

        list = List.objects.get(id=list_id)
        list.description=description
        list.save()

        data = {
            "msg": "successfully edited  task",
        }
        return JsonResponse(data)
    return redirect("index")
