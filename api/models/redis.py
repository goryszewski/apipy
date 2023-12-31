import redis,os
class Mem:
    def __init__(self):

        self.redis = redis.Redis(host=os.environ['HOST_REDIS'], port=6379, decode_responses=True)

    def get(self,key):
        value = self.redis.get(key)
        return 'Get Redis value {}:{}'.format(key,value)

    def set(self,key,value):
        self.redis.set(key,value)
        return 'Set Redis value {}:{}'.format(key,value)

mem = Mem()
