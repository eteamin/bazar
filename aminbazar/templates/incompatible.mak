<%!
  browsers = [
    ('Google Chrome', 0, "http://www.google.com/chrome/"),
    ('Mozilla Firefox', 1, "https://www.mozilla.org/en-US/firefox/new/"),
    ('Microsoft Internet Explorer', 2, "http://windows.microsoft.com/en-us/internet-explorer/download-ie"),
    ('Apple Safari', 3, "http://www.google.com/search?q=safari%20for%20windows"),
    ('Opera', 4, "http://www.opera.com/download")
  ]
%>
<%
  browser_name = 'Internet Explorer' if request.client_info.browser.family == 'IE' else request.client_info.browser.family
  browser_version = request.client_info.browser.version[0]
%>

<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="${response.charset}"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
  <title>${'' if not seo else seo.title}</title>
  <style>
    .supported-browsers {
      margin-left: auto;
      margin-right: auto;
      width: 400px;
      height: 80px;
      background-color: #656565;
    }
    .supported-browsers a {
      text-decoration: none;
      padding: 0;
      margin: 0;
      display: block;
      float: left;
      width: 80px;
      height: 80px;
    }
    .supported-browsers a:hover {
      text-decoration: none;
    }
    div.icon {
      display: inline-block;
      background-image: url(/img/browsers.png);
      width: 80px;
      height: 80px;
      background-position-y: 0px;
    }
    div.icon:hover {
      background-position-y: -80px;
    }
  </style>

</head>
<body>
<center>
  <%include file="local:templates.partial.header" />
  <div class="content-area">
    <img src="/img/warning-sign.png" alt="WARNING"/>

    <p class="text-center">
      <br/><br/>
      ${_('You are using an old version of the %s browser (v.%s)') % (browser_name, browser_version)}
      <br/>
      ${_('This browser and the older versions of it are not supported by %s') % seo.title}
      <br/>
      ${_('To be able to see this website please use one these browsers:')}
    </p>

    <div class="supported-browsers">
      %for browser in browsers:
        <a target="_blank" href="${browser[2]}">
          <div class="icon" style="background-position-x: -${browser[1]*80}px"></div>
        </a>
      %endfor
    </div>
  </div>
  <%include file="local:templates.partial.footer" />
</center>
</body>
</html>

