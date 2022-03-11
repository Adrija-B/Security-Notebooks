import requests

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r.json())


#docker-compose exec web python make-request.py
