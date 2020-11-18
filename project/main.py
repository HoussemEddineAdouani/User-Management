from flask import Blueprint, make_response, render_template, request
from flask_login import current_user, login_required
import pdfkit
from . import db, User

# Built of Blueprint for main
main = Blueprint('main', __name__)


@main.route('/')
def render_to_index():
    return render_template('index.html')

# To manage access and protect pages ==> @login_required
@main.route('/profile')
@login_required
def render_to_profile():
    return render_template('profile.html')


@main.route('/export_pdf/<user>')
def export_pdf(user):
    # Get the current user from the session.
    id__ = current_user.get_id()
    user = User.query.filter_by(id=id__).first()

    # Return the template as an object(String)
    res = render_template('template_pdf.html', user=user)
    # Generate PDF from the string
    response = pdfkit.from_string(res, False)
    response = make_response(response, False)

    # Manipulate the content
    response.headers['Content-type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline;file_name=output.pdf'

    return response


@main.route('/render_to_update/')
def render_to_update():
    return render_template('update_profile.html')


@main.route('/update', methods=['POST'])
def update():
    # Get the current user from the session.
    id__ = current_user.get_id()
    verify_user = User.query.filter_by(id=id__)

    first_name_ = request.form.get('first_name')
    last_name_ = request.form.get('last_name')
    email_ = request.form.get('email')
    password_ = request.form.get('password')
    direction_ = request.form.get('direction')

    verify_user.first_name = first_name_
    verify_user.last_name = last_name_
    verify_user.email = email_
    verify_user.password = password_
    verify_user.direction = direction_

    # Ensure the action of updating on the database
    db.session.commit()

    return render_template('profile.html', verify_user=verify_user)
