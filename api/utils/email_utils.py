import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from api.database import get_database
from datetime import datetime, timedelta
from api.validations.validation_utils import validate_user_otp
from api.config import PASSWORD, MAIL

def send_otp(email, otp):
    """
    Sends an OTP to the specified email address.

    Args:
        email (str): The recipient's email address.
        otp (str): The OTP to be sent.

    Sends the OTP via email using SMTP.
    """
    sender_email = MAIL
    sender_password = PASSWORD
    subject = "Your OTP Code"
    body = f"Your OTP code is {otp}. It is valid for 10 minutes."

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Use port 1025 for the local SMTP server
        server.starttls()  # Remove this line if using a simple local SMTP server without TLS
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
        

def send_otp_to_db(email, otp):
    """
    Stores the OTP and its expiry time in the database.

    Args:
        email (str): The recipient's email address.
        otp (str): The OTP to be stored.

    Stores the OTP in the 'otp_verification' collection with an expiry time of 10 minutes from the current time.
    If the email already exists in the database, updates the existing document with the new OTP and expiry time.
    """
    db = get_database()
    curr_time = datetime.now()
    new_time = curr_time + timedelta(minutes=10)
    if not validate_user_otp(email):  # Ensure you pass the email parameter to the validation function
        document = {"_id": email, "otp": otp, "otp_expiry": new_time}
        db["otp_verification"].insert_one(document)
    else:
        db["otp_verification"].update_one({"_id": email}, {"$set": {"otp": otp, "otp_expiry": new_time}})
