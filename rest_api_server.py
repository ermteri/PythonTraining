from bottle import *
from pprint import pprint
import time
import math
index_success_template='''\
<html>
<h1>Welcome to time-presenter and area calculator</h1>
<p>Current time is: {{time}}</p>
<p>Area of a circle with radius {{radius}} is {{area}}</p>
<i>See you around!!</i>
</html>
'''
index_fail_template='''\
<html>
<h1>Welcome to time-presenter and area calculator</h1>
<p>Current time is: {{time}}</p>
<p>Sorry, the area couldn't be calculated because radius {{radius}}</p>
<i>See you around!!</i>
</html>
'''
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
    if 'radius' in d.keys():
       if d.get('radius').replace('.','',1).isdigit():
           return dict(radius=str(r),something=dict(area="r*pi^2"),listan=[1,2,3],area=str(3.14*r**2.0))
    
@route('/index')
def index():
    d=dict(request.query)
    t=time.asctime(time.localtime())
    if 'radius' in d.keys():
       r=d.get('radius')
       if r.replace('.','',1).isdigit():
           a=math.pi*int(r)**2.0
           return template(index_success_template,time=t,radius=r, area=a)
       return template(index_fail_template,time=t,radius='was invalid ('+r+')')
    return template(index_fail_template,time=t,radius='didn\'t exist')

if __name__ == "__main__":
    run(host='localhost',port=8080)
