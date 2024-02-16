from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *



# Create your views here.
def home(request):
    return render(request,'home.html')
def teacher(request):
    if request.method == "POST":
        data=request.POST
        name=data.get("name")
        pwd=data.get("pwd")
        if name=="Teacher" and pwd=="Teacher123":
             return render(request,'teacherframe.html')
        else:
            return render(request,'error.html')
    return render(request,'teacher.html')
def student(request):
    if request.method == "POST":
        data=request.POST
        name=data.get("name")
        pwd=data.get("pwd")
        if name=="Student" and pwd=="Student123":
             return render(request,'studentframe.html')
        else:
               return render(request,'error.html')
    return render(request,'student.html')
def administer (request):
    if request.method == "POST":
        data=request.POST
        name=data.get("name")
        pwd=data.get("pwd")
        if name=="Admin" and pwd=="Admin123":
             return render(request,'adminframe.html')
        else:
            return render(request,'error.html')
    return render(request,'administer.html')
def teacherframe(request):
    return render(request,'teacherframe.html')
def studentframe(request):
    return render(request,'studentframe.html')
def adminframe(request):
    return render(request,'adminframe.html')
def addpuc1student(request):
    return render(request,'addpuc1student.html')
def postadd(request):
    return render(request,'postadd.html')

def addstudent(request):
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        dob=data.get("dob")
        fees=data.get("fees")
        clas=data.get("class")
        mobile=data.get("mobile")
        rollno=data.get("rollno")
        std=Student.objects.create(
            name=name,
            dob=dob,
            fees=fees,
            mobile=mobile,
            cls=clas,
            rollno=rollno,
        )
        attendence1=Attendence.objects.create(student=std)
        mrk=Marks.objects.create(student=std)
        queryset=Student.objects.all()
        context={'info':queryset}
    
    return render(request,'postadd.html' )
def error(request):
    return render(request,'error.html')
def view1(request):
    queryset=Student.objects.filter(cls=1).values()
    context={'info':queryset}
    
    return render(request,'view1.html',context)
def view2(request):
    queryset=Student.objects.filter(cls=2).values()
    context={'info':queryset}
    
    return render(request,'view2.html',context)
def fee1(request):
    queryset=Student.objects.filter(cls=1).values()
    context={'info':queryset}
    
    return render(request,'fee1.html',context)
def fee2(request):
    queryset=Student.objects.filter(cls=2).values()
    context={'info':queryset}
    
    return render(request,'fee2.html',context)
def stafform(request):
    return render(request,'stafform.html')
def addstaff(request):
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        email=data.get("email")
        mobile=data.get("mobile")
        salary=data.get("salary")
        subject=data.get("subject")
        Staff.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            salary=salary,
            subject=subject,
        )
    return render(request,'poststaff.html')
def viewstaff(request):
    queryset=Staff.objects.all()
    context={'info':queryset}
    
    return render(request,'viewstaff.html',context)
def staffsalary(request):
    queryset=Staff.objects.all()
    context={'info':queryset}
    
    return render(request,'staffsalary.html',context)
def delete(request,id):
    queryset=Student.objects.get(id=id)
    queryset.delete()
    return redirect('/view1')
def update(request,id):
    queryset=Student.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        dob=data.get("dob")
        fees=data.get("fees")
        clas=data.get("class")
        mobile=data.get("mobile")
        queryset.name=name
        queryset.dob=dob
        queryset.fees=fees
        queryset.cls=clas
        queryset.mobile=mobile
        queryset.save()
        return redirect('/view1')
    context={'info':queryset}
    return render(request,'update.html',context)
def delete_view2(request,id):
    queryset=Student.objects.get(id=id)
    queryset.delete()
    return redirect('/view2')
def update_view2(request,id):
    queryset=Student.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        dob=data.get("dob")
        fees=data.get("fees")
        clas=data.get("class")
        mobile=data.get("mobile")
        queryset.name=name
        queryset.dob=dob
        queryset.fees=fees
        queryset.cls=clas
        queryset.mobile=mobile
        queryset.save()
        return redirect('/view2')
    context={'info':queryset}
    return render(request,'update1.html',context)
def updatefee1(request,id):
    queryset=Student.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        fees=data.get("fees")
        mobile=data.get("mobile")
        queryset.name=name
        queryset.fees=fees
        queryset.mobile=mobile
        queryset.save()
        return redirect('/fee1')
    context={'info':queryset}
    return render(request,'updatefee.html',context)
