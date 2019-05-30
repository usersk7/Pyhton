from requests_oauthlib import OAuth1Session
test = OAuth1Session('consumer_key',
                    client_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
url = 'https://one-legged-ouath.example.com/username/test'
r = test.get(url)
print (r.content)
