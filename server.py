import tornado.ioloop
import tornado.web
from tornado.options import options, define
from tornado.autoreload import watch

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


class BaseHandler(tornado.web.RequestHandler):
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


class GetStockHandler(BaseHandler):
    async def get(self, symbol):
        d = fa.Stock.fetch(fa_client, symbol)
        self.render_json(d)


class GetOptionPositionsHandler(BaseHandler):
    async def get(self):
        d = fa.OptionPosition.all(fa_client)
        self.render_json(d)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/stock/([^/]+)", GetStockHandler),
        (r"/option_positions", GetOptionPositionsHandler),
    ], static_path='static', debug=True)


if __name__ == "__main__":
    try:
        fn = 'webpack-assets.json'
        with open(fn) as f:
            watch(fn)
            assets = json.load(f)
    except IOError:
        pass
    except KeyError:
        pass

    define('ASSETS', assets)
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
