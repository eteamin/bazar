<%inherit file="local:templates.scaffold" />
<%namespace name="carousel" file="local:templates.partial.carousel"/>
<%namespace name="product" file="local:templates.partial.product"/>

## <%namespace name="ribbon" file="local:templates.news.partial.ribbon"/>
## ${ribbon.body()}
<div class="index-content-area">
  ${carousel.body()}
  ${product.body()}
  <%include file="local:templates.partial.related_image_link" />
</div>
<%def name="page_scripts()">
##   ${ribbon.script()}
  ${carousel.script()}
</%def>
