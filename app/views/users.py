from flask import render_template


class views:
    def index():
        return render_template('users/index.html')
