from src.user_db_connection import make_db_connection,admit_user
class user:
    def __init__(self,mobileNumber,userName,password):
        self.mobnumber=mobileNumber
        self.userName=userName
        self._passward=password
        admit_user(userName,password,mobileNumber)
    
    