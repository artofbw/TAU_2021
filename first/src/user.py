class User:
    def __init__(self, first_name, last_name, is_active=False, salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.salary = salary

    def get_first_name(self):
        if not self.first_name:
            raise ValueError("first name cannot be empty")
        return self.first_name

    def get_last_name(self):
        if not self.last_name:
            raise ValueError("last name cannot be empty")
        return self.last_name

    def is_rich(self):
        if self.salary > 100:
            return "user is rich"
        else:
            return "user is poor"
