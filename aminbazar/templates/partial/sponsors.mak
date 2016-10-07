%if sponsors:
  <section class="box sponsors-box">
    <div>
      <header>
        <h3 class="pull-right">حامیان هیأت</h3>
      </header>
      <article>
        <ul class="sponsor sponsor-hidden">
          %for b in sponsors:
            <li class="sponsor-item">
              <a target="_blank" href="${b.url}">
                <img data-src="${b.image.url}" alt="${b.url}" src="${b.image.url}"/>
              </a>
            </li>
          %endfor
        </ul>
      </article>
    </div>
  </section>
%endif

<%def name="script()">
<script>
  //http://sachinchoolur.github.io/lightslider/settings.html
  $('.sponsor').lightSlider({
    auto: true,
    pause: 2000,
    mode: 'fade',
    loop: true,
    item: 1,
    speed: 500,
    pager: false,
    controls: false,
    adaptiveHeight: false,
    onSliderLoad: function () {
      $('.sponsor').removeClass('sponsor-hidden');
    }
  });
</script>
</%def>