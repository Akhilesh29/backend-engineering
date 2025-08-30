from celery import Celery
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_email(email):
    ## sending email logic
    print(f"Sending email to {email}")

if __name__ == '__main__':
    send_email.delay('user@example.com') 
