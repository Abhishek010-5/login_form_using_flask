import random
from flask import jsonify, request
from api.database import get_database
import datetime

db = get_database()

def verify_otp(email, otp):
    """
    Verifies the OTP for the specified email address.

    Args:
        email (str): The email address to verify the OTP for.
        otp (int): The OTP to be verified.

    Returns:
        bool: True if the OTP is valid and has not expired, False otherwise.

    Deletes the OTP record from the database if the OTP is valid and not expired.
    If an exception occurs, returns a JSON response with the error message.
    """
    try:
        record = db["otp_verification"].find_one({"_id": email})

        if not record:
            return False

        if record["otp"] == int(otp) and datetime.datetime.utcnow() <= record["otp_expiry"]:
            db["otp_verification"].delete_one({"_id": email})
            return True
        else:
            return False

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_otp():
    """
    Generates a random 6-digit OTP.

    Returns:
        int: A randomly generated 6-digit OTP.
    """
    return random.randint(100000, 999999)
