from Account.models import DeleteAccount
from django.test import TestCase
from Account.CreateAccount import CreateAccount
from Account.DeleteAccount import DeleteAccount
from Account.models import Account


class Test_DeleteAccount(TestCase):
    def setUp(self):
        pass