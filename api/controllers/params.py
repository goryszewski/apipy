from api.models.redis import mem

def get(key):
    return mem.get(key)

def set(key,value):
    return mem.set(key,value)