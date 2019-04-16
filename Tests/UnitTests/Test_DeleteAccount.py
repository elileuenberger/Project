from Account.models import DeleteAccount
from django.test import TestCase
from Account.CreateAccount import CreateAccount
from Account.DeleteAccount import DeleteAccount
from Account.models import Account


class Test_DeleteAccount(TestCase):
    def setUp(self):
        self.DA = DeleteAccount()
        self.account1 = Account.objects.create(userName="cheng41", title="2")
        self.account2 = Account.objects.create(userName="suzuki15", title="2")
        self.account3 = Account.objects.create(userName="spykim2003", title="1")
        Account.objects1.remove()
        Account.objects2.remove()
        Account.objects3.remove()

    def test_DeleteAccount_successfully_created(self):
        self.assertEqual(self.DA.DeleteAccount(["deleteaccount", "cheng41", "2"]),
                         "Account successfully deleted")
        self.assertEqual(self.DA.DeleteAccount(["deleteaccount", "suzuki15", "2"]),
                         "Account successfully deleted")
        self.assertEqual(self.DA.DeleteAccount(["deleteaccount", "spykim2003", "1"]),
                         "Account successfully deleted")

    def test_DeleteAccount_no_username_found(self):
        self.assertEqual(self.AI.assignInst(["deleteaccount", "spykim2003", "2"]),
                         "Invalid user name")
        self.assertEqual(self.AI.assignInst(["deleteaccount", "eonshik", "1"]),
                         "Invalid user name")