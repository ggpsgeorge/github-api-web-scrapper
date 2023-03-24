import requests
import json

GH_URL = "https://api.github.com"
REPOS_URL = GH_URL + "/repos"
LIMIT_URL = 'https://api.github.com/rate_limit'
USER_TOKEN_PATH = 'github_token.txt'
JSON_DATA = 'data//request_data_'

def get_api_limit() -> tuple[dict[str], dict[str]]:
    """Function get the limit of requests for the github api, rate and the search limit"""

    r = requests.get(LIMIT_URL, auth=(get_token_and_user(USER_TOKEN_PATH)))
    response = r.json()

    return (response['rate'], response['resources']['search'])


def get_search_url_response(search_url: str):
    """Function that dumps the response of a search into a file"""
    
    user, token = get_token_and_user(USER_TOKEN_PATH)

    response = requests.get(search_url, auth=(user, token))

    return response


def get_all_search_url_responses(search_url: str, num_of_pages: int):

    for i in range(1, num_of_pages+1):
        response = get_search_url_response(search_url + str(i))
        write_json_response_to_file(response, JSON_DATA + str(i) + ".json")


def write_json_response_to_file(response, path):
    with open(path, "x") as outfile:
        json.dump(response.json(), outfile)
    outfile.close()


def get_token_and_user(path: str):
    """Function that reads the user and token from a file"""
    
    with open(path) as file:
        items = file.readlines()
        user, token = items[0], items[1]
    
    return user, token


def load_json_data(path: str):
    with open(path) as json_file:
        data = json.load(json_file)
    json_file.close()
    
    return data


def save_repos_urls(num_of_pages):
    for i in range(1, num_of_pages+1):
        data_items = load_json_data(JSON_DATA + str(i) + ".json")['items']
        
        with open("data//repos_urls.txt", "a") as repos:
            for item in data_items:
                repos.write(item['html_url'] + "\n")
        repos.close()

def clone_repo(repo_url):
    """Clone the entire repository"""
    user, token = get_token_and_user(USER_TOKEN_PATH)
    response = requests.get(repo_url, auth=(user, token))
    
    print(response)


   