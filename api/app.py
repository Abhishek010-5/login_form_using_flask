from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from api.config import SECRET_KEY
# from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize the Limiter with default limits
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

limiter.init_app(app)

# Enable CSRF protection
# csrf = CSRFProtect(app)

from api.routes import *
# if __name__ == "__main__":
#     app.run()
