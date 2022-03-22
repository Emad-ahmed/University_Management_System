from django.urls import path
from myversity.views import HomeView, RegisterView, PaymentView, BBAVIEW, LoginView, StudentRegsiterView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("payment/<int:id>", PaymentView.as_view(), name="payment"),
    path("bba/", BBAVIEW.as_view(), name="bba"),
    path('loginview/', LoginView.as_view(), name='loginview'),
    path('myregister/', StudentRegsiterView.as_view(), name='myregister'),
]
