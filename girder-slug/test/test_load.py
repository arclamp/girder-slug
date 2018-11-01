import pytest

from girder.plugin import loadedPlugins


@pytest.mark.plugin('girder_slug')
def test_import(server):
    assert 'girder_slug' in loadedPlugins()
