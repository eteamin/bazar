<script src="/js/jquery.cookie.min.js"></script>
<script src="/js/jquery.navgoco.min.js"></script>
<link rel="stylesheet" type="text/css" media="screen" href="/css/jquery.navgoco.css"/>

<ul class="nav">
    %if categories:
        <h3>دسته بندی محصولات</h3>
        %for c in categories:
            <li><a href="#">${c.title}</a>
                <ul>
                    %for s in c.sub_category:
                        <li><a href="${tg.url('/products/subcategory')}/${s.id}">${s.title}</a></li>
                    %endfor
                </ul>
            </li>
        %endfor
</ul>
    %else:
        <p>هیچ دسته بندی وجود ندارد</p>
    %endif


<%def name="script()">
<script type="text/javascript">
    $(document).ready(function() {
        $('.nav').navgoco({
              caretHtml: '<i></i>',
              accordion: false,
              openClass: 'open',
              save: true,
              cookie: {
                  name: 'navgoco',
                  expires: false,
                  path: '/'
              },
              slide: {
                  duration: 300,
                  easing: 'swing'
              }
          });
    });
</script>
</%def>