from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #附加路由和自定义的页面
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
