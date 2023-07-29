from os import set_handle_inheritable

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
from datetime import date
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html',locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalservices = Services.objects.all().count()
    totalunread = Contact.objects.filter(isread="no").count()
    totalread = Contact.objects.filter(isread="yes").count()
    totalnewbooking = SiteUser.objects.filter(status=None).count()
    totaloldbooking = SiteUser.objects.filter(status="1").count()
    return render(request, 'admin_home.html',locals())

def add_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        st = request.POST['servicetitle']
        des = request.POST['description']
        image = request.FILES['image']
        try:
            Services.objects.create(title=st,description=des,image=image)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_services.html', d)

def manage_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.all()
    return render(request, 'manage_services.html', locals())

def edit_service(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.get(id=pid)
    error = ""
    if request.method=="POST":
        title = request.POST['servicetitle']
        description = request.POST['description']
        service.title = title
        service.description = description
        try:
            service.save()
            error = "no"
        except:
            error = "yes"
        try:
            image = request.FILES['image']
            service.image = image
            service.save()
        except:
            pass
    return render(request, 'edit_service.html', locals())

def delete_service(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.get(id=pid)
    service.delete()
    return redirect('manage_service')

def Logout(request):
    logout(request)
    return redirect('index')

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', locals())

def about(request):
    return render(request, 'about.html', locals())


def request_quote(request):
    error = ""
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        loc = request.POST['location']
        shiftloc = request.POST['shiftingloc']
        shiftdate = request.POST['shiftingdate']
        briefitems = request.POST['briefitems']
        items = request.POST['items']


        try:
            SiteUser.objects.create(name=name,email=email,mobile=contact,location=loc,shiftingloc=shiftloc,shiftingdate=shiftdate,briefitems=briefitems,items=items,requestdate=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request, 'request_quote.html',locals())

def new_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.filter(status=None)
    return render(request, 'new_booking.html', locals())

def view_bookingdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        remark = request.POST['remark']
        try:
            booking.remark = remark
            booking.status = "1"
            booking.updationdate = date.today()
            booking.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'view_bookingdetail.html', locals())

def old_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking = SiteUser.objects.filter(status="1")
    return render(request, 'old_booking.html', locals())

def contact(request):
    if request.method == 'POST':
        n = request.POST['fullname']
        cont = request.POST['contact']
        e = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        try:
            Contact.objects.create(name=n, contact=cont, emailid=e,subject=sub, message=msg, mdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())


def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(isread="no")
    return render(request, 'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(isread="yes")
    return render(request, 'read_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request, 'view_queries.html',locals())

def delete_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.get(id=pid)
    contact.delete()
    return redirect('read_queries')

def search(request):
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
    try:
        booking = SiteUser.objects.filter(Q(name=sd)|Q(mobile=sd))
        #bookingcount = SiteUser.objects.filter(Q(name=sd)|Q(contact=sd)).count()
    except:
        booking = ""

    return render(request, 'search.html',locals())

def betweendate_bookingreport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        booking = SiteUser.objects.filter(Q(requestdate__gte=fd) & Q(requestdate__lte=td))
        return render(request, 'bookingbtwdates.html', locals())
    return render(request, 'betweendate_bookingreport.html')

def betweendate_contactreport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        contact = Contact.objects.filter(Q(mdate__gte=fd) & Q(mdate__lte=td))
        return render(request, 'contactbtwdates.html', locals())
    return render(request, 'betweendate_contactreport.html')


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"

    return render(request,'change_passwordadmin.html',locals())
