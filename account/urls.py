from django.urls import path
from account.views import HomeAccount, Addmission_Approve_View, Approve_RegisterView, UpdateAdmission, deleteadmission


urlpatterns = [
    path("", HomeAccount.as_view(), name="home_account"),
    path("addmission_approve", Addmission_Approve_View.as_view(),
         name="addmission_approve"),
    path("approve_register/<int:id>/", Approve_RegisterView.as_view(),
         name="approve_register"),
    path("updateaddmission/<int:id>/", UpdateAdmission.as_view(),
         name="updateaddmission"),
    path("deleteadmission/<int:id>/", deleteadmission,
         name="deleteadmission"),
]
