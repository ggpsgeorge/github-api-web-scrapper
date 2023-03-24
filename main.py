import utils

if __name__ == '__main__':
    # needs the page of the search
    search_url: str = 'https://api.github.com/search/repositories?q=cucumber+bdd&type=Repositories&per_page=100&page='
    # # github only show the first 1000 searches
    num_of_pages = 10
    # utils.get_all_search_url_responses(search_url, num_of_pages)
    # utils.save_repos_urls(num_of_pages)
    # print(utils.get_api_limit())
    repo_url = utils.REPOS_URL + "/ggpsgeorge/Java-PoW"
    utils.clone_repo(repo_url)
        