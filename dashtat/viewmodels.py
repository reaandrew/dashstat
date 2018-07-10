import functools
import datetime
from dateutil.parser import parse

class PullsViewModelFactory:

    def __init__(self, org):
        self.org = org

    def getClassNameForDays(self, days):
        if days == 0:
            return 'alert-success'
        if days == 1:
            return 'alert-warning'
        return 'alert-danger'

    def create(self, git_service):
        viewmodel = []

        for repo in git_service.get_repos(self.org):
            repo_name = repo['name']
            pulls = {}
            repo_model = {
                'name': repo_name,
                'pulls': []
            }
            for pull in git_service.get_pulls(self.org, repo_name):
                delta = datetime.datetime.utcnow() - parse(pull['created_at']).replace(tzinfo=None)
                if delta.days not in pulls:
                    pulls[delta.days] = 0

                pulls[delta.days] += 1
            repo_model['pulls'] = ({
                'days': x,
                'count': y,
                'className': self.getClassNameForDays(x)
            } for x,y in pulls.iteritems())


            if len(pulls) > 0:
                print(repo_model['name'], repo_model['pulls'])
                viewmodel.append(repo_model)

        return viewmodel
