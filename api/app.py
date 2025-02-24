from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
# from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the Limiter with default limits
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Enable CSRF protection
# csrf = CSRFProtect(app)
# from routes import *
@app.route("/")
def home():
    return "This is home page"
# if __name__ == "__main__":
    # app.run()