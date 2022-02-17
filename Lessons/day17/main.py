
class User():
    def __init__(self, idnum:int, name:str):
        self.id = idnum
        self.username = name
        self.followers = 0
        self.following = 0

    def get_name(self,id:int):
        return self.username

    def get_id(self, name:str):
        return self.id 

    def follow_user(self,user):
        user.followers += 1
        self.following += 1


user_1 = User(1,"Secho")
user_2 = User(2,"Silvaeth")
print(f"User ID: {user_1.id} \nUser Name: {user_1.username}")

user_1.follow_user(user_2)

print(user_1.followers)
print(user_1.following)
print()
print(user_2.followers)
print(user_2.following)
