from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, BankInfo, Education, Experience, PersonalInfo, Contact
import json




def holiday_page(request):
    return render(request, 'holidays.html')


def profile(request):
    return render(request, 'profile.html')


# def profile(request):
#     user_id = request.user.id  # Example for getting the user's ID
#     return render(request, 'profile.html', {'id': user_id})


def dashboard(request):
    return render(request, 'index.html')


def logout_page(request):
    return render(request, 'auth-login-basic.html')


def forget_password(request):
    return render(request, 'auth-forgot-password-basic.html')


def get_user(request, emp_id):
    if request.method == 'GET':
        try:
            # emp_id = '100-1001'
            profile = Profile.objects.get(emp_id=emp_id) 
            print(profile)
            data = {
                'emp_id': profile.emp_id,
                'name': profile.name,
                'role': profile.role,
                'blood_group': profile.blood_group,
                'email': profile.email,
                'contact': profile.contact,
                'status': 'Active'  # Assuming you have a status field, otherwise update this accordingly
            }
            return JsonResponse({'status': 'success', 'data': data})
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Employee not found.'})


@csrf_exempt
def update_user(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)  # Adjust according to how data is sent
            
            employee = Profile.objects.get(emp_id=id)
            if not employee:
                return JsonResponse({"error": "Employee not found"}, status=404)

            first_name = data.get('modalEditUserFirstName')
            middle_name = data.get('modalEditUserMiddleName')
            last_name = data.get('modalEditUserLastName')
            employee.role = data.get('modalEditUserDeignation')
            employee.blood_group = data.get('modalEditUserBlood')
            employee.email = data.get('modalEditUserEmail')
            employee.contact = data.get('modalEditUserPhone')
            employee.name = f"{first_name} {middle_name} {last_name}"
            employee.save()  # Save the updated employee
            
            updated_employee_data = {
                'emp_id': employee.emp_id,
                'name': employee.name,
                'role': employee.role,
                'blood_group': employee.blood_group,
                'email': employee.email,
                'contact': employee.contact,
            }
            print(f"Updated employee: {updated_employee_data}") 
            return JsonResponse({'status': 'success', 'message': 'Employee updated successfully.', 'updated_employee': updated_employee_data})

        except Profile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Employee not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)




def bank_list(request):
    banks = BankInfo.objects.all()
    return render(request, 'bank_list.html', {'banks': banks})


def bank_detail(request, id):
    bank = get_object_or_404(BankInfo, id=id)
    print(bank)
    return render(request, 'bank_detail.html', {'bank':bank})

# def edit_bank(request, bank_id):
#     bank = get_object_or_404(BankInfo, id=bank_id)

#     if request.method == "GET":
#         return render(request, 'edit_bank.html', {'bank': bank})

def bank_create(request):
    if request.method == 'POST':
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        ifsc_code = request.POST.get('ifsc_code')
        pan_no = request.POST.get('pan_no')

        bank = BankInfo.objects.create(
            bank_name=bank_name,
            account_number=account_number,
            ifsc_code=ifsc_code,
            pan_no=pan_no
        ) 
        return JsonResponse({'success': True})  
    return render(request, 'bank_create.html')
    

# @csrf_exempt  
# def edit_bank(request, id):
#     if request.method == 'GET':
#         bank = get_object_or_404(BankInfo, id=id)
#         return render(request, 'bank_edit.html', {'bank': bank})
    
#     if request.method == 'PUT':  
#         data = json.loads(request.body)
#         try:
#             bank = BankInfo.objects.get(id=id)
#             bank.bank_name = data.get('bank_name')
#             bank.account_number = data.get('account_number')
#             bank.ifsc_code = data.get('ifsc_code')
#             bank.pan_no = data.get('pan_no')
#             bank.save()
#             return JsonResponse({'message': 'Bank info updated successfully!'}, status=200)
#         except BankInfo.DoesNotExist:
#             return JsonResponse({'error': 'Bank not found'}, status=404)
#     return JsonResponse({'error': 'Invalid request'}, status=400)


def edit_bank(request, id):
    if request.method == 'GET':
        bank = get_object_or_404(BankInfo, id=id)
        return render(request, 'bank_edit.html', {'bank': bank})

    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            bank = BankInfo.objects.get(id=id)
            bank.bank_name = data.get('bank_name')
            bank.account_number = data.get('account_number')
            bank.ifsc_code = data.get('ifsc_code')
            bank.pan_no = data.get('pan_no')
            bank.save()
            return JsonResponse({'message': 'Bank info updated successfully!'}, status=200)
        except BankInfo.DoesNotExist:
            return JsonResponse({'error': 'Bank not found'}, status=404)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

   
