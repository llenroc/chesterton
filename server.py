import tornado.web
import tornado.ioloop
import tornado.options
import tornado.escape
from tornado.options import options, define
from tornado.autoreload import watch

from gino.ext.tornado import Gino, Application, GinoRequestHandler

import json
from jinja2 import Environment, FileSystemLoader
import fast_arrow as fa


import configparser
config_file = "config.dev.ini"
config = configparser.ConfigParser()
config.read(config_file)
username = config['account']['username']
password = config['account']['password']
fa_client = fa.Client(username=username, password=password)
result = fa_client.authenticate()

env = Environment(loader=FileSystemLoader('templates'))

db = Gino()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode(), nullable=False)


class BaseHandler(GinoRequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        self.set_status(204)
        self.finish()

    def render_json(self, data):
        self.write(json.dumps(data))
        self.finish()

    def render_template(self, template):
        self.write(template.render({
            'assets': options.ASSETS
        }))
        self.finish()


class MainHandler(BaseHandler):
    def get(self):
        template = env.get_template('home/index.html')
        self.render_template(template)


class AllUsers(BaseHandler):
    async def get(self):
        users = await User.query.gino.all()
        for user in users:
            url = self.application.reverse_url('user', user.id)
            email = tornado.escape.xhtml_escape(user.email)
            self.write(f'<a href="{url}">{email}</a><br/>')


class GetUser(GinoRequestHandler):
     async def get(self, uid):
        user: User = await User.get_or_404(int(uid))
        self.write(f'Hi, {user.email}!')


class GetStockHandler(BaseHandler):
    def get(self, symbol):
        d = fa.Stock.fetch(fa_client, symbol)
        self.render_json(d)


class OptionPositionsHandler(BaseHandler):
    def get(self):
        d = fa.OptionPosition.all(fa_client)
        self.render_json(d)


class OptionOrdersHandler(BaseHandler):
    def get(self):
        d = fa.OptionOrder.all(fa_client)
        self.render_json(d)


def make_app():
    return Application([
            # tornado.web.URLSpec(r"/", MainHandler),
            # tornado.web.URLSpec(r"/api/v1/stock/([^/]+)", GetStockHandler),
            # tornado.web.URLSpec(r"/api/v1/option_positions/fetch", OptionPositionsHandler),
            # tornado.web.URLSpec(r"/api/v1/option_orders/fetch", OptionOrdersHandler)
            tornado.web.URLSpec(r'/', AllUsers, name='index'),
            tornado.web.URLSpec(r'/user/(?P<uid>[0-9]+)', GetUser, name='user')
        ],
        static_path='static',
        debug=True)


if __name__ == "__main__":
    # try:
    #     fn = 'webpack-assets.json'
    #     with open(fn) as f:
    #         watch(fn)
    #         assets = json.load(f)
    # except IOError:
    #     pass
    # except KeyError:
    #     pass
    # define('ASSETS', assets)

    # python server.py --db_user=weston --db_database=chesterton_prod

    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
    loop = tornado.ioloop.IOLoop.current().asyncio_loop

    app = make_app()

    loop.run_until_complete(app.late_init(db))

    app.listen(8888)

    loop.run_forever()
