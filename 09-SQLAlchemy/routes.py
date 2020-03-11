from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User


@app.route('/', methods=['GET'])
def create_user():
    """Create a user."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing:
            return make_response(f'{username} ({email}) already created!')
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born n raised...",
                        admin=False)
        db.session.add(new_user)  # Add new User record to database
        db.session.commit()  # Commit all changes
    return make_response(f"{new_user} successfully created!")

# [MODEL].query.[METHOD_1].[METHOD_1].[FIRST or ALL]
#  .filter(conditions)
# order_by(mdoel, column)
# get() - by primary key
# .limit- max number of records

# . first
# .all

