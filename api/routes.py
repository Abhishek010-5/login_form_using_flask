from flask import request, jsonify, render_template, redirect, url_for, session
import hashlib
from api.utils.email_utils import send_otp, send_otp_to_db
from api.utils.otp_utils import generate_otp, verify_otp
from api.validations.validation_utils import validate_email, validate_password, validate_user_mail, validate_user_password
from api.database import get_database
from api.utils.reset import reset_password
from functools import wraps
from api.app import limiter, app
from api.config import API_KEY

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:  # Check if user is logged in
            return redirect(url_for('index'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

def require_api_key(view_function):
    def decorated_function(*args, **kwargs):
        api_key = request.args.get('x-api-key')
        if api_key == API_KEY:
            return view_function(*args, **kwargs)
        else:
            return jsonify({"error":"Unauthorized"}), 401
    return decorated_function

# Route for landing page
@app.route("/")
@require_api_key
def landing_page():
    # return redirect(url_for("index"))
    return render_template("landing_page.html")

# Route for index page
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("login_and_signup.html")

# Route for signup
@app.route("/signup", methods=["POST"])
def signup():
    try:
        db = get_database()
        data = request.get_json()
        action =  data.get("action")
        otp =  data.get("otp")
        name = data.get("fullname")
        email = data.get("email")
        password = data.get("password")
        conf_password = data.get("confirmPassword")
        
    
        if not validate_email(email):
            return jsonify({"error": "Invalid email address"}), 400

        if validate_user_mail(email):
            return jsonify({"error": "User already exists"}), 400
        
        if action == "send_otp":
            gen_otp = generate_otp()
            send_otp_to_db(email, gen_otp)
            send_otp(email, gen_otp)
            return jsonify({"message": "OTP sent successfully"})
        
        # Validation checks
        if not email or not password or not conf_password:
            return jsonify({"error": "Email, password, and confirmation password are required"}), 400


        if not validate_password(password):
            return jsonify({"error": "Invalid password"}), 400

        if password != conf_password:
            return jsonify({"error": "Passwords do not match"}), 400
                
        if not verify_otp(email, otp):
            return jsonify({"error": "Invalid OTP"}), 400

        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

        db["users_details"].insert_one({"_id": email, "password": hashed_password, "user_name": name})

        return jsonify({"email": email, "message": "User registered successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Route for login
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        
        # Validation checks
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

        if not validate_email(email):
            return jsonify({"error": "Invalid email address"}), 400

        if validate_user_password(email, hashed_password):
            session['email'] = email  # Store email in session for login state
            return redirect(url_for("home"))
        else:
            return jsonify({"error": "Invalid email or password"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for home page (protected)
@app.route("/home")
@login_required
def home():
    return render_template("home.html")

# Route for forgot password page
@app.route("/forgot_password", methods=["GET"])
def forgot_password_page():
    return render_template("forget_password.html")

# Route for password reset (with OTP)
@app.route("/forget_password", methods=["PUT"])
@limiter.limit("3 per minute")  # Rate limiting for security
def forget_password():
    try:
        data = request.get_json()
        action = data.get("action")
        email = data.get("email")

        if not email:
            return jsonify({"error": "Email is required"}), 400
        if not validate_email(email):
            return jsonify({"error": "Enter a valid email address"}), 400
        
        if not validate_user_mail(email):
            return jsonify({"error": "User not found"}), 404

        if action == "send_otp":
            gen_otp = generate_otp()
            send_otp_to_db(email, gen_otp)
            send_otp(email, gen_otp)
            return jsonify({"message": "OTP sent successfully"})

        if action == "reset_password":
            otp = data.get("otp")
            password = data.get("password")

            if not otp:
                return jsonify({"error": "OTP is required"}), 400
            if not password:
                return jsonify({"error": "Password is required"}), 400

            if not validate_password(password):
                return jsonify({"error": "Invalid password"}), 400
            
            if not verify_otp(email, otp):
                return jsonify({"error": "Invalid OTP"}), 400

            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            reset_password(email, hashed_password)

            return jsonify({"message": "Password updated successfully"})
        return  redirect(url_for("index"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Route for logout
@app.route("/logout",methods=["POST"])
def logout():
    session.pop('email', None) 
    return redirect(url_for("index"))  




