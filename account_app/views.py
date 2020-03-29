from django.contrib import auth
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from account_app import models
import time
import json
import base64
from django.http import FileResponse
from django.http import JsonResponse
from .mailSender import *
from .activeInfo import *
from django.db.models import Q

import datetime
from dwebsocket.decorators import accept_websocket

import shutil
import os

# Create your views here.
from django.shortcuts import render,HttpResponse

def testwebsocket(request):
    return render(request,'testwebsocket.html')

def datasetlink(request):
    #2012份数据
    date_from1 = datetime.date(2012, 1, 1)
    date_to1 = datetime.date(2012, 12, 30)
    list1 = models.Employee.objects.filter(hire_date__range=(date_from1, date_to1),gender=0).all()
    list1n = len(list1)
    print(list1n)
    list2 = models.Employee.objects.filter(hire_date__range=(date_from1, date_to1),gender=1).all()
    list2n = len(list2)
    print(list2n)
    list3 = models.Employee.objects.filter(resign_date__range=(date_from1, date_to1),gender=0).all()
    list3n = len(list3)
    print(list3n)
    list4 = models.Employee.objects.filter(resign_date__range=(date_from1, date_to1),gender=1).all()
    list4n = len(list4)
    print(list4n)

    #2013年份数据
    date_from2 = datetime.date(2013, 1, 1)
    date_to2 = datetime.date(2013, 12, 30)
    list1a = models.Employee.objects.filter(hire_date__range=(date_from2, date_to2),gender=0).all()
    list1na = len(list1a)
    print(list1na)
    list2a = models.Employee.objects.filter(hire_date__range=(date_from2, date_to2),gender=1).all()
    list2na = len(list2a)
    print(list2na)
    list3a = models.Employee.objects.filter(resign_date__range=(date_from2, date_to2),gender=0).all()
    list3na = len(list3a)
    print(list3na)
    list4a = models.Employee.objects.filter(resign_date__range=(date_from2, date_to2),gender=1).all()
    list4na = len(list4a)
    print(list4na)

    #2014年份数据
    date_from3 = datetime.date(2014, 1, 1)
    date_to3 = datetime.date(2014, 12, 30)
    list1b = models.Employee.objects.filter(hire_date__range=(date_from3, date_to3),gender=0).all()
    list1nb = len(list1b)
    print(list1nb)
    list2b = models.Employee.objects.filter(hire_date__range=(date_from3, date_to3),gender=1).all()
    list2nb = len(list2b)
    print(list2nb)
    list3b = models.Employee.objects.filter(resign_date__range=(date_from3, date_to3),gender=0).all()
    list3nb = len(list3b)
    print(list3nb)
    list4b = models.Employee.objects.filter(resign_date__range=(date_from3, date_to3),gender=1).all()
    list4nb = len(list4b)
    print(list4nb)

    #2015年份数据
    date_from4 = datetime.date(2015, 1, 1)
    date_to4 = datetime.date(2015, 12, 30)
    list1c = models.Employee.objects.filter(hire_date__range=(date_from4, date_to4),gender=0).all()
    list1nc = len(list1c)
    print(list1nc)
    list2c = models.Employee.objects.filter(hire_date__range=(date_from4, date_to4),gender=1).all()
    list2nc = len(list2c)
    print(list2nc)
    list3c = models.Employee.objects.filter(resign_date__range=(date_from4, date_to4),gender=0).all()
    list3nc = len(list3c)
    print(list3nc)
    list4c = models.Employee.objects.filter(resign_date__range=(date_from4, date_to4),gender=1).all()
    list4nc = len(list4c)
    print(list4nc)

    product=list(['year', '2012', '2013', '2014', '2015'])
    Matcha_Latte=list(['male_hire', list1n, list1na, list1nb, list1nc])
    Milk_Tea=list(['female_hire', list2n, list2na, list2nb, list2nc])
    Cheese_Cocoa=list(['male_resign', list3n, list3na, list3nb, list3nc])
    Walnut_Brownie=list(['female_resign', list4n, list4na, list4nb, list4nc])

    return render(request,'dataset-link.html',{"product":product,"Matcha_Latte":Matcha_Latte,"Milk_Tea":Milk_Tea,"Cheese_Cocoa":Cheese_Cocoa,"Walnut_Brownie": Walnut_Brownie})

