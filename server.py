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

import datetime

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

class AbstractModel(object):
    @classmethod
    def gen_ads(cls, array):
        result = []
        for e in array:
            result.append(e.to_dictionary())
        return result

    @classmethod
    def find_existing(cls, id):
        return cls.query.where(cls.id == id).gino.all()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode(), nullable=False)


class RhOptionPosition(db.Model, AbstractModel):
    __tablename__ = 'rh_option_positions'

    cid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    id = db.Column(db.String())
    chain_id = db.Column(db.String())
    option = db.Column(db.String())
    url = db.Column(db.String())
    average_price = db.Column(db.Numeric(8,2))
    trade_value_multiplier = db.Column(db.Numeric(8,2))
    chain_symbol = db.Column(db.String())
    strike_price = db.Column(db.Numeric(10,4))
    expiration_date = db.Column(db.Date())
    type = db.Column(db.String())
    option_type = db.Column(db.String())
    quantity = db.Column(db.Numeric(8,2))
    delta = db.Column(db.Numeric(8,4))
    theta = db.Column(db.Numeric(8,4))
    gamma = db.Column(db.Numeric(8,4))
    vega = db.Column(db.Numeric(8,4))
    data = db.Column(db.JSON())

    def to_dictionary(self):
        return dict(
            cid=self.cid,
            id=self.id,
            chain_id=self.chain_id,
            option=self.option,
            url=self.url,
            average_price=str(self.average_price),
            trade_value_multiplier=str(self.trade_value_multiplier),
            chain_symbol=self.chain_symbol,
            strike_price=str(self.strike_price),
            expiration_date=datetime.datetime.strftime(self.expiration_date, "%Y-%m-%d"),
            type=self.type,
            option_type=self.option_type,
            quantity=str(self.quantity),
            delta=str(self.delta),
            theta=str(self.theta),
            gamma=str(self.gamma),
            vega=str(self.vega)
        )

    @classmethod
    def all_open(cls):
        return cls.query.where(cls.quantity != 0.0).gino.all()

    @classmethod
    async def parse_and_save(cls, op):
        existing = await cls.find_existing(op["id"])
        if len(existing) > 0:
            return None
        x = RhOptionPosition()
        x.id = op["id"]
        x.chain_id = op["chain_id"]
        x.option = op["option"]
        x.url = op["url"]
        x.average_price = op["average_price"]
        x.trade_value_multiplier = op["trade_value_multiplier"]
        x.chain_symbol = op["chain_symbol"]
        x.strike_price = op["strike_price"]
        x.expiration_date = datetime.datetime.strptime(op["expiration_date"], "%Y-%m-%d")
        x.type = op["type"]
        x.option_type = op["option_type"]
        x.quantity = op["quantity"]
        x.delta = op["delta"]
        x.theta = op["theta"]
        x.gamma = op["gamma"]
        x.vega  = op["vega"]
        await x.create()


class RhOptionOrder(db.Model, AbstractModel):
    __tablename__ = 'rh_option_orders'

    cid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    id = db.Column(db.String())
    chain_id = db.Column(db.String())
    chain_symbol = db.Column(db.String())
    strike_price = db.Column(db.Numeric(10,4))
    expiration_date = db.Column(db.Date())
    side = db.Column(db.String())
    option = db.Column(db.String())
    state = db.Column(db.String())
    direction = db.Column(db.String())
    position_effect = db.Column(db.Numeric(8,2))
    ratio_quantity = db.Column(db.Integer())
    price = db.Column(db.Numeric(8,4))
    leg = db.Column(db.String())
    opening_strategy = db.Column(db.String())
    closing_strategy = db.Column(db.String())
    data = db.Column(db.JSON())

    @classmethod
    async def parse_and_save(cls, xx):
        existing = await cls.find_existing(xx["id"])
        if len(existing) > 0:
            return None
        x = cls()
        x.id = xx["id"]
        x.chain_id = xx["chain_id"]
        x.chain_symbol == xx["chain_symbol"]
        x.state = xx["state"]
        x.direction = xx["direction"]
        x.data = xx
        x.contract_type = xx["contract_type"]
        x.strike_price = xx["strike_price"]
        x.expiration_date = datetime.datetime.strptime(xx["expiration_date"], "%Y-%m-%d")
        x.side = xx["side"]
        x.option = xx["option"]
        x.position_effect = xx["position_effect"]
        x.ratio_quantity = xx["ratio_quantity"]
        x.price = xx["price"]
        x.leg = xx["leg"]
        x.opening_strategy = xx["opening_strategy"]
        x.closing_strategy = xx["closing_strategy"]
        await x.create()

    @classmethod
    def all_filled(cls):
        return cls.query.where(cls.state == "filled").gino.all()

    @classmethod
    async def parsed_unrolled_data(cls, xx):
        # find first
        return 0

    def to_dictionary(self):
        return dict(
            cid = self.cid,
            id = self.id,
            chain_id = self.chain_id,
            chain_symbol = self.chain_symbol
        )


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

