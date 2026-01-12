import random
import string

class UserHelper:
    def register_user_for_cleanup(request, token):
        if hasattr(request, 'instance') and request.instance is not None:
            if not hasattr(request.instance, 'created_users'):
                request.instance.created_users = []
            request.instance.created_users.append(token)
        else:
            if not hasattr(request, 'created_users'):
                request.created_users = []
            request.created_users.append(token)
            
    def get_login_password(created_user):
        login_pass = {
            "email": created_user['user_data']['email'],
            "password": created_user['user_data']['password']
        }
        return login_pass
    
def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string