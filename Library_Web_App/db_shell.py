# exec(open(r"C:\Users\dell\.vscode\Library_Project\Library_Web_App\db_shell.py").read())

from django.contrib.auth.models import User

# print(User.objects.all())

# User.objects.create(username = "Aryan", password = "aryan@123", email = "aryan@gmail.com") # Creating user by using only create wont encrypt the password So its essential to use createuser all time.


# User.objects.create_user(username = "Rajesh", password="Rajesh@123", first_name = "Rajesh", last_name = "Singh", email="raj@gmail.com")


from django.utils.crypto import get_random_string
print(get_random_string(6))