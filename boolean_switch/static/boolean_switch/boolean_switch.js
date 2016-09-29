var $ = django.jQuery || grp.jQuery;

(function($) {
  $(document).ready(function() {
    $('body').on('click', '.boolean_switch', function(e) {
      e.preventDefault();
      var img = $(this).find('img');
      $.get($(this).attr('href'), function(json) {
        if (json.value) {
          var new_src = img.attr('src').replace(/(icon-)([a-z]+)(.svg)/g, '$1yes$3');
        } else {
          var new_src = img.attr('src').replace(/(icon-)([a-z]+)(.svg)/g, '$1no$3');
        }
        img.attr('src', new_src);
      }, 'json');
    });
  });
})($);
