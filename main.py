import requests
import json

USER_TOKEN_PATH = 'github_token.txt'
JSON_DATA = 'request_data.json'

def get_api_limit() -> tuple[dict[str], dict[str]]:
    """Function get the limit of requests for the github api, rate and the search limit"""
    
    limit_url = 'https://api.github.com/rate_limit'

    r = requests.get(limit_url, auth=(get_token_and_user(USER_TOKEN_PATH)))
    response = r.json()

    return (response['rate'], response['resources']['search'])


def request_a_search_url_response(search_url):
    """Function that checks if the authorization token is accepted first"""
    
    user, token = get_token_and_user(USER_TOKEN_PATH)

    r = requests.get(search_url, auth=(user, token))

    if r.status_code == 200:
        print("Successful Authorization!")
        
        with open(JSON_DATA, "w") as outfile:
            json.dump(r.json(), outfile)
    else:
        print("Authorization was not possible!")
    
    
def get_token_and_user(path: str):
    """Function that reads the user and token in a file and return them"""
    
    with open(path) as file:
        items = file.readlines()
        user, token = items[0], items[1]
    
    return user, token

def load_json_data(path: str):
    with open(path) as json_file:
        data = json.load(json_file)
    
    return data

if __name__ == '__main__':
    search_url: str = 'https://api.github.com/search/repositories?q=cucumber+bdd&type=Repositories&per_page=100&page=1'
    print(get_api_limit())
    request_a_search_url_response(search_url)
    data_items = load_json_data(JSON_DATA)['items']
    
    print(data_items[3]['html_url'])

    for item in data_items:
        print(item['html_url'])
        
   