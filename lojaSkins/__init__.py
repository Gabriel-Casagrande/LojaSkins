from flask import Flask
from routes.home import home_route
from routes.usuarios import usuarios_route

app = Flask(__name__)
app.config['SECRET_KEY']='dev'

app.register_blueprint(home_route)
app.register_blueprint(usuarios_route, url_prefix='/usuarios')



app.run(debug=True)