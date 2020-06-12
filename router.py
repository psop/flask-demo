from app import app
from app.views.users import views

@app.route('/',methods=['GET'])
def index():
    return views.index()


