class User:
    def __init__(self, email, age):
        self.email = email
        self.age = age
        self.active = True

    def deactivate(self):
        self.active = False
class AdminUser(User):
    def ban_user(self, user):
        user.deactivate()
u1 = User("user@mail.com", 20)
admin = AdminUser("admin@mail.com", 30)

admin.ban_user(u1)
print(u1.active)  # False
