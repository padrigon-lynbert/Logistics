from django.shortcuts import render

def index_market(request):
    return render(request, 'index.html')

def explore(request):
    return render(request, 'explore.html')

def item_details(request):
    return render(request, 'details.html')

def author(request):
    return render(request, 'author.html')

def create(request):
    return render(request, 'create.html')



from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import SignupForm
from .models import UserInfo  # Assuming you have a UserInfo model created

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])  # Hash the password
            info = form.cleaned_data['info']
            bid = form.cleaned_data['bid']

            # Create a new user and save
            user = UserInfo(name=name, email=email, password=password, info=info, bid=bid)
            user.save()

            return redirect('index_market')  # Redirect to a login page (you can adjust this)
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})






from django.contrib.auth.hashers import check_password
from .models import UserInfo

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserInfo.objects.get(email=email)
            if check_password(password, user.password):
                # Add login logic here if needed (session, etc.)
                return redirect('index_market')
            else:
                return render(request, 'signin.html', {'error': 'Invalid credentials'})
        except UserInfo.DoesNotExist:
            return render(request, 'signin.html', {'error': 'User not found'})

    return render(request, 'signin.html')

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import UserInfo
from passlib.hash import pbkdf2_sha256
from django.core.exceptions import ValidationError


def vendor_signup(request):
    if request.method == 'POST':
        # Extract other form data
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        service = request.POST['service']
        about = request.POST['about']
        raw_bid = request.POST.get('bid')
        bid = int(raw_bid) if raw_bid else None


        # Handle image upload with check
        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            img_url = fs.url(filename)  # <- This returns /media/filename.ext
        else:
            img_url = None

        # Hash the password
        hashed_password = pbkdf2_sha256.hash(password)

        # Print for debugging
        print(f"Name: {name}, Email: {email}, Service: {service}, About: {about}, Bid: {bid}, Image URL: {img_url}")

        # Create and save UserInfo
        user_info = UserInfo(
            name=name,
            email=email,
            password=hashed_password,
            info=f"{service} - {about}",
            bid=bid,
            img=img_url
        )
        user_info.save()

        # Redirect to the 'signin' page
        return redirect('signin')

    # If the request is not POST, render the signup page
    return render(request, 'vendor_signup.html')






