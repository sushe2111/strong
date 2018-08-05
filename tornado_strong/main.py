import conf.initConf
import tornado.httpserver
import tornado.ioloop

from app.Application import Application
from conf.baseConf import ListenConf


if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(ListenConf["port"], ListenConf["host"])
    print("=======",ListenConf["port"],ListenConf["host"])
    tornado.ioloop.IOLoop.current().start()
