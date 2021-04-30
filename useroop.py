class User:
    pass

    # constructor is called everytime the user object is created
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # uninitialized attributes with default value
        self.followers = 0
        self.following = 0

    def set_followers(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "ssharm02")
user_2 = User("002", "buddy")

user_1.set_followers(user_2)
print(user_1.username, user_1.id, user_1.followers)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)