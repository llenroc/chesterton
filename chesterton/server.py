import tornado.ioloop
import tornado.web
import fast_arrow as fa
import json

import configparser
config_file = "config.dev.ini"
config = configparser.ConfigParser()
config.read(config_file)
username = config['account']['username']
password = config['account']['password']
fa_client = fa.Client(username=username, password=password)
result = fa_client.authenticate()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class BaseHandler(tornado.web.RequestHandler):
    def return_json(self, data):
        self.write(json.dumps(data))
        self.finish()


class GetStockHandler(BaseHandler):
    async def get(self, symbol):
        d = fa.Stock.fetch(fa_client, symbol)
        self.return_json(d)


class GetOptionPositionsHandler(BaseHandler):
    async def get(self):
        d = fa.OptionPosition.all(fa_client)
        self.return_json(d)


def make_app():
    return tornado.web.Application([
        (r"/stock/([^/]+)", GetStockHandler),
        # (r"/stock_positions", GetStockPositionsHandler),
        # (r"/option_orders", GetOptionOrdersHandler),
        (r"/option_positions", GetOptionPositionsHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
