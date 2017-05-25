from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session as login_session,
    redirect,
    url_for,
    jsonify
)

aboutBase = Blueprint('about', __name__, url_prefix='')

'''
    Set the route and accepted methods About
'''


@aboutBase.route('/', methods=['GET'])
def showAbout():
    return render_template("about/about.html")