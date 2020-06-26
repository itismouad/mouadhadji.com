from flask import Flask
from flask_bootstrap import Bootstrap
from jinja2 import Environment, PackageLoader, TemplateNotFound
from .config import Config

# Initialize app
app = Flask(__name__)

# import routes
from . import routes

# Configuration
app.config.from_object(Config)

# Loading
env = Environment(loader=PackageLoader('blog', 'templates'))

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html')
