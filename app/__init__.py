<<<<<<< HEAD
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
=======
from flask import Flask, request, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging 
from logging.handlers import SMTPHandler, RotatingFileHandler
import os 
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from elasticsearch import Elasticsearch
<<<<<<< HEAD
from config import Config
from redis import Redis
import rq #not sure why here we only use 'import'

=======

#have removed app from the block of code below
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
<<<<<<< HEAD
    migrate.init_app(app, db)
=======
    migrate.init_app(app,db)
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
<<<<<<< HEAD
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
    app.redis = Redis(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('microblog-tasks', connection=app.redis)
=======

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

<<<<<<< HEAD
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
=======
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
<<<<<<< HEAD
                auth = (app.config['MAIL_USERNAME'],
                        app.config['MAIL_PASSWORD'])
=======
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
<<<<<<< HEAD
                toaddrs=app.config['ADMINS'], subject='Microblog Failure',
=======
                toaddrs=app.config['ADMINS'], subject='Anotherblog Failure',
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

<<<<<<< HEAD
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
=======
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/anotherblog.log',
                                                maxBytes=10240, backupCount=10)
            file_handler.serFormatter(logging.Formatter(
                '%(asctime)s%(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Anotherblog startup')

    return app
        
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/anotherblog.log', maxBytes=10240,
                                            backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
<<<<<<< HEAD
        app.logger.info('Microblog startup')

    return app


=======
        app.logger.info('Anotherblog startup')

    return app

>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

<<<<<<< HEAD

=======
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
from app import models


