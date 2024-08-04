import redis

try:
    r = redis.StrictRedis(
        host='localhost',
        port=6379
    )
    print(r.ping())
    print('Connected!')
    r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    print(r.get("Bahamas"))
except Exception as ex:
    print ('Error:', ex)
    exit('Failed to connect, terminating.')
