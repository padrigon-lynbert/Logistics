from django.shortcuts import render

def index_market(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

def author(request):
    return render(request, 'author.html')

def create(request):
    return render(request, 'create.html')




from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import UserInfo

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserInfo.objects.get(email=email)
            stored_hash = user.password

            print(f"Entered: {password}")
            print(f"Stored: {stored_hash}")

            if check_password(password, stored_hash):
                print("Password correct")
                return redirect('author')  # Success redirect here
            else:
                print("Wrong password")
                return render(request, 'signin.html', {'error': 'Invalid password'})

        except UserInfo.DoesNotExist:
            print("No user found")
            return render(request, 'signin.html', {'error': 'User not found'})

    return render(request, 'signin.html')




from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import UserInfo
from passlib.hash import pbkdf2_sha256
from django.core.exceptions import ValidationError


from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password

from django.db import IntegrityError 

def vendor_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        service = request.POST['service']
        about = request.POST['about']
        raw_bid = request.POST.get('bid')
        bid = int(raw_bid) if raw_bid else None

        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            img_url = fs.url(filename)
        else:
            img_url = None

        hashed_password = make_password(password)

        try:
            user_info = UserInfo(
                name=name,
                email=email,
                password=hashed_password,
                info=f"{service} - {about}",
                bid=bid,
                img=img_url
            )
            user_info.save()
            return redirect('signin')

        except IntegrityError:
            return render(request, 'vendor_signup.html', {
                'error': 'Email already exists. Try signing in or use another email.'
            })

    return render(request, 'vendor_signup.html')

