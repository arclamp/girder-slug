import jsonschema

from girder import plugin
from girder import utility
from girder import logger
from girder.exceptions import ValidationException


_slugSchema = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'resourceType': {
                'enum': ['collection', 'folder', 'item'],
            },
            'girderID': {
                'type': 'string',
                'pattern': '^[0-9a-f]{24}$'
            },
            'slug': {
                'type': 'string',
                'pattern': '^[a-zA-Z0-9-]{1,128}$'
            }
        },
        'required': ['resourceType', 'girderID', 'slug']
    }
}


@utility.setting_utilities.validator('slug')
def validateSettings(doc):
    try:
        jsonschema.validate(doc['value'], _slugSchema)
    except jsonschema.ValidationError as e:
        raise ValidationException('Invalid slug: ' + e.message)


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'slug'
    CLIENT_SOURCE_PATH = 'web_client'

    def load(self, info):
        # add plugin loading logic here
        pass
