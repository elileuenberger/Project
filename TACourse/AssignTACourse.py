from TACourse.models import TACourse
from Account.models import Account
from Course.models import Course


class AssignTACourse:

    def assignTACourse(self, command):
        if len(command) != 3:
            return "Your command has an incorrect number of arguments, please enter your command in the following format: " \
                   "assignTACourse userName classNumber"

        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid TA username."

        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number."

        ta = Account.objects.get(userName=command[1])

        if ta.title > 1:
            return "Account is not a TA."

        course = Course.objects.get(number=command[2])

        if TACourse.objects.filter(TA=ta, Course=course).exists():
            return str(ta) + " is already assigned to " + str(course)

        l = TACourse()
        l.TA = ta
        l.Course = course
        l.save()

        return "Assignment successful."
