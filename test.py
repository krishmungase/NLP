import pymysql
import redis
import json

MYSQL_CONFIG = {
    'host': 'database-1.c7w4wqmsa7z2.ap-south-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'Krishna1',
    'database': 'college',
    'ssl': {
        'ca': './global-bundle.pem',
        'check_hostname': True
    }
}

REDIS_CONFIG = {
    'host': 'master.server-cache.jizf7z.aps1.cache.amazonaws.com',
    'port': 6379,
    'decode_responses': True,
    'ssl': True
}

def get_data_with_caching(query, cache_key):
    r = redis.Redis(**REDIS_CONFIG)

    cached_data = r.get(cache_key)
    if cached_data:
        print("Cache Hit! Returning data from Redis.")
        return json.loads(cached_data)

    print("Cache Miss. Fetching from RDS...")
    connection = pymysql.connect(**MYSQL_CONFIG)

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            r.setex(cache_key, 3600, json.dumps(result))
            return result
    finally:
        connection.close()

sql_query = "SELECT * FROM student WHERE dept = 'computer'"
data = get_data_with_caching(sql_query, "category:computer")

print(data)
