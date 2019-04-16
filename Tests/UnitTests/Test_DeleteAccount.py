
from django.test import TestCase
from Account.DeleteAccount import DeleteAccount
from Account.models import Account


class Test_DeleteAccount(TestCase):
    def setUp(self):
        self.DA = DeleteAccount()
        self.account1 = Account.objects.create(userName="cheng41", title="2")
        self.account2 = Account.objects.create(userName="suzuki15", title="2")
        self.account3 = Account.objects.create(userName="henry53", title="1")
        #Account.objects1.remove()
        #Account.objects2.remove()
        #Account.objects3.remove()

    def test_DeleteAccount_successfully_created(self):
        self.assertEqual(self.DA.deleteAccount("cheng41"), "Account successfully deleted")
        self.assertEqual(self.DA.deleteAccount("suzuki15"),"Account successfully deleted")
        self.assertEqual(self.DA.deleteAccount("spykim2003"),"Account successfully deleted")

   # def test_DeleteAccount_no_username_found(self):
    #    self.assertEqual(self.DA.assignInst(["deleteaccount", "spykim2003", "2"]),
     #                    "Invalid user name")
      #  self.assertEqual(self.DA.assignInst(["deleteaccount", "eonshik7", "1"]),
       #                  "Invalid user name")