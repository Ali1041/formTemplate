from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import os
import stripe

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
stripe.api_key = "secret_key" #client secrent key of stripe

# Create your views here.

def form(request, **kwargs):
    # return redirect('application:form-back')
    # saving the data in db
    if request.method == 'POST':
        country = Country.objects.get(country_name=request.POST['country'])
        birth_country = Country.objects.get(country_name=request.POST['birth_country'])
        record = Record.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            country=country,
            phone_number=request.POST['phone_number'],
            birth_country=birth_country,
            age=request.POST['age'],
            martial_status=request.POST['martial_status'],
            speaking_english_level=request.POST['english_level'],
            education_level=request.POST['education_level'],
            been_to_canada=request.POST['been_in_canada'],
            monthly_income=request.POST['monthly_income'],
            interested_visa=request.POST['visa']
        )

        # storing in session
        request.session['record_id'] = record.pk
        return redirect('application:form-back')
    if request.method == 'GET':

        # in get request checking if form has been submitted before
        try:
            if request.session['record_id']:
                return redirect('application:form-back')

        # rendering the form if not
        except:
            ctx = {'country': Country.objects.all()}
            return render(request, 'form.html', ctx)


# displaying the empty page once the form s submitted
def payment(request):
    # checking if record_id not set, then redirect to the first step of form
    if 'record_id' not in request.session:
        return redirect("application:form")
    
    # otherwise render payment page
    return render(request, 'payment.html')

def charge(request):
    # checking if record_id not set, then redirect to the first step of form
    if 'record_id' not in request.session:
        return redirect("application:form")

    if request.method == "POST":
        print(request.POST)
        try:
            # get the stored recod model id from session
            id = request.session['record_id']

            # query db to get that specific record
            user_record = Record.objects.get(pk=id)

            # customer = stripe.Customer.create(
            #     email = user_record.email, #set user email here from recorded object of previous info
            #     name = user_record.first_name+' '+user_record.last_name, #set full name of customer here
            #     source = request.POST.get('stripeToken') #DONT change anything
            # )
            # print(customer)
            # charge = stripe.Charge.create(
            #     customer = customer,
            #     amount = int(49)*100,
            #     currency = 'usd',
            #     description = "Canada Immigration"
            # )
            # MAKE A MODEL called payment_charge with following fileds
            # id (default - no need to create)
            # user (FOREIGN KEY, connect with our previous model - this field will save information of user which he has given previously)
            # amount (float - default = 49.0)
            # unit (string - default = USD)
            # DATE TIME (datetimefield, default = datetime.now())

            # create object above model here with the current user

            # creating payment charge instance from the user_record variable
            my_user = PaymentCharge.objects.create(user_record=user_record,amount=49,unit='USD')

            messages.info(request, "Your purchase has been completed successfully!")

            # reditect user to a new empty page which says THANK YOU SO MUCH , we will contact you soon!
            return render(request,'success.html')
        except:
            messages.info(request, "Something went wrong! please try Again")

            # reditect user to SAME payment page with "SOMETHIHNG WENT WRONG , try again"
            return render(request,'wrong.html')