def datasetlink_old(request):
    #2012份数据
    date_from1 = datetime.date(2012, 1, 1)
    date_to1 = datetime.date(2012, 12, 30)
    list1 = models.Oldperson.objects.filter(checkin_date__range=(date_from1, date_to1)).all()
    list1n = len(list1)
    print(list1n)
    list4 = models.Oldperson.objects.filter(checkout_date__range=(date_from1, date_to1)).all()
    list4n = len(list4)
    print(list4n)

    #2013年份数据
    date_from2 = datetime.date(2013, 1, 1)
    date_to2 = datetime.date(2013, 12, 30)
    list1a = models.Oldperson.objects.filter(checkin_date__range=(date_from2, date_to2)).all()
    list1na = len(list1a)
    print(list1na)
    list4a = models.Oldperson.objects.filter(checkout_date__range=(date_from2, date_to2)).all()
    list4na = len(list4a)
    print(list4na)

    #2014年份数据
    date_from3 = datetime.date(2014, 1, 1)
    date_to3 = datetime.date(2014, 12, 30)
    list1b = models.Oldperson.objects.filter(checkin_date__range=(date_from3, date_to3)).all()
    list1nb = len(list1b)
    print(list1nb)
    list4b = models.Oldperson.objects.filter(checkout_date__range=(date_from3, date_to3)).all()
    list4nb = len(list4b)
    print(list4nb)

    #2015年份数据
    date_from4 = datetime.date(2015, 1, 1)
    date_to4 = datetime.date(2015, 12, 30)
    list1c = models.Oldperson.objects.filter(checkin_date__range=(date_from4, date_to4)).all()
    list1nc = len(list1c)
    print(list1nc)
    list4c = models.Oldperson.objects.filter(checkout_date__range=(date_from4, date_to4)).all()
    list4nc = len(list4c)
    print(list4nc)

    product=list(['year', '2012', '2013', '2014', '2015'])
    Matcha_Latte=list(['male_checkin', list1n, list1na, list1nb, list1nc])
    Walnut_Brownie=list(['female_checkout', list4n, list4na, list4nb, list4nc])

    return render(request,'dataset-link-old.html',{"product":product,"Matcha_Latte":Matcha_Latte,"Walnut_Brownie": Walnut_Brownie})

