class PullsView(object):
    
    def __init__(self, viewmodel):
        self.viewmodel = viewmodel

    def repos(self):
        return self.viewmodel
