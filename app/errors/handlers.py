<<<<<<< HEAD
from flask import render_template, request
from app import db
from app.errors import bp #I've added this, but there is no explanation in the tutorial as to why
from app.api.errors import error_response as api_error_response

def wants_json_response():
    return request.accept_mimetypes['application/json']  >= \
        request.accept_mimetypes['text/html']

@bp.app_errorhandler(404)
def not_found_error(error):
    if wants_json_response():
        return api_error_response(404)
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):    
    db.session.rollback()
    if wants_json_response():
        return api_error_response(500)
=======
from flask import render_template
from app import db
from app.errors import bp #I've added this, but there is no explanation in the tutorial as to why

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
    return render_template('errors/500.html'), 500