def updatefee2(request,id):
    queryset=Student.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        fees=data.get("fees")
        mobile=data.get("mobile")
        queryset.name=name
        queryset.fees=fees
        queryset.mobile=mobile
        queryset.save()
        return redirect('/fee2')
    context={'info':queryset}
    return render(request,'updatefee.html',context)
def deletestaff(request,id):
    queryset=Staff.objects.get(id=id)
    queryset.delete()
    return redirect('/viewstaff')
def updatestaff(request,id):
    queryset=Staff.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        email=data.get("email")
        salary=data.get("salary")
        subject=data.get("subject")
        mobile=data.get("mobile")
        queryset.name=name
        queryset.email=email
        queryset.salary=salary
        queryset.subject=subject
        queryset.mobile=mobile
        queryset.save()
        return redirect('/viewstaff')
    context={'info':queryset}
    return render(request,'updatestaff.html',context)
def updatestaffee(request,id):
    queryset=Staff.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        name=data.get("name")
        salary=data.get("salary")
        mobile=data.get("mobile")
        queryset.name=name
        queryset.salary=salary
        queryset.mobile=mobile
        queryset.save()
        return redirect('/staffsalary')
    context={'info':queryset}
    return render(request,'updatestaffee.html',context)
def viewstaff1(request,id):
    queryset=Staff.objects.all()
    context={'info':queryset}
    
    return render(request,'viewstaff.html',context)
def updatestaffee1(request,id):
    queryset=Staff.objects.all()
    context={'info':queryset}
    
    return render(request,'staffsalary.html',context)
def back1(request,id):
   
     return redirect('/view1')
def back2(request,id):
   
     return redirect('/view2')   
def backfee1(request,id):
   
     return redirect('/fee1')   
def backfee2(request,id):
   
     return redirect('/fee2')   
def attendence1(request):
    queryset=Attendence.objects.all()
    queryset=queryset.filter(student__cls=1)
    context={'info':queryset}
    return render(request,'attendence1.html',context)
def attendence2(request):
    queryset=Attendence.objects.all()
    queryset=queryset.filter(student__cls=2)
    context={'info':queryset}
    return render(request,'attendence2.html',context)
def updateattendence1(request,id):
    queryset=Attendence.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/attendence1')
    context={'info':queryset}
    return render(request,'updateattendence.html',context)
def attendenceback1(request):
    return redirect('/attendence1')
def updateattendence2(request,id):
    queryset=Attendence.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/attendence2')
    context={'info':queryset}
    return render(request,'updateattendence1.html',context)
def attendenceback2(request):
    return redirect('/attendence2')
def result1(request):
    queryset=Marks.objects.all()
    queryset=queryset.filter(student__cls=1)
    context={'info':queryset}
    return render(request,'result1.html',context)
def result2(request):
    queryset=Marks.objects.all()
    queryset=queryset.filter(student__cls=2)
    context={'info':queryset}
    return render(request,'result2.html',context)
def updatemarks1(request,id):
    queryset=Marks.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/result1')
    context={'info':queryset}
    return render(request,'updateresult1.html',context)
def updatemarks2(request,id):
    queryset=Marks.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/result2')
    context={'info':queryset}
    return render(request,'updateresult2.html',context)
def backre1(request):
    return redirect('/result1')
def backre2(request):
    return redirect('/result2')
def notice1(request):
    return render(request,'notice1.html')
def notice2(request):
    return render(request,'notice2.html')
def addnotice(request):
    return render(request,'addnotice.html')
def viewnotice(request):
    queryset=Notice.objects.all()
    context={'info':queryset}
    return render(request,'viewnotice.html',context)
def noticeback1(request):
    return redirect('/notice1')
def addnotice(request):
    if request.method=="POST":
        data=request.POST
        notice=data.get("notice")
        Notice.objects.create(notice=notice)
        return render(request,'postnotice.html')
    return render(request,'addnotice.html')
def deletenotice(request,id):
    queryset=Notice.objects.get(id=id)
    queryset.delete()
    return redirect('/viewnotice')
def addnotice1(request):
    if request.method=="POST":
        data=request.POST
        notice=data.get("notice")
        Notice2.objects.create(notice=notice)
        return render(request,'postnotice1.html')
    return render(request,'addnotice1.html')
def deletenotice1(request,id):
    queryset=Notice2.objects.get(id=id)
    queryset.delete()
    return redirect('/viewnotice1')
