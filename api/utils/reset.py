from api.database import get_database

def reset_password(email, password):
    """
    Resets the password for the specified email address in the database.

    Args:
        email (str): The email address for which the password needs to be reset.
        password (str): The new password to be set.

    Returns:
        dict: A JSON response indicating success or failure.

    Updates the password in the "otp_verification" collection for the specified email.
    If an exception occurs, returns a JSON response with the error message.
    """
    try:
        db = get_database()
        db["users_details"].update_one({"_id": email}, {"$set": {"password": password}})
    except Exception as e:
        return {"error": str(e)}
