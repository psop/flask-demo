from flask import render_template, request
from app.models.users import User, _create

class views:
    def index():
        return render_template('users/index.html')

    def new():
        user = User()
        return render_template('users/new.html')

    def create():
        username = request.form['username']
        email = request.form['email']
        _create(username, email)
        # call back
        return "User creation sucessful!"

    def edit(id):
        user = User.query.filter_by(id=id).first()
        return render_template('users/edit.html',user=user)