@csrf_exempt 
def delete_bank(request, id):
    if request.method == 'DELETE':
        try:
            bank = get_object_or_404(BankInfo, id=id)
            bank.delete()
            return JsonResponse({'success': True})
        except BankInfo.DoesNotExist:
            return JsonResponse({'error': 'Bank not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
 



@csrf_exempt
def education_list(request):
    educations = Education.objects.all()
    return render(request, 'education_list.html', {'educations': educations})



def education_detail(request, id):
    education = get_object_or_404(Education, id=id)
    return render(request, 'education_detail.html', {'education': education})


@csrf_exempt 
def education_edit(request, id):
    if request.method == 'GET':
        education = get_object_or_404(Education, id=id)
        return render(request, 'education_edit.html', {'education': education})
    
    if request.method == 'PUT':  
        data = json.loads(request.body)
        try:
            education = Education.objects.get(id=id)
            education.institution_name = data.get('institution_name')
            education.degree = data.get('degree')
            education.start_year = data.get('start_year')
            education.end_year = data.get('end_year')
            education.save()
            return JsonResponse({'message': 'Education updated successfully!'}, status=200)
        except Education.DoesNotExist:
            return JsonResponse({'error': 'Education not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

    

def education_create(request):
    if request.method == 'POST':
        institution_name = request.POST.get('institution_name')
        degree = request.POST.get('degree')
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')

        education = Education.objects.create(
            institution_name=institution_name,
            degree=degree,
            start_year=start_year,
            end_year=end_year
        ) 
        return JsonResponse({'success': True})  
    return render(request, 'education_create.html')


@csrf_exempt 
def delete_education(request, id):
    if request.method == 'DELETE':
        try:
            education = get_object_or_404(Education, id=id)
            education.delete()
            return JsonResponse({'success': True})
        except Education.DoesNotExist:
            return JsonResponse({'error': 'Education not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
 





def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'experience_list.html', {'experiences': experiences})


def experience_detail(request, id):
    experience = get_object_or_404(Experience, id=id)
    return render(request, 'experience_detail.html', {'experience':experience})


def experience_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        duration = request.POST.get('duration')

        experience = Experience.objects.create(
            title=title,
            start_date=start_date,
            end_date=end_date,
            duration=duration
        ) 
        return JsonResponse({'success': True})  
    return render(request, 'experience_create.html')
    

@csrf_exempt  
def experience_edit(request, id):
    if request.method == 'GET':
        experience = get_object_or_404(Experience, id=id)
        return render(request, 'experience_edit.html', {'experience': experience})
    
    if request.method == 'PUT':  
        data = json.loads(request.body)
        try:
            experience = Experience.objects.get(id=id)
            experience.title = data.get('title')
            experience.start_date = data.get('start_date')
            experience.end_date = data.get('end_date')
            experience.duration = data.get('duration')
            experience.save()
            return JsonResponse({'message': 'Experience info updated successfully!'}, status=200)
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'experience not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

   
@csrf_exempt 
def delete_experience(request, id):
    if request.method == 'DELETE':
        try:
            experience = get_object_or_404(Experience, id=id)
            experience.delete()
            return JsonResponse({'success': True})
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'experience not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt 
def edit_personalinfo(request):
    if request.method == 'GET':
        personal = get_object_or_404(PersonalInfo, id=id)
        print(personal)
        return render(request, 'edit_pi.html', {'personal': personal})

    if request.method == 'POST':
        return JsonResponse({'message': 'Personal info updated successfully!'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt 
def personal_detail(request):
    return render(request, 'edit_pi.html' )


@csrf_exempt 
def edit_contact(request):
    if request.method == 'GET':
        contact = get_object_or_404(Contact, id=id)
        print(contact)
        return render(request, 'contact_edit.html', {'contact': contact})

    if request.method == 'POST':
        return JsonResponse({'message': 'contact updated successfully!'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt 
def contact_detail(request):
    return render(request, 'contact_edit.html' )





# @csrf_exempt
# def edit_personalinfo(request):
#     if request.method == 'PUT':
#         nationality = request.POST.get('nationality')
#         religion = request.POST.get('religion')
#         marital_status = request.POST.get('marital_status')
#         address = request.POST.get('address')
#         contact = request.POST.get('contact')
#         country = request.POST.get('country')
#         state = request.POST.get('state')
#         zipcode = request.POST.get('zipcode')

#         personal_info = PersonalInfo(
#             nationality=nationality,
#             religion=religion,
#             marital_status=marital_status,
#             address=address,
#             contact=contact,
#             country=country,
#             state=state,
#             zipcode=zipcode
#         )
#         personal_info.save()
#         return JsonResponse({'status': 'success', 'message': 'Information updated successfully!'})
         



# def personal_detail(request, id):
#     personal = get_object_or_404(PersonalInfo, id=id)
#     print(personal)
    # return render(request, 'personal_detail.html', {'personal':personal})


# @csrf_exempt
# def update_profile(request):
#     if request.method == "POST":
#         # Get the data from the request
#         nationality = request.POST.get('nationality')
#         religion = request.POST.get('religion')
#         marital_status = request.POST.get('marital_status')
#         address = request.POST.get('address')
#         contact = request.POST.get('contact')
#         country = request.POST.get('country')
#         state = request.POST.get('state')
#         zipcode = request.POST.get('zipcode')

#         # Update the user's personal information
#         personal_info = PersonalInformation.objects.get(user=request.user)  # Adjust based on your user model
#         personal_info.nationality = nationality
#         personal_info.religion = religion
#         personal_info.marital_status = marital_status
#         personal_info.address = address
#         personal_info.contact = contact
#         personal_info.country = country
#         personal_info.state = state
#         personal_info.zipcode = zipcode
#         personal_info.save()

#         return JsonResponse({"message": "Profile updated successfully"})
#     return JsonResponse({"error": "Invalid request"}, status=400)





# def update_bank_info(request, id):
#     bank_info = get_object_or_404(BankInfo, id=id)
#     if request.method == 'POST':
#         bank_info.bank_name = request.POST.get('bank_name')
#         bank_info.account_number = request.POST.get('account_number')
#         bank_info.ifsc_code = request.POST.get('ifsc_code')
#         bank_info.pan_no = request.POST.get('pan_no')
#         bank_info.save()
#         return redirect('bank_info')  # Redirect to the list or detail page after updating
#     return HttpResponse("Invalid Request")


# @csrf_exempt 
# def update_user(request, id):
#     if request.method == 'PUT':
#         # emp_id = request.POST.get('modalEditTaxID')
#         id = '100-1001'
#         emp_id = id
#         try:
#             profile = Profile.objects.get(emp_id=emp_id)  # Retrieve the profile using emp_id
#             print(profile)
#         except Profile.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Employee not found.'})    
        
#         # data = json.loads(request.body)  # Use json.loads to get the data from PUT request
#         # first_name = data.get('modalEditUserFirstName')
#         # middle_name = data.get('modalEditUserMiddleName')
#         # last_name = data.get('modalEditUserLastName')
#         # designation = data.get('modalEditUserDeignation')
#         # blood_group = data.get('modalEditUserBlood')
#         # email = data.get('modalEditUserEmail')
#         # phone = data.get('modalEditUserPhone')
#         # emp_id = request.POST.get('emp_id')
#         first_name = request.POST.get('modalEditUserFirstName')
#         middle_name = request.POST.get('modalEditUserMiddleName')
#         last_name = request.POST.get('modalEditUserLastName')
#         designation = request.POST.get('modalEditUserDeignation')
#         blood_group = request.POST.get('modalEditUserBlood')
#         email = request.POST.get('modalEditUserEmail')
#         phone = request.POST.get('modalEditUserPhone')
#         # status = request.POST.get('modalEditUserStatus')
#         profile.name = f"{first_name} {middle_name} {last_name}"  # Example of combining names
#         profile.role = designation
#         profile.blood_group = blood_group
#         profile.email = email
#         profile.contact = phone
#         profile.save() 
#         return JsonResponse({'status': 'success', 'message': 'User information updated successfully!'})
        

# @csrf_exempt
# def update_user(request, id):
#     if request.method == 'PUT':
#         id = '100-1001'
#         try:
#             employee = Profile.objects.get(emp_id=id)
#             if not employee:
#                 return JsonResponse({"error": "Employee not found"})  # Adjust according to your field name
#             first_name = request.POST.get('modalEditUserFirstName')
#             middle_name = request.POST.get('modalEditUserMiddleName')
#             last_name = request.POST.get('modalEditUserLastName')
#             employee.role = request.POST.get('modalEditUserDeignation')
#             employee.blood_group = request.POST.get('modalEditUserBlood')
#             employee.email = request.POST.get('modalEditUserEmail')
#             employee.contact = request.POST.get('modalEditUserPhone')
#             # employee.status = request.POST.get('modalEditUserStatus')
#             employee.name = f"{first_name} {middle_name} {last_name}"
#             employee.save()
#             print(employee)
#             return JsonResponse({'status': 'success', 'message': 'Employee updated successfully.'})
#         except Profile.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Employee not found.'})
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