def datasetlink_vol(request):
    #2012份数据
    date_from1 = datetime.date(2012, 1, 1)
    date_to1 = datetime.date(2012, 12, 30)
    list1 = models.Volunteer.objects.filter(hire_date__range=(date_from1, date_to1),gender=0).all()
    list1n = len(list1)
    print(list1n)
    list2 = models.Volunteer.objects.filter(hire_date__range=(date_from1, date_to1),gender=1).all()
    list2n = len(list2)
    print(list2n)
    list3 = models.Volunteer.objects.filter(resign_date__range=(date_from1, date_to1),gender=0).all()
    list3n = len(list3)
    print(list3n)
    list4 = models.Volunteer.objects.filter(resign_date__range=(date_from1, date_to1),gender=1).all()
    list4n = len(list4)
    print(list4n)

    #2013年份数据
    date_from2 = datetime.date(2013, 1, 1)
    date_to2 = datetime.date(2013, 12, 30)
    list1a = models.Volunteer.objects.filter(hire_date__range=(date_from2, date_to2),gender=0).all()
    list1na = len(list1a)
    print(list1na)
    list2a = models.Volunteer.objects.filter(hire_date__range=(date_from2, date_to2),gender=1).all()
    list2na = len(list2a)
    print(list2na)
    list3a = models.Volunteer.objects.filter(resign_date__range=(date_from2, date_to2),gender=0).all()
    list3na = len(list3a)
    print(list3na)
    list4a = models.Volunteer.objects.filter(resign_date__range=(date_from2, date_to2),gender=1).all()
    list4na = len(list4a)
    print(list4na)

    #2014年份数据
    date_from3 = datetime.date(2014, 1, 1)
    date_to3 = datetime.date(2014, 12, 30)
    list1b = models.Volunteer.objects.filter(hire_date__range=(date_from3, date_to3),gender=0).all()
    list1nb = len(list1b)
    print(list1nb)
    list2b = models.Volunteer.objects.filter(hire_date__range=(date_from3, date_to3),gender=1).all()
    list2nb = len(list2b)
    print(list2nb)
    list3b = models.Volunteer.objects.filter(resign_date__range=(date_from3, date_to3),gender=0).all()
    list3nb = len(list3b)
    print(list3nb)
    list4b = models.Volunteer.objects.filter(resign_date__range=(date_from3, date_to3),gender=1).all()
    list4nb = len(list4b)
    print(list4nb)


    date_from4 = datetime.date(2015, 1, 1)
    date_to4 = datetime.date(2015, 12, 30)
    list1c = models.Volunteer.objects.filter(hire_date__range=(date_from4, date_to4),gender=0).all()
    list1nc = len(list1c)
    print(list1nc)
    list2c = models.Volunteer.objects.filter(hire_date__range=(date_from4, date_to4),gender=1).all()
    list2nc = len(list2c)
    print(list2nc)
    list3c = models.Volunteer.objects.filter(resign_date__range=(date_from4, date_to4),gender=0).all()
    list3nc = len(list3c)
    print(list3nc)
    list4c = models.Volunteer.objects.filter(resign_date__range=(date_from4, date_to4),gender=1).all()
    list4nc = len(list4c)
    print(list4nc)

    product=list(['year', '2012', '2013', '2014', '2015'])
    Matcha_Latte=list(['male_hire', list1n, list1na, list1nb, list1nc])
    Milk_Tea=list(['female_hire', list2n, list2na, list2nb, list2nc])
    Cheese_Cocoa=list(['male_resign', list3n, list3na, list3nb, list3nc])
    Walnut_Brownie=list(['female_resign', list4n, list4na, list4nb, list4nc])

    return render(request,'dataset-link-vol.html',{"product":product,"Matcha_Latte":Matcha_Latte,"Milk_Tea":Milk_Tea,"Cheese_Cocoa":Cheese_Cocoa,"Walnut_Brownie": Walnut_Brownie})


@accept_websocket
def pathweb(request):
    if request.is_websocket():
        print(1)
        request.websocket.send('下载完成'.encode('utf-8'))

    return render(request, 'dateset-link.html')

@login_required
def loginFaceCheck(request):
    if request.method == "POST" and request.is_ajax():
        user = get_user(request)
        username = user.username
        # 获取base64格式的图片
        faceImage = request.POST.get('faceImg')
        # 提取出base64格式，并进行转换为图片
        index = faceImage.find('base64')
        base64Str = faceImage[index+6:]
        img = base64.b64decode(base64Str)
        # 将文件保存
        backupDate = time.strftime("%Y%m%d_%H%M%S")
        if int(request.POST.get('id')) == 0 :
            fileName =  "static/media/" +username+"_%s.jpg" % (backupDate)
        else:
            fileName = "static/media/" + username+"_%s.jpg" % (backupDate)
        file = open(fileName, 'wb')
        file.write(img)
        file.close()
    return HttpResponse('ok')

@login_required
def camera(request):
    if request.method == "POST":
        return JsonResponse()
    else:
        return render(request, 'camera.html')

def upload(request):
  if request.method == 'POST':
    name = request.POST.get('username')
    avatar = request.FILES.get('avatar')
    models.Upload.objects.create(username=name, avatar=avatar)
    with open(avatar.name,'wb') as f:
      for line in avatar:
        f.write(line)
    return HttpResponse('ok')
  return render(request,'edit.html')


@login_required
def guanli(request):
    if request.method == "POST":
        type = request.POST.get('type')
        user = get_user(request)
        username = user.username
        print(username)
        results = models.MyUser.objects.all()
       # print(results.email)
        employees = []
        for result in results:

            employee = {
                'clientnum': result.email,
                'clientname': result.username,
                'tel': result.created_at,
            }
            employees.append(employee)
        return JsonResponse({'clients':employees})
    else:
        return render(request, 'guanli.html')



