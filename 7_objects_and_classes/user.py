class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_email(self, new_email):
        self.email = new_email
    
    def change_name(self, new_name):
        self.name = new_name
    
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as {self.current_job_title}. You can contact them at {self.email}")
        