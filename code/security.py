from models.user import UserModel
import hmac

def authenticate(username: str, password: str):
    user = UserModel.find_by_username(username)
    # safe_str_cmp() deprecated
    if user and hmac.compare_digest(user.password, password):
        return user

# Takes in content of JWT, extract
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
    
