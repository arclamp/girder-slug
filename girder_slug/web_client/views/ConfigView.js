import $ from 'jquery';

import GroupCollection from 'girder/collections/GroupCollection';
import PluginConfigBreadcrumbWidget from 'girder/views/widgets/PluginConfigBreadcrumbWidget';
import router from 'girder/router';
import View from 'girder/views/View';
import events from 'girder/events';
import { restRequest } from 'girder/rest';

import ConfigViewTemplate from '../templates/configView.pug';
// import '../stylesheets/configView.styl';

var ConfigView = View.extend({
    events: {
        'click .g-slug-remove': function (event) {
            this.$('#g-slug-error-message').text('');
            var index = parseInt($(event.currentTarget).attr('data-index'), 10);
            this.slugs.splice(index, 1);
            this.render();
        },
        'click #g-slug-add': function (event) {
            this.$('#g-slug-error-message').text('');
            var resourceType = $('#g-slug-resource-type').val();
            var girderID = $('#g-slug-girder-id').val();
            var slug = $('#g-slug-slug').val();
            if (resourceType === '' || girderID === '' || slug === '') {
                this.$('#g-slug-error-message').text(
                    'All fields are required.');
                return;
            }
            var slugSpec = {
                resourceType: resourceType,
                girderID: girderID,
                slug: slug
            };
            this.slugs.push(slugSpec);
            this.render();
        },
        'click #g-slug-save': function (event) {
            this.$('#g-slug-error-message').text('');
            this._saveSettings([{
                key: 'slug',
                value: this.slugs
            }]);
        },
        'click #g-slug-cancel': function (event) {
            router.navigate('plugins', {trigger: true});
        }
    },

    initialize: function () {
        this.slugs = [];

        restRequest({
            method: 'GET',
            url: 'slug/setting'
        }).done((resp) => {
            this.slugs = resp['slug'] || [];
            this.render();
        });
    },

    render: function () {
        this.$el.html(ConfigViewTemplate({
            slugs: this.slugs,
        }));

        new PluginConfigBreadcrumbWidget({
            pluginName: 'Slug',
            el: this.$('.g-config-breadcrumb-container'),
            parentView: this
        }).render();

        return this;
    },

    _saveSettings: function (settings) {
        restRequest({
            method: 'PUT',
            url: 'system/setting',
            data: {
                list: JSON.stringify(settings)
            },
            error: null
        }).done(() => {
            events.trigger('g:alert', {
                icon: 'ok',
                text: 'Settings saved.',
                type: 'success',
                timeout: 4000
            });
        }).fail((resp) => {
            this.$('#g-slug-error-message').text(
                resp.responseJSON.message
            );
        });
    }
});

export default ConfigView;
