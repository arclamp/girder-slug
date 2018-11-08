import router from 'girder/router';
import events from 'girder/events';
import { exposePluginConfig } from 'girder/utilities/PluginUtils';
import { restRequest } from 'girder/rest';

import ConfigView from './views/ConfigView';

exposePluginConfig('girder_slug', 'plugins/slug/config');

router.route('slug/:id', 'slug', function (slug, params) {
  const hash = window.location.hash;

  restRequest({
    method: 'GET',
    url: 'slug/setting'
  }).done((resp) => {
    const slugs = resp['slug'] || [];
    const slugSpec = slugs.filter(d => d.slug === slug)[0];

    if (slugSpec) {
      router.navigate(`#${slugSpec.resourceType}/${slugSpec.girderID}`, {
        trigger: true,
        replace: true
      });
      router.navigate(hash, { replace: true });
    } else {
      events.trigger('g:alert', {
        icon: 'attention',
        text: `No such slug '${slug}'`,
        type: 'danger',
        timeout: 4000
      });
    }
  });
});

router.route('plugins/slug/config', 'slugConfig', function () {
  events.trigger('g:navigateTo', ConfigView);
});
