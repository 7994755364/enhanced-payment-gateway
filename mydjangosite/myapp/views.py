import export
import random
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from django.core.mail import send_mail
from . models import *
from cryptography.fernet import Fernet
import os
from django.contrib.auth import logout
from google.oauth2 import service_account
from googleapiclient.discovery import build


# Create your views here.

# Generate a key and save it securely, such as in environment variables
# key = Fernet.generate_key()
# print(f"Your encryption key: {key}")

# Temporary storage for OTPs (for demonstration)
otp_storage = {}

key = os.getenv('PAYMENT_ENCRYPTION_KEY', Fernet.generate_key())
cipher = Fernet(key)


def encrypt_payment_data(card_number, expiry_date, cvv):
    encrypted_card_number = cipher.encrypt(card_number.encode())
    encrypted_expiry_date = cipher.encrypt(expiry_date.encode())
    encrypted_cvv = cipher.encrypt(cvv.encode())

    return {
        'card_number': encrypted_card_number,
        'expiry_date': encrypted_expiry_date,
        'cvv': encrypted_cvv,
    }
def dummy_payment_gateway(encrypted_data):
    # Decrypt data (this simulates what a real payment gateway might do)
    card_number = cipher.decrypt(encrypted_data['card_number']).decode()
    expiry_date = cipher.decrypt(encrypted_data['expiry_date']).decode()
    cvv = cipher.decrypt(encrypted_data['cvv']).decode()
    print('cccccc',card_number)
    if int(card_number[-1]) % 2 == 0:
        return {"status": "success", "message": "Payment processed successfully"}
    else:
        return {"status": "failure", "message": "Payment failed"}

def payment_page(request):
    return render(request, 'payment_page.html')



# encryption_key = os.getenv('PAYMENT_ENCRYPTION_KEY')

def index(request):
   return render(request,"myapp/index.html",{})

def Base(request):
   return render(request, 'myapp/base.html',{})
def home(request):
   return render(request, 'myapp/home.html',{})

def buyer_reg(request):
   if request.method == 'POST':
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      email = request.POST.get('email')
      print(email)
      password = request.POST.get('password')
      confirm_password = request.POST.get('confirm_password')
      address = request.POST.get('address')
      country = request.POST.get('country')
      town = request.POST.get('town')
      post = request.POST.get('post')
      phone = request.POST.get('phone')
      login_obj = Login()
      login_obj.username = email
      login_obj.password = password
      login_obj.save()
      buyer_obj = Buyer()
      buyer_obj.f_name = fname
      buyer_obj.l_name = lname
      buyer_obj.email = email
      buyer_obj.address = address
      buyer_obj.country = country
      buyer_obj.town = town
      buyer_obj.zipcode = post
      buyer_obj.phone = phone
      buyer_obj.LOGIN_ID = login_obj
      buyer_obj.save()
   return render(request, 'Buyer/Signup.html', {})


def send_email_with_gmail_api():
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/your/service_account.json',
        scopes=['https://www.googleapis.com/auth/gmail.send']
    )

    service = build('gmail', 'v1', credentials=credentials)

def login(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      log_obj = Login.objects.filter(username=username, password=password)
      if log_obj.exists():
          log_obj = log_obj[0]
          request.session["logout"] = "0"
          request.session['lg'] = "yes"
          if request.session['lg'] == "yes":
              buyer_obj = Buyer.objects.filter(LOGIN_ID = log_obj)
              if buyer_obj.exists():
                  buyer_obj = buyer_obj[0]
                  request.session['buyer_id'] = buyer_obj.id
                  return redirect('home')
              else:
                  messages.error(request, "Not Exist.")
          else:
              return render(request, 'myapp/login.html', {})
      else:
          messages.error(request, "Invalid username or password.")
   return render(request, 'myapp/login.html',{})


      # log_obj = Login.objects.filter(username=username, password=password).first()

   #    if user:
   #        # Generate a 6-digit OTP
   #        otp = str(random.randint(100000, 999999))
   #        otp_storage[username] = otp
   #
   #        # Send OTP to user's email
   #        send_mail(
   #            "Your OTP Code",
   #            f"Your OTP code is: {otp}",
   #            settings.EMAIL_HOST_USER,
   #            [user.username],
   #            fail_silently=False,
   #        )
   #
   #        # Store username in session and redirect to OTP page
   #        request.session['username'] = username
   #        return redirect('verify_otp')
   #    else:
   #        messages.error(request, "Invalid username or password.")
   # return render(request, "myapp/login.html")

      #old login

   # View for OTP verification
def verify_otp(request):
    username = request.session.get('username')

    if not username:
        return redirect("login")

    if request.method == "POST":
        otp_entered = request.POST.get("otp")
        otp_correct = otp_storage.get(username)

        if otp_correct == otp_entered:
            user = authenticate(username=username)
            login(request, user)
            del otp_storage[username]  # Clear OTP after use
            return HttpResponse("Login successful with MFA!")
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, "myapp/verify_otp.html")




