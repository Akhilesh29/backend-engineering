import redis
cache = redis.Redis(host='localhost', port=6379)

# Setting cache
cache.set('user:1', 'akhilesh')

# Get cache
user = cache.get('user:1')
print(user) 
