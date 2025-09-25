"""
URL configuration for ttstntry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tstapp import views
from django.contrib import admin
from django.urls import path

from django.conf import settings

from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
# from django.contrib.staticfiles.url.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pfr',views.prf, name='pfr'),
    path('nav',views.hddr),
    # path('faq',views.faqs),
    path('signup',views.regs,name='reg'),
    path('login/',views.log, name='login'),
    path('con',views.cont),
    path('chngpw',views.chngpw),
    path('logout',views.logout, name='logout'),
    path('info-usr',views.edit,name='edit'),
    path('forgot-pass',views.fpw,name="fpass"),
    path('email-auth',views.otp,name='eauth'),
    path('setpass',views.setpass, name='setpass'),
    path('bodymap',views.image_map, name='imap'),
    path('sym/<int:body_part_id>',views.symptoms_view, name='sym'),
    path('disease',views.disease,name="disease"),
    path('calculators',views.cal_index,name="cal_index"),
    path('BMI',views.bmi, name='bmi'),
    path('BMR',views.bmr, name='bmr'),
    path('IBW',views.ibw, name='ibw'),
    path('Calorie_Intake',views.CalorieIntake, name='CalorieIntake'),
    path('Hydration_Calculator',views.HydrationCal, name='HydrationCal'),
    path('hospitals',views.hosp, name='hosp_list'),
    path('Expert',views.exprt, name='exprt'),
    path('Feedback',views.feedback, name='Feedback'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
