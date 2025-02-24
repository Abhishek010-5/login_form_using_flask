from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os 
from dotenv import load_dotenv
# from flask_wtf.csrf import CSRFProtect
load_dotenv()
secrect_key = os.getenv("SECRECT_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = secrect_key


# Initialize the Limiter with default limits
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Enable CSRF protection
# csrf = CSRFProtect(app)
from routes import *
# if __name__ == "__main__":
    # app.run()