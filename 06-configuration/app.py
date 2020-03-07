from flask import Flask
app = Flask(__name__)

app.config.from_object('config.Config')      # Config from object
app.config.from_envvar('APP_CONFIG')         # Config from filepath in env
app.config.from_pyfile('application.cfg',
                       silent=True)          # Config from cfg file