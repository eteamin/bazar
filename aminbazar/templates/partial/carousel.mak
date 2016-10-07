<div class="main-slider-wrapper">
  <ul id="mainSlider" class="slider-hidden">
    %for b in banners:
      <li class="slider-item"><img src="${b.image.url}" title="${b.title}"/></li>
    %endfor
  </ul>
</div>

<%def name="script()">
  <script type="text/javascript">
    //http://sachinchoolur.github.io/lightslider/settings.html
    $('#mainSlider').lightSlider({
      auto: true,
      pause: 5000,
      loop: true,
      item: 1,
      cssEasing: 'cubic-bezier(0.680, -0.550, 0.265, 1.550)',
      speed: 500,
      galleryMargin: -35,
      pager: true,
      onSliderLoad: function () {
        $('#mainSlider').removeClass('slider-hidden');
      }
    });
  </script>
</%def>