class OptionPositionsHandler(BaseHandler):
    async def get(self):
        ops = await RhOptionPosition.all_open()
        ads = RhOptionPosition.gen_ads(ops)
        self.render_json(ads)

class OptionPositionsRefreshHandler(BaseHandler):
    async def get(self):
        ops = await RhOptionPosition.all_open()

        ops_for_market_fetch = []
        for op in ops:
            x = {"id": op.id, "option": op.option}
            ops_for_market_fetch.append(x)

        mds = fa.OptionPosition.mergein_marketdata_list(fa_client, ops_for_market_fetch)

        for md in mds:
            selected_op = [op for op in ops if op.id == md["id"]][0]
            updated_fields = {
                "delta": md["delta"],
                "theta": md["theta"],
                "vega":  md["vega"],
                "gamma": md["gamma"]
            }
            await selected_op.update(**updated_fields).apply()

        ops = await RhOptionPosition.all_open()
        ads = RhOptionPosition.gen_ads(ops)
        self.render_json(ads)

class OptionPositionsFetchHandler(BaseHandler):
    async def get(self):
        ops = fa.OptionPosition.all(fa_client)
        ops = fa.OptionPosition.mergein_marketdata_list(fa_client, ops)
        ops = fa.OptionPosition.humanize_numbers(ops)
        ops = fa.OptionPosition.mergein_instrumentdata_list(fa_client,ops)

        [await RhOptionPosition.parse_and_save(op) for op in ops]

        self.render_json({"success": True})


class OptionOrdersHandler(BaseHandler):
    async def get(self):
        x = await RhOptionOrder.all_filled()
        ads = RhOptionOrder.gen_ads(x)
        self.render_json(ads)

class OptionOrdersFetchHander(BaseHandler):
    async def get(self):
        oos = fa.OptionOrder.all(fa_client)
        oos = fa.OptionOrder.unroll_option_legs(fa_client, oos[0:500])

        [await RhOptionOrder.parse_and_save(oo) for oo in oos]

        self.render_json({"success": True})


def make_app():
    return Application([
            tornado.web.URLSpec(r"/api/v1/option_orders/fetch", OptionOrdersFetchHander),
            tornado.web.URLSpec(r"/api/v1/option_orders", OptionOrdersHandler),

            tornado.web.URLSpec(r"/api/v1/option_positions/fetch", OptionPositionsFetchHandler),
            tornado.web.URLSpec(r"/api/v1/option_positions/refresh", OptionPositionsRefreshHandler),
            tornado.web.URLSpec(r"/api/v1/option_positions", OptionPositionsHandler),

            tornado.web.URLSpec(r'/', AllUsers, name='index'),
            tornado.web.URLSpec(r'/user/(?P<uid>[0-9]+)', GetUser, name='user')
        ],
        static_path='static',
        debug=True)


if __name__ == "__main__":
    # pipenv run python server.py --db_user=weston --db_database=chesterton

    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
    loop = tornado.ioloop.IOLoop.current().asyncio_loop

    app = make_app()

    loop.run_until_complete(app.late_init(db))

    app.listen(8888)

    loop.run_forever()
