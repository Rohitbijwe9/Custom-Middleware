
from typing import Any


class DemoMiddleware:


    def __init__(self,get_response):  #get response is handle response 
        self.get_response =get_response

    
    def __call__(self,request, *args: Any, **kwds: Any):  #call automatically call
        print('middleware call')
        res=self.get_response(request)

        return res


