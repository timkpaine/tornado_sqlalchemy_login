import tornado.web
import os.path
import tornado_sqlalchemy_login
from tornado_sqlalchemy_login.handlers import LogoutHandler
from mock import MagicMock


class TestLogout:
    def setup(self):
        settings = {
            "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            "login_url": "/login",
            "debug": "True",
            "template_path": os.path.join(os.path.dirname(tornado_sqlalchemy_login.__file__), 'assets'),
        }
        self.app = tornado.web.Application(**settings)
        self.app._transforms = []

    def test_LogoutHandler(self):
        req = MagicMock()
        req.body = ''
        context = {'users': {1234: ''},
                   'sessionmaker': MagicMock()}

        x = LogoutHandler(self.app, req, **context)
        x._transforms = []
        x._validate = lambda *args: True
        x.current_user = True
        x.get()
