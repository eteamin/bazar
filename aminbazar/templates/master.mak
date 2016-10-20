<!DOCTYPE HTML>
  <%
    min = '' if h.is_debug() else '.min'
  %>
<head>
${self.page_title()}
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

<link rel="stylesheet" type="text/css" media="screen" href="/css/public${min}.css"/>
    <link rel="stylesheet" type="text/css" href="/contrib/slick.css"/>
    <link rel="stylesheet" type="text/css" href="/contrib/slick-theme.css"/>
<script src="/js/public${min}.js"></script>
    <script src="/contrib/slick.min.js"></script>
</head>
<body>
	<div class="header">
  	  		<div class="wrap">
				<div class="header_top">
					<div class="logo">
						<h1><a href="" style="color: #b94a48;">AminBazaar</a></h1>
					</div>
## 						<div class="header_top_right">
## 							  <div class="search_box">
## 							  	<span>Search</span>
## 					     		<form>
## 					     			<input type="text" value=""><input type="submit" value="">
## 					     		</form>
## 					     		<div class="clear"></div>
## 					     	</div>
## 					</div>
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
                    <a class="navbar-brand" href="#">امین بازار</a>
                </div>

                <div class="collapse navbar-collapse js-navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li class="dropdown mega-dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">دسته بندی ها <span class="caret"></span></a>
                            <ul class="dropdown-menu mega-dropdown-menu">
                                <li class="col-sm-3">
                                    <ul>
                                        <li class="dropdown-header">Men Collection</li>
                                        <div id="menCollection" class="carousel slide" data-ride="carousel">
                                          <div class="carousel-inner">
                                            <div class="item active">
                                                <a href="#"><img src="" class="img-responsive" alt="product 1"></a>
                                                <h4><small>Summer dress floral prints</small></h4>
                                                <button class="btn btn-primary" type="button">49,99 €</button> <button href="#" class="btn btn-default" type="button"><span class="glyphicon glyphicon-heart"></span> Add to Wishlist</button>
                                            </div><!-- End Item -->
                                            <div class="item">
                                                <a href="#"><img src="" class="img-responsive" alt="product 2"></a>
                                                <h4><small>Gold sandals with shiny touch</small></h4>
                                                <button class="btn btn-primary" type="button">9,99 €</button> <button href="#" class="btn btn-default" type="button"><span class="glyphicon glyphicon-heart"></span> Add to Wishlist</button>
                                            </div><!-- End Item -->
                                            <div class="item">
                                                <a href="#"><img src="" class="img-responsive" alt="product 3"></a>
                                                <h4><small>Denin jacket stamped</small></h4>
                                                <button class="btn btn-primary" type="button">49,99 €</button> <button href="#" class="btn btn-default" type="button"><span class="glyphicon glyphicon-heart"></span> Add to Wishlist</button>
                                            </div><!-- End Item -->
                                          </div><!-- End Carousel Inner -->
                                          <!-- Controls -->
                                          <a class="left carousel-control" href="#menCollection" role="button" data-slide="prev">
                                            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                            <span class="sr-only">Previous</span>
                                          </a>
                                          <a class="right carousel-control" href="#menCollection" role="button" data-slide="next">
                                            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                            <span class="sr-only">Next</span>
                                          </a>
                                        </div><!-- /.carousel -->
                                        <li class="divider"></li>
                                        <li><a href="#">View all Collection <span class="glyphicon glyphicon-chevron-right pull-right"></span></a></li>
                                    </ul>
                                </li>
                                <li class="col-sm-3">
                                    <ul>
                                        <li class="dropdown-header">Features</li>
                                        <li><a href="#">Auto Carousel</a></li>
                                        <li><a href="#">Carousel Control</a></li>
                                        <li><a href="#">Left & Right Navigation</a></li>
                                        <li><a href="#">Four Columns Grid</a></li>
                                        <li class="divider"></li>
                                        <li class="dropdown-header">Fonts</li>
                                        <li><a href="#">Glyphicon</a></li>
                                        <li><a href="#">Google Fonts</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li><a href="#">ارتباط با ما</a></li>
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">حساب کاربری <span class="caret"></span></a>
                      <ul class="dropdown-menu" role="menu">
                         % if 'user_name' not in session:
                         <li><a href="#">ورود</a></li>
                        <li><a href="#">ثبت نام</a></li>
                         %else:
                             <li><a href="#">محصولات من</a></li>
                         %endif
                      </ul>
                    </li>
                  </ul>
                </div><!-- /.nav-collapse -->
              </nav>
            </div>

  		     <div class="header_bottom">
			   <div class="slider-text">
			   	<h2>امین بازار</h2>
			   	<p>شعار امین بازار</p>
			   	<a href="#">درباره ی ما</a>
	  	      </div>
	  	      <div class="slider-img">
	  	      	<img src="/images/slider-img.png" alt="" />
	  	      </div>
	  	     <div class="clear"></div>
	      </div>
   		</div>

   <!------------End Header ------------>
  <div class="main">
      <div class="content">
    	        <div class="content_top">
    	        	<div class="wrap">
		          	   <h3>آخرین محصولات</h3>
		          	</div>
		          	<div class="line"> </div>
                        <div class="slicker">
                          <div class="item"><a href="#" title="img1"> <img src="/images/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a></div>
                            <div class="item"><a href="#" title="img1"> <img src="/images/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a></div>
                            <div class="item"><a href="#" title="img1"> <img src="/images/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a></div>
                            <div class="item"><a href="#" title="img1"> <img src="/images/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a></div>
                            <div class="item"><a href="#" title="img1"> <img src="/images/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a></div>
                            <div class="item"><a href="#" title="img1"> <img src="/images/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a></div>
                            <div class="item"><a href="#" title="img1"> <img src="/images/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a></div>
                        </div>
                </div>
				   </div>
    	       </div>
    	       </div>
    	  <div class="content_bottom">
    	    <div class="wrap">
    	    	<div class="content-bottom-left">
    	    		<div class="categories">
						   <ul>
						  	   <h3>دسته بندی ها</h3>
							      <li><a href="#">ورزشی</a></li>
						  	 </ul>
						</div>
						<div class="buters-guide">
						<h3>راهنمای سایت</h3>
						<p><span>راهنمای امین بازار</span></p>
						<p>توضیحات بیشتر </p>
					  </div>
					  <div class="add-banner">
					  	<img src="img/camera.png" alt="" />
					  	<div class="banner-desc">
					  		<h4>Electronics</h4>
					  	    <a href="#">More Info</a>
					  	</div>
					  	<div class="clear"></div>
					  </div>
    	    	</div>
                <div class="content-bottom-right">
                  ${next.body()}
                  ${self.content_wrapper()}
                </div>

		      <div class="clear"></div>
		   </div>
         </div>
   <div class="footer">
   	  <div class="wrap">
		   <div class="footer-nav">
		   	<ul>
		   		<li><a href="#">قوانین سایت</a> : </li>
		   		<li><a href="contact.html">ارتباط با ما</a> : </li>
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
            $('.slicker').slick({
              slidesToShow: 10,
              slidesToScroll: 10,
              autoplay: true,
              autoplaySpeed: 2000
});

    });
</script>
