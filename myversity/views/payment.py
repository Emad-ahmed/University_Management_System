from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from myversity.models import Registration, Payment_Done
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class PaymentView(View):
    def get(self, request, id):
        try:
            myuser = Registration.objects.get(id=id)
            return render(request, 'payment.html', {'myuser': myuser})
        except:
            return redirect('myregister')

    def post(self, request, id):
        my_ref = request.POST.get("ref_number")
        myuser = Registration.objects.get(id=id)
        myemail = myuser.email

        if my_ref == myuser.referece_number:
            payment = 500
            mypayment = Payment_Done(user=myuser, payment_amount=payment)
            mypayment.save()
            messages.success(request, 'Successfully Send Email.')
            content = f"Hello {myuser.name}\nYour Payment Sucessfully Completed Thank You.\nLeading University, Sylhet"
            send_mail("Successfully Registration",
                      content,
                      settings.EMAIL_HOST_USER,
                      [myemail]
                      )
        else:
            messages.success(request, 'Enter Correct Reference Number.')
        return render(request, 'payment.html')
