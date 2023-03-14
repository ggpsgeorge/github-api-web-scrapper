import requests

USER_TOKEN_PATH = 'github_token.txt'

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

    print(r.json())

    if r.status_code == 200:
        print("Successful Authorization!")
    else:
        print("Authorization was not possible!")
    
    
def get_token_and_user(path: str):
    """Function that reads the user and token in a file and return them"""
    
    with open(path) as file:
        items = file.readlines()
        user, token = items[0], items[1]
    
    return user, token

if __name__ == '__main__':
    search_url: str = 'https://api.github.com/search/repositories?q=cucumber+bdd&type=Repositories+language:javascript'
    print(get_api_limit())
    request_a_search_url_response(search_url)
        
    

   