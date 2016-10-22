<!DOCTYPE HTML>
  <%
    min = '' if h.is_debug() else '.min'
    logged_in = 'user_name' in session
  %>
<head>
${self.page_title()}
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

<link rel="stylesheet" type="text/css" media="screen" href="/css/public${min}.css"/>
<script src="/js/public${min}.js"></script>
</head>
<body>
    <div class="persian-num">
        <div class="header">
                <div class="wrap">
                    <div class="header_top">
                        <div class="logo">
                            <h1><a href="${tg.url('/')}" style="color: #b94a48;">AminBazaar</a></h1>
                        </div>
                     <div class="clear"></div>
                </div>
                <div class="container">
                  <nav class="navbar navbar-inverse">
                    <div class="navbar-header">
                        <button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".js-navbar-collapse">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="${tg.url('/')}">امین بازار</a>
                    </div>

                    <div class="collapse navbar-collapse js-navbar-collapse">
                        <ul class="nav navbar-nav">
                            <li><a href="${tg.url('/contact')}">ارتباط با ما</a></li>
                        </ul>
                        <ul class="nav navbar-nav navbar-right">
                            % if logged_in:
                                <li><a href="${tg.url('/products/new')}">افزودن محصول</a></li>
                            %endif
                            <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">حساب کاربری <span class="caret"></span></a>
                              <ul class="dropdown-menu" role="menu">
                                 % if not logged_in:
                                 <li><a href="${tg.url('/accounts/sign_in')}">ورود</a></li>
                                <li><a href="${tg.url('/accounts/sign_up')}">ثبت نام</a></li>
                                 %else:
                                     <li><a href="${tg.url('/products/my_products/')}${session['account_id']}">محصولات من</a></li>
                                     <li><a href="${tg.url('/accounts/log_out')}">خروج</a></li>
                                 %endif
                              </ul>
                            </li>
                            % if logged_in:
                                <li><a>خوش آمدید ${session['user_name']}</a></li>
                        % endif
                      </ul>
                    </div><!-- /.nav-collapse -->
                  </nav>
                </div>


             <div class="clear"></div>
            </div>

       <!------------End Header ------------>
      <div class="main">
          <div class="content">

                       </div>
                   </div>
                   </div>
              <div class="content_bottom">
                <div class="wrap">
                    <div class="content-bottom-left">
                        <div class="categories">
                               <ul>
                                   <h3>دسته بندی ها</h3>
                                 </ul>
                            <ul class="cat-dropdown">
                                %for c in categories:
                                <li><a>${c.title}</a>
                                    <ul>
                                        %for s in c.sub_category:
                                            <li><a href="${tg.url('/sub_category/')}${s.id}">${s.title}</a></li>
                                        %endfor
                                    </ul>
                                </li>
                                %endfor
                            </ul>
                            </div>
                            <div class="buters-guide">
                            <h3>راهنمای سایت</h3>
                            <p><span>راهنمای امین بازار</span></p>
                            <p>توضیحات بیشتر </p>
                          </div>
    ## 					  <div class="add-banner">
    ## 					  	<img src="img/camera.png" alt="" />
    ## 					  	<div class="banner-desc">
    ## 					  		<h4>Electronics</h4>
    ## 					  	    <a href="#">More Info</a>
    ## 					  	</div>
    ## 					  	<div class="clear"></div>
    ## 					  </div>
                    </div>
                    <div class="content-bottom-right">
                      ${self.content_wrapper()}
                      ${next.body()}
                    </div>

                  <div class="clear"></div>
               </div>
             </div>
       <div class="footer">
          <div class="wrap">
               <div class="footer-nav">
                <ul>
                    <li><a href="#">قوانین سایت</a> : </li>
                    <li><a href="#">ارتباط با ما</a> : </li>
                    <li><a href="#">نقشه سایت</a></li>
                </ul>
               </div>
            </div>
        </div>
        <script type="text/javascript">
            $(document).ready(function() {
                $().UItoTop({ easingType: 'easeOutQuart' });
            });
        </script>
        <a href="#" id="toTop"> </a>
    </div>
</body>
## ${self.page_scripts()}
<%def name="head()"></%def>
<%def name="page_title()" >
  <title>${page.header}</title>
  <meta name="description" content="${page.description}"/>
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
<script>
    $(document).ready(function(){
        $(".dropdown").hover(
            function() {
                $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideDown("400");
                $(this).toggleClass('open');
            },
            function() {
                $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideUp("400");
                $(this).toggleClass('open');
            }
        );
##     simple hack to add comma to numbers
    var prices = $('.rupees');
    for(var i = 0; i < prices.length; i++)
    {
        var price = prices.eq(i).text();
        var dom_price = prices[i];
        var converted = Number(parseInt(price)).toLocaleString('en');
        var text = $(dom_price).text();
        $(dom_price).text(text.replace(text, converted))
    }
        $('.cat-dropdown').navgoco();

});
</script>