def view_profile(request):
    if request.session['lg'] == "yes":
        b_id = request.session['buyer_id']
        print(b_id)
        prof_obj = Buyer.objects.get(id=b_id)
        print(id)
    else:
        return redirect('login')
    return render(request, 'Buyer/View_profile.html', {'prof_obj': prof_obj})

# @login_required
def view_product(request):
    if request.session['lg'] == "yes":
        product = Product.objects.all()
    else:
        return redirect('login')

    return render(request, 'Buyer/View_Product.html', {'product':product})

# @login_required
def cart(request, product_id):
    if request.session['lg'] == "yes":
        b_id = request.session['buyer_id']
        print(b_id)
        product = Product.objects.get(pk=product_id)
        buyer = Buyer.objects.get(pk=b_id)
        cart_item, created = Cart.objects.get_or_create(PRODUCT_ID=product, Buyer_ID=buyer)
        if created:
            cart_item.quantity = 1
            cart_item.save()
            messages.success(request, "the product was added successfully")
        else:
            return redirect('view_cart')
    else:
        return redirect('login')
    return render(request, 'Buyer/cart.html', {})

# @login_required
def view_cart(request):
    # if request.session['lg'] == "yes":
    print(f'User authenticated: {request.user.is_authenticated}')
    b_id = request.session['buyer_id']
    cart_obj = Cart.objects.filter(Buyer_ID= b_id)
    total_price = sum(float(item.quantity) * float(item.PRODUCT_ID.rate) for item in cart_obj)
    request.session['total_price'] = total_price
    # else:
    #     return redirect('login')

    return render(request, 'Buyer/cart.html', {'cart_obj': cart_obj, 'total_price': total_price})

def remove_cart(request, product_id):
    # Find the cart item by ID, or return a 404 if not found
    cart_item = Cart.objects.filter(id=product_id)

    # Remove the item from the cart
    cart_item.delete()

    # Optional: Add a success message
    messages.success(request, "Item removed from cart successfully.")

    # Redirect back to the cart page
    return redirect('view_cart')

def view_product_more(request):
    return render(request, 'Buyer/View_productmore.html', {})

def checkout(request):
    if request.session['lg'] == "yes":
        total_price = request.session.get('total_price',0)
        b_id = request.session['buyer_id']
        # cart_obj = Cart.objects.filter(Buyer_ID=b_id)
        del_obj = Shipping_address.objects.filter(LOGIN_ID= b_id)
        prof_obj = Buyer.objects.get(id=b_id)
        if request.method == 'POST':
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            email = request.POST.get('email')
            country = request.POST.get('country')
            address = request.POST.get('address')
            city = request.POST.get('city')
            zipcode = request.POST.get('post')
            phone = request.POST.get('phone_number')
            del_obj.f_name = fname
            del_obj.l_name = lname
            del_obj.email = email
            del_obj.country = country
            del_obj.address = address
            del_obj.city = city
            del_obj.zipcode = zipcode
            del_obj.phone = phone
            del_obj.save()
    else:
        return redirect('login')

    return render(request, 'Buyer/checkout.html', {'prof_obj': prof_obj, 'total_price': total_price})

def process_payment(request):
    if request.method == 'POST':
        # Collect payment data
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Encrypt the payment data
        encrypted_data = encrypt_payment_data(card_number, expiry_date, cvv)

        # Simulate sending to dummy payment gateway
        gateway_response = dummy_payment_gateway(encrypted_data)

        # Redirect to confirmation page based on response
        if gateway_response['status'] == "success":
            return redirect('payment_confirmation')
        else:
            return redirect('payment_failed')
    return redirect('checkout')

def payment_confirmation(request):
    return render(request, 'Buyer/payment_confirmation.html')

def payment_failed(request):
    return render(request, 'Buyer/payment_failed.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or any other page after logout




