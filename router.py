from app import app
from app.views.users import views

@app.route('/',methods=['GET'])
def index():
    return views.index()

@app.route('/new',methods=['GET'])
def new():
    return views.new()

@app.route('/create',methods=['POST'])
def create():
    return views.create()
