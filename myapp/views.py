from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile, BankInfo, Education
import json


def holiday_page(request):
    return render(request, 'holidays.html')


def profile(request):
    return render(request, 'profile.html')


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
    # Fetch all banks from the database
    banks = BankInfo.objects.all()
    return render(request, 'bank_list.html', {'banks': banks})


def bank_detail(request, id):
    bank = get_object_or_404(BankInfo, id=id)
    return render(request, 'bank_detail.html', {'bank':bank})


def bank_create(request):
    if request.method == 'POST':
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        ifsc_code = request.POST.get('ifsc_code')
        pan_no = request.POST.get('pan_no')

        # Create the bank record
        bank = BankInfo.objects.create(
            bank_name=bank_name,
            account_number=account_number,
            ifsc_code=ifsc_code,
            pan_no=pan_no
        ) 
        return JsonResponse({'success': True})  
    return render(request, 'bank_create.html')
    

@csrf_exempt  
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
 


def education_detail(request, id):
    education = get_object_or_404(Education, id=id)
    return render(request, 'education_detail.html', {'education': education})

















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


