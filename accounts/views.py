from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.http import HttpResponse
from .models import CustomUser,DoctorsTable,CategoryTable,AppointMail
from django.contrib import messages
from FirstProj.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def login(request):

    print(request.method)
    if request.method == 'POST':
        try:
            email = request.POST["Email"]
            pass_word = request.POST["Password"]
            print("hello")
            for custom_users in CustomUser.objects.all():
                if str(custom_users.email) == email:
                    login_obj = custom_users
                    u_name = custom_users.username
                    u_email = custom_users.email
                    break
                else:
                    login_obj  = None   

            if login_obj is not None:
                if str(login_obj.password) == pass_word:
                    request.session['user_id'] = login_obj.id
                    print("login done!!!")
                    docs = {}
                    cats = CategoryTable.objects.all().count()
                    cats = int(cats)
                    print(cats)
                    i=1
                    doc=[]
                    data = {}
                    category = ""
                    while (i <= cats):
                        persons= []
                        docs[i] = DoctorsTable.objects.filter(dr_category__id=i)
                        print(docs[i])
                        for doc in docs[i]:
                            person = {
                                'dr_name' :'',
                                'dr_qualification' :'',
                                'dr_img' :'',
                                'dr_address' :'',
                                'dr_city' :'',
                                    }
                            category = doc.dr_category
                            print(category)
                            person['dr_name'] = doc.dr_name
                            person['dr_img'] = doc.dr_img
                            person['dr_qualification'] = doc.dr_qualification
                            person['dr_address'] = doc.dr_address
                            person['dr_city'] = doc.dr_city
                            persons.append(person)
                        data[category] = persons 
                        i=i+1
                    print(data)
                    print(u_name)
                    print(u_email)
                    print(login_obj.password)
                    context = {
                        'u_name' : u_name,
                        'u_email' : u_email,
                    } 
                    return render(request,'SecondPage.html', {'data': data , 'context': context})   
         
                else:
                    print("Wrong Password")
                    return redirect('/')
            else:
                print("Invalid Credentialssssss..")
                return redirect('/')
        except:
            return HttpResponse("Exception...!")
    
def confirm(request):
    obj = AppointMail()
    if request.method == 'POST':
        # appointmail = AppointMail()
        # drObj = DoctorsTable()
        docName = request.POST['send_name']
        userMail = request.POST['send_email']
        print(userMail)
        obj.patient_name = request.POST['PatientName']
        obj.appoint_date = request.POST['AppointDate']
        obj.appoint_time = request.POST['AppointTime']
        
        for doc in DoctorsTable.objects.all():
            if str(doc.dr_name) == docName:
                print(docName)
                obj.dr_detail = doc 
                obj.save()
                docMail = str(doc.dr_email)
                print(docMail)
                
                messenger1 = "Doctor's Name : %s\nDoctor's Address : %s\nDoctor's City : %s\nPatient's Name : %s\nAppointment Date(YYYY-MM-DD) : %s\nAppointment Time(24 Hrs Format) : %s\n"%(
                    docName,
                    doc.dr_address,
                    doc.dr_city,
                    obj.patient_name,
                    obj.appoint_date,
                    obj.appoint_time)
                recipient = userMail
                send_mail('Hello From Django', messenger1 , EMAIL_HOST_USER, [recipient], fail_silently = False)

                messenger2 = "Patient's Name : %s\nAppointment Date(YYYY-MM-DD) : %s\nAppointment Time(24 Hrs Format) : %s\n"%(
                    obj.patient_name,
                    obj.appoint_date,
                    obj.appoint_time)
                recipient = docMail
                send_mail("Here's Your Patient", messenger2, EMAIL_HOST_USER, [recipient], fail_silently= False)
                messages.success(request, "Email is Sent to Your Email and Doctor's Mail")
    return redirect('/')  


def register(request):
    user_obj = CustomUser()
    if request.method =='POST':
        user_obj.username = request.POST['Name']
        user_obj.email = request.POST['Email']
        user_obj.password = request.POST['Password']
        user_obj.address = request.POST['Address']
        user_obj.city = request.POST['City']
        user_obj.pincode = request.POST['PinCode']

        if CustomUser.objects.filter(email=user_obj.email).exists():
            messages.warning(request, "Email Already Exists")
            print('Email Already Exists')
        else:
            user_obj.save()
            messages.success(request, "Your Account has been Created Successfully!!!")
            return redirect('/')

        return redirect('/')

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('/')


   