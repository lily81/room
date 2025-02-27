from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager  # 导入 LoginManager

db = SQLAlchemy()
socketio = SocketIO()
login_manager = LoginManager()  # 初始化 LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # 从config.py加载配置

    # 初始化扩展
    db.init_app(app)
    socketio.init_app(app)
    login_manager.init_app(app)  # 初始化 flask-login

    # 注册蓝图
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

# 添加用户加载器
from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))