import router from 'girder/router';
import events from 'girder/events';
import { exposePluginConfig } from 'girder/utilities/PluginUtils';

import ConfigView from './views/ConfigView';

exposePluginConfig('slug', 'plugins/slug/config');

router.route('slug/:id', 'slug', function (slug, params) {
  const hash = window.location.hash;
  router.navigate('/collections', {
    trigger: true,
    replace: true
  });
  router.navigate(hash, { replace: true });
});

router.route('plugins/slug/config', 'slugConfig', function () {
  events.trigger('g:navigateTo', ConfigView);
});
