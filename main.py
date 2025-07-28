#region Libraries
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import LoginManager, UserMixin, login_user, login_required
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
#endregion

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

# Define a User class for user authentication
class User(UserMixin):
    def __init__(self, email):
        self.id = email

# Load a user by their user ID (used for authentication)
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Create an empty list to store customer emails
customer_emails = []

# Store the user's email address for login
user_email = ''

book = ''

# Function to fetch emails from the API and store them in the emails list
import requests

def get_emails(product_id):
    global customer_emails

    customer_emails = []
    page = 1

    while True:
        headers = {
            "accept": "application/json",
            "authorization": "Bearer API_KEY"  # Add your actual API key here
        }

        params = {
            "limit": 50,
            "page": page,
            "sort": "dateDesc",
            "productId": product_id
        }

        response = requests.get("https://api.shopier.com/v1/orders", headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            if not data:
                break

            for order in data:
                email = order["shippingInfo"]["email"]
                customer_emails.append(email)

            page += 1
        else:
            print("API request failed:", response.status_code)
            break

    return customer_emails

@app.route('/')
def main():
    # Redirect to the main.html page on opening the app
    return render_template('main.html')

# Function to create a verification code
def create_verification_code():
    return str(random.randint(1000, 9999))

@app.route('/check', methods=['POST'])
def send_code_to_mail():
    # Get the user's input email
    global user_email
    user_email = request.form.get('txtEmail', '')

    if user_email in customer_emails:
        global app
        app.secret_key = create_verification_code()

        # Send a verification code to the email upon success
        def send_email(subject, body, to_email):
            from_email = "YOUR_GMAIL"  # Sender's email address
            password = "YOUR_PASSWORD_OF_GMAIL"  # Email password

            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # SMTP settings for Gmail
            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()

        subject = "\U0001FAE1" + " YOUR_MESSAGE"  # Customize your message
        body = f"Verification Code: {app.secret_key}"
        # It could be a Gmail, Outlook, or Hotmail address.
        to_email = user_email
        send_email(subject, body, to_email)

        # Open the page where the user can enter the verification code
        return render_template('verification.html')
    else:  # If the email is not registered in the system
        # Redirect to a page saying 'Failed'
        return render_template('error_page.html', message="The email you entered is not registered among the orders.")

@app.route('/login')
def login():
    global customer_emails
    global book

    book = request.args.get('book')  # Get the value of the 'book' parameter

    if book == 'firstbook':
        # Fetch emails (runs when the app is started)
        all_customer_emails = get_emails("YOUR_PRODUCT_ID")

    elif book == 'secondbook':
        all_customer_emails = get_emails("YOUR_PRODUCT_ID")
    else:
        abort(403)

    return render_template('login.html')

@app.route('/verification', methods=['POST'])
def check_verification():
    global app
    entered_code = request.form['verification_code']

    if entered_code == app.secret_key:
        user = User(user_email)  # Create a user object
        login_user(user)  # Mark the user as logged in

        if book == 'firstbook':
            return redirect(url_for('firstbook'))

        elif book == 'secondbook':
            return redirect(url_for('second book'))
        
        else:
            abort(403)

    else:
        return render_template('error_page.html', message="The verification code you entered is incorrect.")

@app.route('/firstbook')
@login_required
def firstbook():
    return render_template('firstbook.html')

# For security, block access to firstbook.pdf
@app.route('/static/firstbook.pdf')
@login_required
def block_firstbook_access():
    abort(403)  # Access denied

@app.route('/secondbook')
@login_required
def secondbook():
    return render_template('secondbook.html')

# For security, block access to 2ndbook.pdf
@app.route('/static/secondbook.pdf')
@login_required
def block_secondbook_access():
    abort(403)  # Access denied

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
