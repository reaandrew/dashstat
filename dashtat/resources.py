import falcon
import pystache
import json
from dashtat.views.pulls_view import PullsView
from dashtat.viewmodels import PullsViewModelFactory

class PullRequestsResource(object):
    def __init__(self, org, service):
        self.org = org
        self.service = service

    def on_get(self, req, resp):
        """Handles GET requests"""
        viewmodelfactory = PullsViewModelFactory(self.org)
        viewmodel = viewmodelfactory.create(self.service)
        resp.content_type = 'text/html'
        resp.status = falcon.HTTP_200  # This is the default status

        renderer = pystache.Renderer(search_dirs='./dashtat/views')
        view = PullsView(viewmodel)

        resp.body = renderer.render(view)
