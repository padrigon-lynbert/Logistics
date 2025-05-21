from django.db import IntegrityError 
from django.http import HttpResponse, Http404

from django.shortcuts import render
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect

from .models import UserInfo, Vendor_history


def index_market(request):
    return render(request, 'index.html')
def explore(request):
    return render(request, 'explore.html')
def create(request):
    return render(request, 'create.html')

def author(request):
    vendor_history = Vendor_history.objects.all()
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('signin')  # Not logged in

    try:
        user = UserInfo.objects.get(id=user_id)
        return render(request, 'author.html', {
            'user': user,
            'vendor_history': vendor_history})
    except UserInfo.DoesNotExist:
        return redirect('signin')


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
                request.session['user_id'] = user.id  # Save user.id
                return redirect('author') # success page
            else:
                print("Wrong password")
                return render(request, 'signin.html', {'error': 'Invalid password'})

        except UserInfo.DoesNotExist:
            print("No user found")
            return render(request, 'signin.html', {'error': 'User not found'})

    return render(request, 'signin.html')








def vendor_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        service = request.POST['service']
        about = request.POST['about']
        raw_bid = request.POST.get('bid')
        bid = request.POST.get('bid') or None

        if 'image' in request.FILES:
            image = request.FILES['image']
            img_binary = image.read()
        else:
            img_binary = None

        hashed_password = make_password(password)

        try:
            user_info = UserInfo(
            name=name,
            email=email,
            password=hashed_password,
            info=f"{service} - {about}",
            bid=bid,
            img=img_binary
        )
            user_info.save()
            return redirect('signin')

        except IntegrityError:
            return render(request, 'vendor_signup.html', {
                'error': 'Email already exists. Try signing in or use another email.'
            })

    return render(request, 'vendor_signup.html')

def user_image(request, user_id):
    try:
        user = UserInfo.objects.get(id=user_id)
        if user.img:
            return HttpResponse(user.img, content_type="image/jpeg")  # or image/png, depending on your images
        else:
            raise Http404("No image found")
    except UserInfo.DoesNotExist:
        raise Http404("User not found")