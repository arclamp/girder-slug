import router from 'girder/router';

router.route('slug/:id', 'slug', function (slug, params) {
  const hash = window.location.hash;
  router.navigate('/collections', {
    trigger: true,
    replace: true
  });
  router.navigate(hash, { replace: true });
});
