from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from passwordDatabase.models import PasswordDatabase
from passwords.models import Password
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    user_id = request.session.get('user_id')
    print(user_id)
    if user_id:
        user_profile = User.objects.get(id=user_id)
    else:
        user_profile = [{'username':'User'}]
    password_db = PasswordDatabase.objects.filter(db_user=user_id)
    paginator = Paginator(password_db, 10)
    page_number=request.GET.get('page')
    password_dbFinal=paginator.get_page(page_number)
    totalPageNumber=password_dbFinal.paginator.num_pages
    data={
        'password_db':password_dbFinal,
        'lastpage':totalPageNumber,
        'totalPage':[n+1 for n in range(totalPageNumber)],
        'user_profile':user_profile
    }
    return render(request,"index.html",data)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['user_id'] = user.id
            print(request.session['user_id'])
            return redirect('/')
        else:
            return render(request,"login.html",{'message':'Login error'})
    return render(request,"login.html")

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordConfirmation = request.POST.get('__passwordConfirmation')

        if password!=passwordConfirmation:
            return render(request,"register.html",{'message':'Password should match'})
        else:
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect('/login/')

    return render(request,"register.html")

def logoutPage(request):
    logout(request)
    return redirect('login')

def creatDb(request):
    message=''
    if request.method=='POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        print(user)
        db_name = request.POST.get('dbname')
        db_password = request.POST.get('dbpassword')
        db_passwordConfirmation = request.POST.get('dbpasswordConfirmation')
        if db_name=="":
            return render(request, "create-database.html",{'message':'Database name is required'})
        if db_password!=db_passwordConfirmation:
            return render(request, "create-database.html",{'message':'Database password should match'})
        password_db = PasswordDatabase(db_name=db_name,db_password=db_password,db_user=user)
        password_db.save()
        message='Database Created'
    return render(request, "create-database.html",{'message': message})

def updateDb(request,id):
    password_db = PasswordDatabase.objects.get(pk=id)
    message=''
    data={
        'password_db':password_db,
        'message':message
    }
    if request.method=='POST':

        db_name = request.POST.get('dbname')
        db_password = request.POST.get('dbpassword')
        dbpasswordConfirmation = request.POST.get('dbpasswordConfirmation')
        if db_name=="":
            message = 'All fields are required'
            return render(request,"update-database.html",data)
        if db_password!=dbpasswordConfirmation:
            message = 'Password should match'
            return render(request,"update-database.html",data)
        password_db.db_name = db_name
        password_db.db_password = db_password
        password_db.save()
        message='Database updated'
        data={
            'password_db':password_db,
            'message':message
        }

    return render(request,"update-database.html",data)

def deleteDb(request,id):
    password_db = PasswordDatabase.objects.get(pk=id).delete()
    return redirect('/')

def viewPassword(request,id):
   
   password_db = PasswordDatabase.objects.get(pk=id)
   password = Password.objects.filter(password_db=password_db)
   if password is not None:
        data={
            'passwords':password,
            'db_id':id
        }
        return render(request,"passwords.html",data)
   else:
       return redirect('/')
   

def createPassword(request,id):
    message=''
    if request.method=='POST':
        password_db = PasswordDatabase.objects.get(pk=id)
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = request.POST.get('url')
        if username=="":
            message = 'Username is required'
            return render(request,"create-password.html",{'message':message})
        if password=="":
            message = 'Password is required'
            return render(request,"create-password.html",{'message':message})
        if url=="":
            message = 'Url is required'
            return render(request,"create-password.html",{'message':message})
        passKeys = Password(username=username,password=password,url=url,password_db=password_db)
        passKeys.save()
        message = 'Added new password'

        return redirect('/password/'+str(id))
    return render(request,"create-password.html",{'message':message})

def updatePassword(request,id):
    passKey = Password.objects.get(pk=id)
    message=''
    data={
        'password':passKey,
        'message':message
    }
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = request.POST.get('url') 
        if username=="":
            message = 'Username is required'
            return render(request,"update-password.html",data)
        if password=="":
            message = 'Password is required'
            return render(request,"update-password.html",data)
        if url=="":
            message = 'Url is required'
            return render(request,"update-password.html",data)
        passKey.username = username
        passKey.password = password
        passKey.url = url
        passKey.save()
        message = 'Password updated'
        data={
            'password':passKey,
            'message':message
        }
    return render(request,"update-password.html",data)

def deletePassword(request,id):
   password = Password.objects.get(id=id)
   db_id = password.password_db.id
   print(db_id)
   password.delete()
   message='Password deleted'
   return redirect('/password/'+str(db_id))

   
