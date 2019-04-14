from django.shortcuts import render
from django.views import View
from CurrentUserHelper import CurrentUserHelper
# Create your views here.


class adminPage(View):

    def get(self, request):
        return render(request, 'Accounts/AdminHome.html')


class supervisorPage(View):

    def get(self, request):
        return render(request, 'Accounts/SupervisorHome.html')


class instructorPage(View):

    def get(self, request):
        CUH = CurrentUserHelper()
        Account = CUH.getCurrentUser()
        return render(request, 'Accounts/InstructorHome.html', {"Account": Account})

class taPage(View):

    def get(self, request):
        CUH = CurrentUserHelper()
        Account = CUH.getCurrentUser()
        return render(request, 'Accounts/TaHome.html', {"Account": Account})

class createAccount(View):

    def get(self, request):
        return render(request, 'createAccount.html')

    def post(self, request):

        userName = str(request.POST["username"])
        firstName = str(request.POST["firstname"])
        lastName = str(request.POST["lastname"])
        password = str(request.POST["password"])
        email = str(request.POST["email"])
        title = str(request.POST["title"])
        address = str(request.POST["address"])
        city = str(request.POST["city"])
        state = str(request.POST["state"])
        zipCode = str(request.POST["zipcode"])
        officeNumber = str(request.POST["officenumber"])
        officePhone = str(request.POST["officephone"])
        officeDays = str(request.POST["officeday"])
        officeHoursStart = str(request.POST["officehourstart"])
        officeHoursEnd = str(request.POST["officehoursend"])
        currentUser = str(request.POST["dfshjkhljfds"])

        try:
            message = command = ["", userName, title, email, firstName, lastName, password, address, city, state, zipCode, officeNumber, officePhone, officeDays, officeHoursStart, officeHoursEnd]
            return render(request, 'loginscreen.html', {"message": message})
        except Exception as e:
            return render(request, 'loginscreen.html', {"message": str(e)})
