from Account.models import DeleteAccount


class DeleteAccount:

    """
    This method will create an account given a list of strings, "command"
        command[0] = deleteaccount
        command[1] = username
        command[2] = title

    If given valid values, the account will be deleted, fill the other fields to default values, and add it to the
    database. A confirmation message will be returned. If any arguments are invalid, an error message will be returned.
    """

    def deleteAccount(self, command):

        # Check that the command has the correct number of arguments
        if len(command) != 2:
            return "There are arguments missing, please enter your command in the following format: "
            "deleteaccount userName title"
