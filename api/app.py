# from flask import Flask
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
# import os 
# from dotenv import load_dotenv
# # from flask_wtf.csrf import CSRFProtect
# load_dotenv()
# secret_key = os.getenv("SECRET_KEY")
# app = Flask(__name__)
# app.config['SECRET_KEY'] = secret_key


# # Initialize the Limiter with default limits
# limiter = Limiter(
#     get_remote_address,
#     app=app,
#     default_limits=["200 per day", "50 per hour"]
# )

# # Enable CSRF protection
# # csrf = CSRFProtect(app)
# if __name__ == "__main__":
#     from routes import *
#     # app.run()

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv
# from flask_wtf.csrf import CSRFProtect

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

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
    # app.run()
