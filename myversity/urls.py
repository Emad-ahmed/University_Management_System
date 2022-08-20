from django.urls import path
from myversity.views import HomeView, RegisterView, PaymentView, BBAVIEW, Login, logout, StudentInfo, AboutView, ScholarView, AllteachInfo, CSEVIEW, EEEVIEW, NewsView, EventsView, TutionFeesView, GuideLineView, ResultViewStudent, SemisterregisterView, EnglishVIEW, CivilVIEW, ArchitecureVIEW, LawVIEW, StudentSemisterregisteradd, Classroutine


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("news/<int:id>/", NewsView.as_view(), name="news"),
    path("events/<int:id>/", EventsView.as_view(), name="events"),
    path("register/", RegisterView.as_view(), name="register"),
    path("payment/<int:id>", PaymentView.as_view(), name="payment"),
    path("bba/", BBAVIEW.as_view(), name="bba"),

    path("cse/", CSEVIEW.as_view(), name="cse"),
    path("eee/", EEEVIEW.as_view(), name="eee"),
    path("eng/", EnglishVIEW.as_view(), name="eng"),
    path("civil/", CivilVIEW.as_view(), name="civil"),
    path("arch/", ArchitecureVIEW.as_view(), name="arch"),
    path("law/", LawVIEW.as_view(), name="law"),
    path("classroutine/", Classroutine.as_view(), name="classroutine"),

    path("about/", AboutView.as_view(), name="about"),
    path("scholar/", ScholarView.as_view(), name="scholar"),
    path("showallinfoteacher/<int:id>/",
         AllteachInfo.as_view(), name="showallinfoteacher"),
    path('loginview/', Login.as_view(), name='loginview'),

    path('studentallinfo/', StudentInfo.as_view(), name='studentallinfo'),
    path('tution_fees/', TutionFeesView.as_view(), name='tution_fees'),
    path('guide_line/', GuideLineView.as_view(), name='guide_line'),
    path('resultviewstudent/', ResultViewStudent.as_view(),
         name='resultviewstudent'),
    path('semisterview/', SemisterregisterView.as_view(),
         name='semisterview'),
    path('addstudentsemister/<int:id>?', StudentSemisterregisteradd.as_view(),
         name='addstudentsemister'),
    path('logout/', logout, name='logout'),
]
