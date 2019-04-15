from django.shortcuts import render
from django.views import View
from Account.models import Account
from ViewCourseAssign.models import viewCourseAssign
# Create your views here.


class viewAssign(View):

    def get(self, request):
        taList = Account.objects.filter(title=1)
        return render(request, 'viewAssignments.html', {"taList": taList})

    def post(self, request):
        taList = Account.objects.filter(title=1)
        account = str(request.POST["taAccount"])

        command = ["", account]

        vca = viewCourseAssign()

        message = vca.viewCourseAssign(command)

        return render(request, 'viewAssignments.html', {"assignments": message, "taList": taList})
