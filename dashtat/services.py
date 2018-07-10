import requests
import requests_cache

class GithubService:

    def __init__(self, github_token):
        self.github_token = github_token

    def __repo_url(self, org):
        return 'https://api.github.com/orgs/{0}/repos'.format(org)

    def __pulls_url(self, org, repo):
        return 'https://api.github.com/repos/{0}/{1}/pulls'.format(org, repo)

    def __github_api_get(self, url):
        requests_cache.install_cache(expire_after=5*60)
        headers = {'Authorization': 'token ' + self.github_token}
        return requests.get(url, headers=headers)

    def get_repos(self, org):
        url = self.__repo_url(org) 
        data = self.__github_api_get(url).json()
        return data

    def get_pulls(self, org, repo):
        url = self.__pulls_url(org, repo)
        data = self.__github_api_get(url).json()
        return data
