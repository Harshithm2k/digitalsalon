from django.shortcuts import render, redirect
from adminsapp.models import *
from adminsapp.forms import *
# from customerapp.models import Customer, Booking, Rating
# from salonapp.models import Salons
from customerapp.models import Customer, Booking, Rating
from salonapp.models import Salons


# Create your views here.


# def admins_login(request):
#     if request.method == "POST":
#         fullname = request.POST["fullname"]
#         password = request.POST["password"]
#         request.session["fullname"] = fullname
#         try:
#             print("hi")
#             admin = Admins.objects.get(fullname=fullname, password=password)
#             print(admin.errors)
#             msg = "data found"
#             return render(request, "admins_home.html", {"admin": admin, "msg": msg})
#         except:
#             msg = "invalid data"
#             return render(request, "admins_login.html", {"msg": msg})
#     return render(request, "admins_login.html", {})


def is_admin_login(request):
    if request.session.__contains__("fullname"):
        return True
    else:
        return False


def admins_login(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        password = request.POST['password']
        print(fullname, " ", password)
        administration = Admins.objects.filter(fullname=fullname, password=password)
        if administration.exists():
            print("hello")
            request.session["fullname"] = fullname
            return render(request, "admins_home.html", {"msg": fullname})

        else:
            return render(request, "admins_login.html", {"msg": "fullname or password not exist"})
    return render(request, "admins_login.html", {"msg": ""})


def admins_home(request):
    return render(request, "admins_home.html", {})


def admins_logout(request):
    request.session['fullname'] = ''
    del request.session["fullname"]
    return render(request, "admins_login.html", {})


def is_login(request):
    if request.session.__contains__("fullname"):
        return True
    else:
        return False


def admins_change_password(request):
    if is_login(request):
        if request.method == "POST":
            fullname = request.session['fullname']
            password = request.POST['password']
            new_password = request.POST['new_password']
            try:
                admins = Admins.objects.get(fullname=fullname, password=password)
                admins.password = new_password
                admins.save()
                msg = "success fully change your password"
                return render(request, "admins_login.html", {"msg": msg})
            except:
                msg = "invalid data"
                return render(request, "admins_change_password.html", {"msg": msg})
        return render(request, "admins_change_password.html", {})
    else:
        return render(request, "admins_login.html", {})


def admins_customer_display(request):
    customers = Customer.objects.all()
    return render(request, "admins_customer_display.html", {"customers": customers})


def admins_salon_display(request):
    salons = Salons.objects.all()
    return render(request, "admins_salon_display.html", {"salons": salons})


def admins_salon_delete(request, id):
    salon = Salons.objects.get(id=id)
    salon.delete()
    return redirect("/admins_salon_display")


def admins_customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/admins_customer_display")


def admins_salon_booking_display(request):
    books = Booking.objects.all()
    return render(request, "admins_salon_booking_display.html", {"books": books})


def admins_salon_rating_display(request):
    ratings = Rating.objects.all()
    return render(request, "admin_salon_rating_display.html", {"ratings": ratings})
