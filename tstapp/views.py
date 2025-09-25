from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from tstapp.models import *

from django.conf import settings
from django.core.mail import send_mail
import tstapp.wrkfile as wf
import tstapp.med_exprt as ME
import tstapp.cal as cal
# Create your views here.
    

def hddr(request):
    return render(request,'header.html')

def faqs(request):
    q_a = FAQ.objects.all()
    return render(request,'faq.html',{'data':q_a})

def cont(request):
    if request.method == "POST":
        x = contactus()
        x.name = request.POST.get("fullName")
        x.email = request.POST.get("Email")
        x.sub = request.POST.get("sub")
        x.msg = request.POST.get("msg")
        x.save()
        print(x.name)
        return render(request,'contact.html',{'rmsg':"DONE ✔"})

    else:
        return render(request,'contact.html')

def regs(request):
    if request.method == "POST":
        N = request.POST.get("NM")
        E = request.POST.get("EM")
        

        if usrdata.objects.filter(email=E).exists():
            return render(request,'registerform.html',{'rmsg':'Email already exist'})
        else:
            sotp = wf.generateOTP()
            subject = "Email Verification"
            msg = "welcome! Your verification code is "+ sotp
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [E]
            send_mail(subject,msg,email_from,recipient_list)
            sotp = wf.OWT_door(sotp)
            # res = "Your password is sent on your email."
            return render(request,'otp.html',{'email':E,'name':N,'sotp':sotp})
              
    else:
        return render(request,'registerform.html')

def log(request):

    if request.method=='POST':
        e = request.POST.get('em')
        p = request.POST.get('pass')
        data = usrdata.objects.filter(email=e, Pw=p)
        l = len(data)
        if l>0:
            request.session["email"]=e
            return redirect('/pfr')

        else:

            return render(request,'login.html',{'rmsg':'User not found'})

    else:
        return render(request,'login.html')


