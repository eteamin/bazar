<%namespace name="header" file="local:templates.partial.header"/>
<%namespace name="sponsors" file="local:templates.partial.sponsors"/>
<%namespace name="category" file="local:templates.partial.category"/>
<%namespace name="ads" file="local:templates.partial.ads"/>
<!DOCTYPE html>
  <%
    min = '' if h.is_debug() else '.min'
  %>
<html lang="${tmpl_context.lang}">
<head>
  <meta charset="${response.charset}"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <%include file="local:templates.partial.favicon" />
  ${self.page_title()}
  <!--[if lt IE 9]>
      <script src="/contrib/html5shiv.min.js"></script>
      <script src="/contrib/respond.min.js"></script>
  <![endif]-->
  <link rel="stylesheet" type="text/css" media="screen" href="/css/public${min}.css"/>
    <script src="/js/public${min}.js"></script>
  ${self.head()}


</head>
<body>
  ${header.body()}
<div class="container">
    <%include file="local:templates.partial.navigator" />
</div>
<div class="container">
  <div class="right-bar">
      ${category.body()}
  </div>
    ${next.body()}
    ${self.content_wrapper()}
  <div class="left-bar">
    ${ads.body()}
  </div>

</div>
  <%include file="local:templates.partial.footer" />
  ${header.script()}
  ${sponsors.script()}
  ${category.script()}
  ${self.page_scripts()}
</body>
</html>
<%def name="head()"></%def>
<%def name="page_title()" >
  <title>${page.header}</title>
  <meta name="description" content="${page.description}"/>
</%def>
<%def name="page_scripts()">
</%def>

<%def name="content_wrapper()">
  <%
    flash=tg.flash_obj.render('flash', use_js=False)
  %>
  % if flash:
      <div class="row">
        <div class="col-md-8 col-md-offset-2">
              ${flash | n}
        </div>
      </div>
  % endif
</%def>