@login_required
def xiugai(request):
    if request.method == "POST":
        email = request.POST.get("clientnum")
        username = request.POST.get("clientname")
        oldpass = request.POST.get("oldpass")
        password = request.POST.get("newpass")
        print(username)
        print(email)
        print(oldpass)
        print(password)
        user = models.MyUser.objects.get(email=email)  # 查看用户
        ret = user.check_password(oldpass)
        if ret:
            user.set_password(password)  # 如果正确就给设置一个新密码
            user.username = username
            user.save()  # 保存
            print("success")
            msg = 'success'
            re = auth.authenticate(request, username=email, password=password)
            auth.login(request, re)
            return JsonResponse({'msg': msg})

        else:
             print("false")
             msg = 'false'
             re = auth.authenticate(request, username=email, password=oldpass)
             auth.login(request, re)
             return JsonResponse({'msg': msg})
    else:
        return redirect("guanli")


def home(request):
    user = get_user(request)
    if user.is_anonymous:
        return render(request, 'landing.html')
    else:
        return redirect("manage")


# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            re = models.MyUser.objects.get(email=email)
        except models.MyUser.DoesNotExist:
            res = {'msg': 'fail', 'info': 'email not found.'}
            return HttpResponse(json.dumps(res))
        re = auth.authenticate(request, username=email, password=password)
        if re is None:
            res = {'msg': 'fail', 'info': 'password is invalid.'}
            return HttpResponse(json.dumps(res))
        auth.login(request, re)

        res = {'msg': 'success'}
        return HttpResponse(json.dumps(res))
    return render(request, 'login.html');


