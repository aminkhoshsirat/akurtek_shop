from redis import Redis

re = Redis(host='localhost', port=6379, db=0)

print(re.ttl('vjkdvjdf'))