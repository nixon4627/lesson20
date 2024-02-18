

import requests
import pprint

url = 'https://api.github.com/search/repositories?g=tetris+language:assembly&sort=stars&order=desc'
#token = ('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')

#result = requests.get(url, auth = ('nixon4627', token))

#headers = {
    #'Autorization':f'tokenP{token}'
#}

#result = requests.get(url, headers= headers)

session = requests.session()
session.auth = ('nixon4627', token)
result = session.get(url)

result = session.get(url)
pprint.pprint(result.json)

url = 'https://api.github.com/search/code?g=addClass+in'