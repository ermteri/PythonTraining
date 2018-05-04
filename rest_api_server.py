from bottle import *
from pprint import pprint
import time
@route('/')
def welcome():
    print(request.headers.get('Accept'))
    response.content_type='text/plain'
    return 'Hello'

@route('/time')
def tid():
    response.set_header('Cache-Control','max-age=1')
    return '<head><meta http-equiv="refresh" content="10" ></head><h1>'+time.asctime(time.localtime())+'</h1>'

@route('/upper/<word>')
def upper_case_service(word):
    return '<h2>'+word.upper()+'</h2>'

@route('/circle')
def circle_area():
    d=dict(request.query)
    r=int(dict(request.query).get('radius'))
    return dict(radius=str(r),something=dict(area="r*pi^2"),listan=[1,2,3],area=str(3.14*r**2.0))
    
if __name__ == "__main__":
    run(host='localhost',port=8080)