def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        try:
            re = models.MyUser.objects.get(email=email)
            res = {'msg': 'fail', 'info': 'email already taken.'}
            return HttpResponse(json.dumps(res))
        except models.MyUser.DoesNotExist:
            try:
                re = models.MyUser.objects.get(username=username)
                res = {'msg': 'fail', 'info': 'username already taken.'}
                return HttpResponse(json.dumps(res))
            except models.MyUser.DoesNotExist:
                user = models.MyUser()
                user.email = email
                user.set_password(password)
                user.username = username
                user.created_at = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                user.save()
                res = {'msg': 'success'}
                return HttpResponse(json.dumps(res))

    return render(request, 'register.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def manage(request):
    user = get_user(request)
    username = user.username
    return render(request, "manage.html", {'username': username})



@login_required
def role(request):
    if request.method == "POST":
        type = request.POST.get('type')
        if type == 'addRole':
            role = request.POST.get('role')
            description = request.POST.get('description')
            try:
                temp = models.Role.objects.get(role=role)
                return JsonResponse({"msg": "fail", "info": "角色名已存在"})
            except models.Role.DoesNotExist:
                newRole = models.Role()
                newRole.role = role
                newRole.description = description
                newRole.save()
                return JsonResponse({"msg": "success"})
        elif type == 'init':
            results = models.Role.objects.all()
            roles = []
            for result in results:
                roles.append({'role': result.role, 'description': result.description,
                              'fun1': result.fun1, 'fun2': result.fun2,
                              'fun3': result.fun3, 'fun4': result.fun4,
                              'fun5': result.fun5, 'fun6': result.fun6,
							  'classfun': result.classfun, 'sportfun': result.sportfun,
                              'gymfun': result.gymfun, 'firstfun': result.firstfun,
                              'secondfun': result.secondfun, 'thirdfun': result.thirdfun
                              })
            return JsonResponse({"roles": roles})
        elif type == 'save':
            dic = {"true": True, 'false': False}
            role = request.POST.get('role')
            fun1 = request.POST.get('fun1')
            fun2 = request.POST.get('fun2')
            fun3 = request.POST.get('fun3')
            fun4 = request.POST.get('fun4')
            fun5 = request.POST.get('fun5')
            fun6 = request.POST.get('fun6')
            classfun = request.POST.get('classfun')
            sportfun = request.POST.get('sportfun')
            gymfun = request.POST.get('gymfun')
            firstfun = request.POST.get('firstfun')
            secondfun = request.POST.get('secondfun')
            thirdfun = request.POST.get('thirdfun')
            role_models = models.Role.objects.get(role=role)
            role_models.fun1 = dic[fun1]
            role_models.fun2 = dic[fun2]
            role_models.fun3 = dic[fun3]
            role_models.fun4 = dic[fun4]
            role_models.fun5 = dic[fun5]
            role_models.fun6 = dic[fun6]
            role_models.classfun = dic[classfun]
            role_models.sportfun = dic[sportfun]
            role_models.gymfun = dic[gymfun]
            role_models.firstfun = dic[firstfun]
            role_models.secondfun = dic[secondfun]
            role_models.thirdfun = dic[thirdfun]
            role_models.save()
            return JsonResponse({"msg": "success"})
        elif type == 'delete':
            role = request.POST.get('role')
            role_models = models.Role.objects.get(role=role)
            role_models.delete()
            return JsonResponse({"msg": "success"})
    else:
        return render(request, 'role.html')

# @login_required
# def user(request):
#     if request.method == "POST":
#         type = request.POST.get('type')
#         if type == "init":
#             results = models.MyUser.objects.all()
#             users = []
#             for result in results:
#                 role = result.role.role if result.role else '无'
#                 users.append({'username': result.username, 'email': result.email, 'role': role})
#             return JsonResponse({"users": users})
#         elif type == "save":
#             username = request.POST.get('username')
#             role = request.POST.get('role')
#             role_models = models.Role.objects.get(role=role)
#             user_models = models.MyUser.objects.get(username=username)
#             user_models.role = role_models
#             user_models.save()
#             return HttpResponse('')
#         elif type == "delete":
#             username = request.POST.get('username')
#             user_models = models.MyUser.objects.get(username=username)
#             user_models.delete()
#             return HttpResponse('')
#     else:
#         results = models.Role.objects.all()
#         roles = []
#         for result in results:
#             roles.append(result.role)
#         return render(request, 'user.html', {'roles': roles})

@login_required
def myField(request):
    if request.method == "POST":
        type = request.POST.get('type')
        if type == "init":
            user_model = models.MyUser.objects.get(username=get_user(request).username)
            results = models.Field.objects.filter(username=user_model)
            fields = []
            for result in results:
                field = {
                    'clientnum': result.fieldnum,
                    'clientname': result.fieldname,
                    'tel': result.category,

                    'addition': result.addition,
                }
                fields.append(field)
            return JsonResponse({'clients':fields})
        if type == "add":
            field = models.Field()
            field.fieldname = request.POST.get("clientname")
            try:
                field_model = models.Field.objects.get(fieldname=request.POST.get("clientname"))
                msg = 'fail'
            except models.Field.DoesNotExist:
                field.category = request.POST.get("tel")

                field.addition = request.POST.get("addition")
                field.username = models.MyUser.objects.get(username=get_user(request).username)
                field.save()
                msg = 'success'
            return JsonResponse({'msg': msg})
        if type == "save":
            fieldnum = request.POST.get("clientnum")
            field = models.Field.objects.get(fieldnum=fieldnum)
            field.category = request.POST.get("tel")

            field.addition = request.POST.get("addition")
            field.save()
            msg = 'success'
            return JsonResponse({'msg': msg})
        if type == "delete":
            field = models.Field.objects.get(fieldnum=request.POST.get("clientnum"))
            field.delete()
            return HttpResponse('')

    return render(request, 'myField.html')

@login_required
def allField(request):
    if request.method == "POST":
        type = request.POST.get('type')
        if type == 'init':
            results = models.Field.objects.all()
            fields=[]
            for result in results:
                field={
                    'clientnum': result.fieldnum,
                    'clientname': result.fieldname,
                    'tel': result.category,

                    'addition': result.addition,
                    'username':result.username.username
                }
                fields.append(field)
            return JsonResponse({"clients":fields})
    return render(request, 'allField.html')

@login_required
def log(request):
    return render(request, 'log.html')

@login_required
def downloadFile(request):
    if request.method == "POST":
        applinum = request.POST.get('contractnum')
        file = models.Application.objects.get(applinum=applinum).file
        file_ = open('media/' + file.name, 'rb')
        response = FileResponse(file_)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="' + file.name + '"'

        return response

@login_required
def news(request):
    if request.method == "POST":
        if(request.POST.get("type")=="delete"):
            message = models.message.objects.get(id=request.POST.get('id'))
            message.delete()
            return HttpResponse('')


@login_required
def myActivity(request):
    if request.method == "POST":
        return JsonResponse()
    else:

        return render(request, 'camera.html')

@login_required
def allActivity(request):
    if request.method == "POST":
        type = request.POST.get('type')
        if type == 'init':
            dic = {'0': '学术类', '1': '体育类', '2': '科技类', '3': '文化类'}

            results = models.Activities.objects.all()
            activities=[]
            for result in results:
                activity={
                    'activityid': result.activityid,
                    'activityname': result.activityname,
                    'activitytype': result.activitytype,
                    'activitytime': result.activitytime,
                    'activitycapacity':result.activitycapacity,
                    'openenrolltime':result.openenrolltime,
                }
                activities.append(activity)
            return JsonResponse({"activities":activities})
        if type == "enroll":
            field = models.Field()
            field.fieldname = request.POST.get("clientname")

            activity = models.Activities.objects.get(activityid=request.POST.get("activityid"))
            try:
                enrollment_model = models.Enrollment.objects.get(activityid=request.POST.get("activityid"))
                msg = 'fail'
            except models.Enrollment.DoesNotExist:
                # enrollment.activityid = models.Activities.objects.get(activityid)
                activity.activitycapacity -= 1
                username = models.MyUser.objects.get(username=get_user(request).username)
                enrollment = models.Enrollment(activityid=activity,username=username)
                enrollment.save()
                activity.save()
                msg = 'success'
            return JsonResponse({'msg': msg})
        if type == "add":
            activity = models.Activities()
            activity.activityname = request.POST.get("activityname")
            try:
                activity_model = models.Activities.objects.get(activityname=request.POST.get("activityname"))
                msg = 'fail'
            except models.Activities.DoesNotExist:
                activity.activitytype = request.POST.get("activitytype")
                activity.activitytime = request.POST.get("activitytime")
                activity.openenrolltime = request.POST.get("openenrolltime")
                activity.activitycapacity = request.POST.get("activitycapacity")

                activity.save()
                msg = 'success'
            return JsonResponse({'msg': msg})
        if type == "save":
            fieldnum = request.POST.get("clientnum")
            field = models.Field.objects.get(fieldnum=fieldnum)
            field.category = request.POST.get("tel")

            field.addition = request.POST.get("addition")
            field.save()
            msg = 'success'
            return JsonResponse({'msg': msg})
    else:
        activities = models.Activities.objects.all()
        res = []
        for activity in activities:
            res.append(activity.activitytype)
        list = []
        [list.append(i) for i in res if not i in list]
        json_ = {'activities': list}
        return render(request, "allActivity.html", json_)
    return render(request, 'allActivity.html')


# @login_required
# def Employee(request):
#     if request.method == "POST":
#         type = request.POST.get('type')
#         if type == "init":
#             results = models.Employee.objects.all()
#             employees = []
#             for result in results:
#                 employee = {
#                     'clientnum': result.id,
#                     'clientname': result.username,
#                     'tel': result.phone,
#                     'id_card': result.id_card,
#                     'birthday': result.birthday,
#                     'hire_date':result.hire_date,
#                     'resign_date': result.resign_date,
#                     'imgset_dir': result.imgset_dir,
#                     'profile_photo': result.profile_photo,
#                     'DESCRIPTION': result.DESCRIPTION,
#                 }
#                 employees.append(employee)
#             return JsonResponse({'clients':employees})
#         if type == "add":
#             employee = models.Employee()
#             employee.username = request.POST.get("clientname")
#             try:
#                 employee_model = models.Employee.objects.get(username=request.POST.get("clientname"))
#                 msg = 'fail'
#             except models.Employee.DoesNotExist:
#                 employee.phone = request.POST.get("tel")
#                 employee.id_card = request.POST.get("id_card")
#                 employee.birthday = request.POST.get("birthday")
#                 employee.hire_date = request.POST.get("hire_date")
#                 employee.resign_date = request.POST.get("resign_date")
#                 employee.imgset_dir = request.POST.get("imgset_dir")
#                 employee.profile_photo = request.POST.get("profile_photo")
#                 employee.DESCRIPTION = request.POST.get("DESCRIPTION")
#                 # employee.CREATED = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#                 employee.save()
#                 msg = 'success'
#             return JsonResponse({'msg': msg})
#         if type == "save":
#             id = request.POST.get("clientnum")
#             employee = models.Employee.objects.get(id = id)
#             employee.username = request.POST.get("clientname")
#             employee.phone = request.POST.get("tel")
#             employee.id_card = request.POST.get("id_card")
#             employee.birthday = request.POST.get("birthday")
#             employee.hire_date = request.POST.get("hire_date")
#             employee.resign_date = request.POST.get("resign_date")
#             employee.imgset_dir = request.POST.get("imgset_dir")
#             employee.profile_photo = request.POST.get("profile_photo")
#             employee.DESCRIPTION = request.POST.get("DESCRIPTION")
#             # employee.UPDATED = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#             employee.save()
#             msg = 'success'
#             return JsonResponse({'msg': msg})
#         if type == "delete":
#             employee = models.Employee.objects.get(id=request.POST.get("clientnum"))
#             employee.delete()
#             return HttpResponse('')
#
#     return render(request, 'myField.html')




@login_required
def Employee(request):

    if request.method == "POST":
        type = request.POST.get('type')
        if type == "init":
            results = models.Employee.objects.all()
            employees = []
            for result in results:
                employee = {
                    'image':"static/media1/"+result.profile_photo,
                    'clientnum': result.id,
                    'clientname': result.username,
                    'gender': result.gender,
                    'tel': result.phone,
                    'id_card': result.id_card,
                    'birthday': result.birthday,
                    'hire_date':result.hire_date,
                    'resign_date': result.resign_date,
                    'imgset_dir': result.imgset_dir,
                    'profile_photo': result.username+"/"+result.profile_photo,
                    'DESCRIPTION': result.DESCRIPTION,
                }

                employees.append(employee)
            return JsonResponse({'clients':employees})
        if type == "add":
            employee = models.Employee()
            employee.username = request.POST.get("clientname")
            try:
                employee_model = models.Employee.objects.get(username=request.POST.get("clientname"))
                msg = 'fail'
            except models.Employee.DoesNotExist:
                employee.gender = request.POST.get("gender")
                employee.phone = request.POST.get("tel")
                employee.id_card = request.POST.get("id_card")
                employee.birthday = request.POST.get("birthday")
                employee.hire_date = request.POST.get("hire_date")
                employee.resign_date = request.POST.get("resign_date")
                employee.imgset_dir = request.POST.get("imgset_dir")
                employee.profile_photo = request.POST.get("profile_photo")
                employee.DESCRIPTION = request.POST.get("DESCRIPTION")
                # employee.CREATED = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                employee.CREATEBY = models.MyUser.objects.get(username=get_user(request).username)
                employee.save()
                msg = 'success'
            return JsonResponse({'msg': msg})
        if type == "save":
            id = request.POST.get("clientnum")

            for root, dirs, files in os.walk("static/media/"):
                print(files)  # 当前路径下所有非目录子文件
            for root, dirs, files1 in os.walk("static/media1/"):
                print(files1)  # 当前路径下所有非目录子文件
            for file1 in files1:
                os.remove("static/media1/"+file1)
            shutil.copyfile("static/media/"+files[len(files)-1], "static/media1/"+files[len(files)-1])
            filem=files[len(files)-1]
            for file in files:
                os.remove("static/media/"+file)

            print(files[len(files)-1])

            print(filem)
            employee = models.Employee.objects.get(id = id)
            employee.username = request.POST.get("clientname")
            employee.gender = request.POST.get("gender")
            employee.phone = request.POST.get("tel")
            employee.id_card = request.POST.get("id_card")
            employee.birthday = request.POST.get("birthday")
            employee.hire_date = request.POST.get("hire_date")
            employee.resign_date = request.POST.get("resign_date")
            employee.imgset_dir = request.POST.get("imgset_dir")
            employee.profile_photo = filem
            employee.DESCRIPTION = request.POST.get("DESCRIPTION")
            # employee.UPDATED = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            employee.UPDATEBY = models.MyUser.objects.get(username=get_user(request).username)
            employee.save()
            msg = 'success'
            return JsonResponse({'msg': msg,})
        if type == "delete":
            employee = models.Employee.objects.get(id=request.POST.get("clientnum"))
            employee.delete()
            return HttpResponse('')

    return render(request, 'myField.html')