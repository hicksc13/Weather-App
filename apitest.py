import http.client, urllib.parse

conn = http.client.HTTPConnection('api.mediastack.com')

params = urllib.parse.urlencode({
    'access_key': 'fe83b1cd4aacdb0399029e84e26993ee',
    'categories': '-general,-sports',
    'sort': 'published_desc',
    'limit': 10,
    })

conn.request('GET', '/v1/news?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))