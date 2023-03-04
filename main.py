import requests

def getLimit(auth: str) -> tuple[dict[str], dict[str]]:
    """Function get the limit of requests for the github api, rate and the search limit"""
    r = requests.get(' https://api.github.com/rate_limit')
    
    response = r.json()

    return (response['rate'], response['resources']['search'])

def getAuth():
    token: str = ''
    auth = requests.get(search_url, auth=('ggpsgeorge', token))
    return auth

if __name__ == '__main__':
    search_url: str = 'https://github.com/search?l=JavaScript&q=cucumber+bdd&type=Repositories'
    auth = getAuth(search_url)
    getLimit(auth)