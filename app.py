import os
from flask import Flask, current_app,Blueprint
from flask_mysqldb import MySQL
from auth.route import user_bp #, select_bp, api_bp
from flask_restx import Api


app = Flask(__name__)
mysql = MySQL(app)

sw_blueprint = Blueprint("api", "__name__", url_prefix = "/api")
api = Api(sw_blueprint,
          title="Example API application",
          description="An example API application using flask-restx",
          version="1.0",
          doc="/swagger/",
          validate=True
          )


# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_DB'] = 'bookingplatform'

app.config['MYSQL_USER'] = 'dfrsrhnzda'
app.config['MYSQL_PASSWORD'] = 'd3w9Cpaz3Hqq$0gB'
app.config['MYSQL_HOST'] = 'laboratory-work-server.mysql.database.azure.com'
app.config['MYSQL_DB'] = 'bookingplatform'

app.config['MYSQL_SSL_DISABLED'] = True

app.mysql = mysql


app.register_blueprint(sw_blueprint)
#app.register_blueprint(user_bp)

api.add_namespace(user_bp)


# lab4
#app.register_blueprint(select_bp)

# lab5
#app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
