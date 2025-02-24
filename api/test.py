# import requests

# BASE_URL = "http://localhost:5000"

# def test_index():
#     response = requests.get(f"{BASE_URL}/")
#     assert response.status_code == 200
#     print("Index route passed")

# def test_signup():
#     payload_valid = {
#         "email": "test@example.com",
#         "password": "Test@1234",
#         "confirmpassword": "Test@1234"
#     }
#     payload_missing_fields = {
#         "email": "test@example.com"
#     }
#     payload_invalid_email = {
#         "email": "invalidemail",
#         "password": "Test@1234",
#         "confirmpassword": "Test@1234"
#     }
#     payload_invalid_password = {
#         "email": "test@example.com",
#         "password": "short",
#         "confirmpassword": "short"
#     }

#     response = requests.post(f"{BASE_URL}/signup", json=payload_valid)
#     assert response.status_code in [200, 400], response.text
#     print("Valid signup passed")

#     response = requests.post(f"{BASE_URL}/signup", json=payload_missing_fields)
#     assert response.status_code == 400, response.text
#     print("Signup with missing fields passed")

#     response = requests.post(f"{BASE_URL}/signup", json=payload_invalid_email)
#     assert response.status_code == 400, response.text
#     print("Signup with invalid email passed")

#     response = requests.post(f"{BASE_URL}/signup", json=payload_invalid_password)
#     assert response.status_code == 400, response.text
#     print("Signup with invalid password passed")

# def test_login():
#     payload_valid = {
#         "email": "test@example.com",
#         "password": "Test@1234"
#     }
#     payload_missing_fields = {
#         "email": "test@example.com"
#     }
#     payload_invalid_email = {
#         "email": "invalidemail",
#         "password": "Test@1234"
#     }
#     payload_invalid_password = {
#         "email": "test@example.com",
#         "password": "WrongPassword"
#     }

#     response = requests.post(f"{BASE_URL}/login", json=payload_valid)
#     assert response.status_code in [200, 400], response.text
#     print("Valid login passed")

#     response = requests.post(f"{BASE_URL}/login", json=payload_missing_fields)
#     assert response.status_code == 400, response.text
#     print("Login with missing fields passed")

#     response = requests.post(f"{BASE_URL}/login", json=payload_invalid_email)
#     assert response.status_code == 400, response.text
#     print("Login with invalid email passed")

#     response = requests.post(f"{BASE_URL}/login", json=payload_invalid_password)
#     assert response.status_code == 400, response.text
#     print("Login with invalid password passed")

# def test_forget_password():
#     payload_missing_email = {
#         "action": "reset_password",
#         "password": "NewPassword@1234"
#     }
#     payload_invalid_email = {
#         "email": "invalidemail",
#         "action": "reset_password",
#         "password": "NewPassword@1234"
#     }
#     payload_user_not_found = {
#         "email": "nonexistent@example.com",
#         "action": "reset_password",
#         "password": "NewPassword@1234"
#     }
#     payload_missing_password = {
#         "email": "test@example.com",
#         "action": "reset_password"
#     }
#     payload_valid = {
#         "email": "test@example.com",
#         "action": "reset_password",
#         "password": "NewPassword@1234"
#     }

#     response = requests.put(f"{BASE_URL}/forget_password", json=payload_missing_email)
#     assert response.status_code == 400, response.text
#     print("Forget Password with missing email passed")

#     response = requests.put(f"{BASE_URL}/forget_password", json=payload_invalid_email)
#     assert response.status_code == 400, response.text
#     print("Forget Password with invalid email passed")

#     response = requests.put(f"{BASE_URL}/forget_password", json=payload_user_not_found)
#     assert response.status_code == 404, response.text
#     print("Forget Password with user not found passed")

#     response = requests.put(f"{BASE_URL}/forget_password", json=payload_missing_password)
#     assert response.status_code == 400, response.text
#     print("Forget Password with missing password passed")

#     response = requests.put(f"{BASE_URL}/forget_password", json=payload_valid)
#     assert response.status_code in [200, 400], response.text
#     print("Forget Password with valid data passed")

# if __name__ == "__main__":
#     test_index()
#     test_signup()
#     test_login()
#     test_forget_password()
