from flask import render_template


class views:
    def index():
        return render_template('users/index.html')

    def new():
        return render_template('users/new.html')
