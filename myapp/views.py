from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile



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



@csrf_exempt  # Use this decorator only if CSRF isn't automatically handled in your setup
def update_user_info(request):
    if request.method == 'POST':

        emp_id = request.POST.get('modalEditTaxID')
        first_name = request.POST.get('modalEditUserFirstName')
        middle_name = request.POST.get('modalEditUserMiddleName')
        last_name = request.POST.get('modalEditUserLastName')
        designation = request.POST.get('modalEditUserDeignation')
        blood_group = request.POST.get('modalEditUserBlood')
        email = request.POST.get('modalEditUserEmail')
        phone = request.POST.get('modalEditUserPhone')
        # status = request.POST.get('modalEditUserStatus')

        try:
            profile = Profile.objects.get(emp_id=emp_id)  # Retrieve the profile using emp_id
            profile.name = f"{first_name} {middle_name} {last_name}"  # Example of combining names
            profile.role = designation
            profile.blood_group = blood_group
            profile.email = email
            profile.contact = phone
            # profile.status = status
            # You can add more fields to update as necessary
            profile.save()  # Save the changes
            
            return JsonResponse({'status': 'success', 'message': 'User information updated successfully!'})
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Employee not found.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
        

    #     return JsonResponse({'status': 'success', 'message': 'User information updated successfully!'})
    # return JsonResponse({'status': 'error', 'message': 'Invalid request'})





# @csrf_exempt
# def update_user_info(request):
#     if request.method == 'POST':
#         tax_id = request.POST.get('modalEditTaxID')

#         try:
#             employee = Profile.objects.get(emp_id=tax_id).first()
#             if not employee:
#                 return JsonResponse({"error": "Employee not found"})  # Adjust according to your field name
#             # Update the employee fields with the new data
#             employee.first_name = request.POST.get('modalEditUserFirstName')
#             employee.middle_name = request.POST.get('modalEditUserMiddleName')
#             employee.last_name = request.POST.get('modalEditUserLastName')
#             employee.role = request.POST.get('modalEditUserDeignation')
#             employee.blood_group = request.POST.get('modalEditUserBlood')
#             employee.email = request.POST.get('modalEditUserEmail')
#             employee.contact = request.POST.get('modalEditUserPhone')
#             # employee.status = request.POST.get('modalEditUserStatus')
#             employee.save()

#             return JsonResponse({'status': 'success', 'message': 'Employee updated successfully.'})
#         except Profile.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Employee not found.'})

#     return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