def prf(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        return render(request,'profile.html',{'usr':usr})

def chngpw(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    usr = usrdata.objects.get(email=request.session["email"])
    if request.method=='POST':
        o = request.POST.get("opw")
        n =  request.POST.get('npw')
        r =  request.POST.get('rpw')
        if n==r:
            p = usr.Pw
            
            if o==p:
                if n==p:
                    return render(request,'chngpw.html',{'rmsg':"Please enter new password to change",'usr':usr})
                else:
                    usr.Pw = n
                    usr.save()
                    return render(request,'chngpw.html',{'rmsg':"Password succesfully changed",'usr':usr})
            else:
                return render(request,'chngpw.html',{'rmsg':"Incorrect old password",'usr':usr})
        else:
            return render(request,'chngpw.html',{'rmsg':"New password and Confirm password are not same",'usr':usr})
    else:
        return render(request,'chngpw.html',{'usr':usr})


def logout(request):
    del request.session['email']
    return redirect('/login')

def edit(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=='POST':
            usr.name = request.POST.get("nm")
            usr.dob = request.POST.get('dob')
            usr.edulvl = request.POST.get('edu')
            usr.edufld = request.POST.get('fedu')
            usr.save()
            return render(request,'edit-prof.html',{'usr':usr,'rmsg':"Updateed Successfully"})

        else:
            return render(request,'edit-prof.html',{'usr':usr})

def fpw(request):
    if request.method=='POST':
        eml = request.POST.get('em')
        user = usrdata.objects.filter(email=eml)
        if(len(user)>0):
            pw = user[0].Pw
            subject = "forget password"
            msg = "welcome! Your password is "+ pw
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [eml]
            send_mail(subject,msg,email_from,recipient_list)
            res = "Your password is sent on your email."
            return render(request,'fpass.html',{'rmsg':res})
        else:
            res = "Email is not valid"
            return render(request,'fpass.html',{'rmsg':res})
    else:
        return render(request,'fpass.html')

def otp(request):

    if request.method=='POST':
        N = request.POST.get("NM")
        E = request.POST.get("EM")
        s = request.POST.get("sotp")
        uotp = request.POST.get("uotp")
        uotp = wf.OWT_door(uotp)
        s = int(s)
        
        print("s = ",s,'uotp = ',uotp)
        if uotp==s:
            return render(request,'setpass.html',{'email':E,'name':N})
        else:
            return render(request,'otp.html',{'email':E,'name':N,'sotp':s,'rmsg':'retry!'})

def setpass(request):
    if request.method=='POST':
        N = request.POST.get("NM")
        E = request.POST.get("EM")
        p = request.POST.get("pw")
        rp = request.POST.get("rpw")
        if p==rp:
            print("enter if")
            newUsr = usrdata()
            newUsr.email = E
            newUsr.name = N
            newUsr.Pw = p
            print("save data")
            newUsr.save()
            return redirect("/pfr")
        else:
            print("enter else block")
            rms = "Password and conferm Password dose not match"
            return render(request,'setpass.html',{'rmsg':rms})

def image_map(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        bodyparts=BodyPart.objects.all()
        return render(request,"body.html",{"bodyparts":bodyparts, "usr":usr})

def symptoms_view(request,body_part_id):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        body_part=get_object_or_404(BodyPart,pk=body_part_id)
        symptoms=Symptom.objects.filter(body_part=body_part)
        return render(request,"symptoms.html",{"body_part":body_part,"symptoms":symptoms,"usr":usr})

def disease(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=="POST":
            selected_symptoms= request.POST.getlist("symptoms")
            if selected_symptoms:
                symptoms=Symptom.objects.filter(pk__in=selected_symptoms)
                diseases=Disease.objects.filter(symptoms__in=symptoms).distinct()
            return render(request,"disease.html",{"symptoms":symptoms,"diseases":diseases,"usr":usr})
        else:
            return render(request,"symptoms.html",{'usr':usr})

def cal_index(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        return render(request,"calculators.html",{"usr":usr})

def bmi(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=="POST":
            w = float(request.POST.get("wt"))
            h = float(request.POST.get("ht"))
            height = h/100
            bmi = w / (height ** 2)
            if bmi <= 18:
                return render(request,"r-bmi.html",{"height":h,"weight":w,"msg": "underweight", "bmi":("%.2f" %bmi),"usr":usr})
            elif bmi <= 24.9:
                return render(request,"r-bmi.html",{"height":h,"weight":w,"msg": "normal", "bmi":("%.2f" %bmi),"usr":usr})
            elif bmi <=29:
                return render(request,"r-bmi.html",{"height":h,"weight":w,"msg": "overweight", "bmi":("%.2f" %bmi),"usr":usr})
            else:
                return render(request,"r-bmi.html",{"height":h,"weight":w,"msg": "obese", "bmi": ("%.2f" %bmi),"usr":usr})
        else:
            return render(request,"bmi.html",{"usr":usr})

def bmr(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=="POST":
            w = float(request.POST.get("wt"))
            h = float(request.POST.get("ht"))
            age = int(request.POST.get("age"))
            gender = str(request.POST.get("gender"))
            bmr = cal.calculate_bmr(w, h, age, gender)
            return render(request,"r-bmr.html",{"bmr":("%.2f" %bmr),"height":h,"weight":w, "age":age, "gender":gender,"usr":usr})
        else:
            return render(request,"bmr.html",{"usr":usr})

def CalorieIntake(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=="POST":
            w = float(request.POST.get("wt"))
            h = float(request.POST.get("ht"))
            age = int(request.POST.get("age"))
            gender = str(request.POST.get("gender"))
            activity_level = float(request.POST.get("activity_level"))
            bmr = cal.calculate_bmr(w, h, age, gender)
            calin = cal.calculate_calorie_intake(bmr, activity_level)
            return render(request,"r-CalorieIntake.html",{"calin":("%.2f" %calin),"height":h,"weight":w, "age":age, 
                "gender":gender,"activity_level":activity_level,"usr":usr})
        else:
            return render(request,"CalorieIntake.html",{"usr":usr})

def ibw(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=="POST":
            h = float(request.POST.get("ht"))
            gender = str(request.POST.get("gender"))
            ibw = cal.calculate_ibw(h, gender)
            return render(request,"r-IBW.html",{"ibw":("%.2f" %ibw),"height":h,"gender":gender,"usr":usr})
        else:
            return render(request,"IBW.html",{"usr":usr})

def HydrationCal(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=="POST":
            w = float(request.POST.get("wt"))
            activity_level = str(request.POST.get("activity_level"))
            h2o = cal.calculate_water_intake(w, activity_level)
            return render(request,"r-HydrationCal.html",{"h2o":("%.2f" %h2o),"weight":w,
                                                         'activity_level':activity_level,"usr":usr})
        else:
            return render(request,"HydrationCal.html",{"usr":usr})

def hosp(request):
    hosp = Hospital.objects.all()
    return render(request,"hosp.html",{'hosp':hosp})

def exprt(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method=="POST":
            ip = request.POST.get("symptom")
            ip1 = ip.lower()
            disease = ME.get_predicted_value(ip1)
            if disease == "Invalid Input":
                return render(request,'exprt.html',{"usr":usr, "rmsg":disease})
            md = med.objects.all()
            for m in md:
                if m.disease == disease:
                    md_output = m.medi

            dt = diets.objects.all()
            for d in dt:
                if d.disease == disease:
                    dt_output = d.diet

            return render(request,'exprt.html',{"ip":ip, 'disease':disease,"med":md_output, 'diet':dt_output ,"usr":usr})
        else:
            return render(request,'exprt.html',{"usr":usr})
        
def feedback(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    else:
        usr = usrdata.objects.get(email=request.session["email"])
        if request.method == "POST":
            feedback.name = request.POST.get("nm")
            feedback.u_id = request.POST.get("id")
            feedback.msg = request.POST.get("fb")
            feedback.save()
            rmsg = "Thanks for your Feedback"
            return render(request,'feedback.html',{'rmsg':rmsg,"usr":usr})
        else:
            return render(request,'feedback.html',{"usr":usr})

