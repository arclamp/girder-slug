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
    # Validate to the schema.
    try:
        jsonschema.validate(doc['value'], _slugSchema)
    except jsonschema.ValidationError as e:
        raise ValidationException('Invalid slug: ' + e.message)

    # Look for duplicate entries (either in resources or slugs).
    resources = set()
    slugs = set()

    dups = {'resources': set(), 'slugs': set()}
    for slug in doc['value']:
        if slug['girderID'] in resources:
            dups['resources'].add(slug['girderID'])

        if slug['slug'] in slugs:
            dups['slugs'].add(slug['slug'])

        resources.add(slug['girderID'])
        slugs.add(slug['slug'])

    if dups['resources']:
        raise ValidationException('Duplicate resources: ' + str(list(dups['resources'])))

    if dups['slugs']:
        raise ValidationException('Duplicate slugs: ' + str(list(dups['slugs'])))


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'slug'
    CLIENT_SOURCE_PATH = 'web_client'

    def load(self, info):
        # add plugin loading logic here
        pass
