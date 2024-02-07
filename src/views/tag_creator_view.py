from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # body = http_request.body
        # product_code = body["product_code"]
        # business rule logic
        print("I'm in my view")
        print(http_request)
        # return http
        return HttpResponse(status_code=200, body={"hello": "world"})
