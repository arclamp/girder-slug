import json

from girder.api import access
from girder.api.describe import Description, autoDescribeRoute, describeRoute
from girder.api.rest import Resource


class Slug(Resource):
    def __init__(self, getSystemSetting):
        super(Slug, self).__init__()
        self.resourceName = 'slug'

        self.getSystemSetting = getSystemSetting;

        self.route('GET', ('setting',), self.getSlugSetting)

    @access.public
    @autoDescribeRoute(
        Description('Retrieve slug plugin system setting.')
    )
    def getSlugSetting(self):
        return self.getSystemSetting(key=None, list=json.dumps(['slug']), default=None, params={})
