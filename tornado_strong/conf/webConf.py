from app.controller.IndexHandler import IndexHandler
from app.controller.LoginHandler import LoginHandler

class Handlers:
    #需要安全检查的handle. dict. 安全类的必须实现post方法。
    secureHandlers = {
		#"userInfo": UserHandler
    }

    #不需要安全检查的handle. list
    commonHandlers = [ 
        #(r/"/sec/(\S+)") 
        #("/sec/(\S+)", SecureHandler), 
		(r"/", IndexHandler),
		(r"/index", IndexHandler),
		(r"/login", LoginHandler),
    ] 
 
