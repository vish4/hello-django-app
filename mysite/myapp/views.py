from django.http import HttpResponse
import redis
import os
host=os.getenv("DB_PORT_6379_TCP_ADDR")
redis_ins = redis.StrictRedis(host=host, port=6379)

def hello(request):
	val=redis_ins.get('background')
	if val == "red":
		return HttpResponse("<body bgcolor='#FF0000'> <p>Hello, world</p> </body>") 
	else:
		return HttpResponse("<body bgcolor='#00ff40'> <p>Hello, world</p> </body>") 
