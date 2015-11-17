from django.http import HttpResponse
#import redis
#redis_POOL=redis.ConnectionPool(host='104.131.206.44', port=6379,db=0)
#redis_ins = redis.StrictRedis(host='localhost', port=6379,db=0)
#redis_ins.set('background', 1)

# def getVariable(variable_name):
#     my_server = redis.Redis(connection_pool=redis_POOL)
#     response = my_server.get(variable_name)
#     return response

# value=getVariable('background')
# print (value)
#def hello(request):
#	val=redis_ins.get('background')
#	if val == "red":
#		return HttpResponse("<body bgcolor='#FF0000'> <p>Hello, world</p> </body>") 
#	else:
#		return HttpResponse("<body bgcolor='#00ff40'> <p>Hello, world</p> </body>") 
def hello(request):
		return HttpResponse("<body bgcolor='#FF0000'> <p>Hello, world</p> </body>")
