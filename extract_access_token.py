import json

access_token_json = json.load(open('access_token.txt'))
print(access_token_json['access_token'])
