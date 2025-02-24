from pymongo import errors
import re
from api.database import get_database

db = get_database()

def validate_email(email: str):
    """
    Validates the given email address using a regular expression pattern.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    return True


def validate_password(password: str):
    """
    Validates the given password based on the following criteria:
    - At least 8 characters long
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*)

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password meets the criteria, False otherwise.
    """
    password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$')
    if len(password) < 8 or not password_regex.match(password):
        return False
    return True


def validate_user_mail(email):
    """
    Validates if the given email address exists in the "users_details" collection.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email exists in the collection, False otherwise.

    Handles `ServerSelectionTimeoutError` and prints an error message if the MongoDB server cannot be reached.
    """
    try:
        # Attempt to retrieve a document with the given email as the _id
        document = db["users_details"].find_one({"_id": email})
        
        # Check if document was found
        return document is not None

    except errors.ServerSelectionTimeoutError:
        print("Could not connect to MongoDB server.")
        return False

def validate_user_password(email, password):
    """
    Validates if the given password matches the one stored in the "users_details" collection for the specified email.

    Args:
        email (str): The email address to be validated.
        password (str): The password to be validated.

    Returns:
        bool: True if the email exists and the password matches, False otherwise.

    Handles `ServerSelectionTimeoutError` and prints an error message if the MongoDB server cannot be reached.
    """
    try:
        # Attempt to retrieve a document with the given email as the _id
        document = db["users_details"].find_one({"_id": email})
        
        # Check if document was found and if the password matches
        if document is not None:
            return document["password"] == password
        else:
            return False
    except errors.ServerSelectionTimeoutError:
        print("Could not connect to MongoDB server.")
        return False

def validate_user_otp(email):
    """
    Validates if the given email address exists in the "users_details" collection.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email exists in the collection, False otherwise.

    Handles `ServerSelectionTimeoutError` and prints an error message if the MongoDB server cannot be reached.
    """
    try:
        # Attempt to retrieve a document with the given email as the _id
        document = db["otp_verification"].find_one({"_id": email})
        
        # Check if document was found
        return document is not None

    except errors.ServerSelectionTimeoutError:
        print("Could not connect to MongoDB server.")
        return False