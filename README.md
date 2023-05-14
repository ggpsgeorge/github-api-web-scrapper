# Github Web Scrapper

A Python script capable of downloading file extensions. However, the script needs to have a base search query. 

The query must have this style 'https://api.github.com/search/repositories?q=cucumber+bdd&type=Repositories&per_page=100&page='. This means, give repositories with cucumber and bdd search elements with 100 repos per page. The last page word is used to identify, well, the current page of the search, as 1, 2, and so on. The script will increments the pages automatically.

Nothing Fancy.

Generate a Token from github, for you to be able to use the API without too many limits. The script reads the username and token, so make sure to create a txt called github_token.txt, and write the username, then a newline, and the token. Then, commment or uncomment the functions that you want to use in the main file. Also, the variables, like the search_url. 

The functions used in the main file are in the utils file.

For questions about the API and repositories search: https://docs.github.com/en/rest/search?apiVersion=2022-11-28#search-repositories
