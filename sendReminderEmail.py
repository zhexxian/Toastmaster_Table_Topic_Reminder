import smtplib
from getpass import getpass
from email.message import EmailMessage
from email.utils import make_msgid

def composeEmail():
    emailAddress = input("Enter email address: ")

    msg = EmailMessage()

    msg['Subject'] = "Toastmasters Table Topic"
    msg['From'] = emailAddress
    msg['To'] = [emailAddress]

    msg.set_content("""\
    Hi!
    This is a reminder to practice Toastmasters Table Topic :)
    List of topics: https://www.dist8tm.org/assets/tm--365-sample-table-topics-questions.pdf
    """)

    msg.add_alternative("""\
    <html>
        <head></head>
        <body>
            <p>Hi!</p>
            <p>This is a reminder to practice Toastmasters Table Topic :)</p>
            <p>List of topics: 
                <a>https://www.dist8tm.org/assets/tm--365-sample-table-topics-questions.pdf</a>
            </p>
        </body>
    </html>
    """, subtype='html')

    return emailAddress,msg

def sendEmail(emailAddress,msg):
    server = smtplib.SMTP('smtp-mail.outlook.com',587)
    server.starttls()
    try:
        password = getpass(prompt='Password: ', stream=None)
    except Exception as error:
        print('ERROR', error)
    else:
        server.login(emailAddress,password)
        server.send_message(msg)
        server.quit()
        print("Reminder email send successfully.")

if __name__ == "__main__":
    emailAddress,msg = composeEmail()
    sendEmail(emailAddress,msg)