def viewnotice1(request):
    queryset=Notice2.objects.all()
    context={'info':queryset}
    return render(request,'viewnotice1.html',context)
def stdatd1(request):
    queryset=Attendence.objects.all()
    queryset=queryset.filter(student__cls=1)
    context={'info':queryset}
    return render(request,'stdatd1.html',context)
def stdatd2(request):
    queryset=Attendence.objects.all()
    queryset=queryset.filter(student__cls=2)
    context={'info':queryset}
    return render(request,'stdatd2.html',context)
def stdre1(request):
    queryset=Marks.objects.all()
    queryset=queryset.filter(student__cls=1)
    context={'info':queryset}
    return render(request,'stdre1.html',context)
def stdre2(request):
    queryset=Marks.objects.all()
    queryset=queryset.filter(student__cls=2)
    context={'info':queryset}
    return render(request,'stdre2.html',context)
def stdnt1(request):
    queryset=Notice.objects.all()
    context={'info':queryset}
    return render(request,'stdnt1.html',context)
def stdnt2(request):
    queryset=Notice2.objects.all()
    context={'info':queryset}
    return render(request,'stdnt2.html',context)
def teatd1(request):
    queryset=Attendence.objects.all()
    queryset=queryset.filter(student__cls=1)
    context={'info':queryset}
    return render(request,'teatd1.html',context)
def teatd2(request):
    queryset=Attendence.objects.all()
    queryset=queryset.filter(student__cls=2)
    context={'info':queryset}
    return render(request,'teatd2.html',context)
def updateteatd1(request,id):
    queryset=Attendence.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/teatd1')
    context={'info':queryset}
    return render(request,'updateteatd1.html',context)
def updateteatd2(request,id):
    queryset=Attendence.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/teatd2')
    context={'info':queryset}
    return render(request,'updateteatd2.html',context)
def backteatd1(request):
    return redirect('/teatd1')
def backteatd2(request):
    return redirect('/teatd2')
def tere1(request):
    queryset=Marks.objects.all()
    queryset=queryset.filter(student__cls=1)
    context={'info':queryset}
    return render(request,'tere1.html',context)
def tere2(request):
    queryset=Marks.objects.all()
    queryset=queryset.filter(student__cls=2)
    context={'info':queryset}
    return render(request,'tere2.html',context)
def updatetere1(request,id):
    queryset=Marks.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/tere1')
    context={'info':queryset}
    return render(request,'updatetere1.html',context)
def updatetere2(request,id):
    queryset=Marks.objects.get(id=id)
    if request.method== "POST":
        data=request.POST
        english=data.get("english")
        hindi=data.get("hindi")
        urdu=data.get("urdu")
        physics=data.get("physics")
        maths=data.get("maths")
        chemistry=data.get("chemistry")
        biology=data.get("biology")
        computer=data.get("computer")
        queryset.english=english
        queryset.hindi=hindi
        queryset.urdu=urdu
        queryset.physics=physics
        queryset.maths=maths
        queryset.chemistry=chemistry
        queryset.biology=biology
        queryset.computer=computer
        queryset.save()
        return redirect('/tere2')
    context={'info':queryset}
    return render(request,'updatetere2.html',context)
def backtere1(request):
    return redirect('/tere1')
def backtere2(request):
    return redirect('/tere2')
def tent1(request):
    return render(request,'tent1.html')
def tent2(request):
    return render(request,'tent2.html')
def addtent1(request):
    if request.method=="POST":
        data=request.POST
        notice=data.get("notice")
        Notice.objects.create(notice=notice)
        return render(request,'posttent1.html')
    return render(request,'addtent1.html')
def viewtent1(request):
    queryset=Notice.objects.all()
    context={'info':queryset}
    return render(request,'viewtent1.html',context)
def deletetent1(request,id):
    queryset=Notice.objects.get(id=id)
    queryset.delete()
    return redirect('/viewtent1')
def backtent1(request):
    return redirect('/tent1')
def addtent2(request):
    if request.method=="POST":
        data=request.POST
        notice=data.get("notice")
        Notice2.objects.create(notice=notice)
        return render(request,'posttent1.html')
    return render(request,'addtent2.html')
def viewtent2(request):
    queryset=Notice2.objects.all()
    context={'info':queryset}
    return render(request,'viewtent2.html',context)
def deletetent2(request,id):
    queryset=Notice2.objects.get(id=id)
    queryset.delete()
    return redirect('/viewtent2')
def backtent2(request):
    return redirect('/tent2')