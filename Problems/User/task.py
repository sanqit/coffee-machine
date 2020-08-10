class User:
    n_active = 0
    users = []

    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name

        if self.active:
            User.n_active += 1

        User.users.append(self)
