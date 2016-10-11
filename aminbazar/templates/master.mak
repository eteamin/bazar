<!DOCTYPE HTML>
  <%
    min = '' if h.is_debug() else '.min'
  %>
<head>
${self.page_title()}
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link rel="stylesheet" type="text/css" media="screen" href="/css/public${min}.css"/>
    <script src="/js/public${min}.js"></script>
</head>
<body>
	<div class="header">
  	  		<div class="wrap">
				<div class="header_top">
					<div class="logo">
						<a href="${tg.url('/')}"><img src="img/logo.png" alt="" /></a>
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
  		    <div class="navigation">
  		    	<a class="toggleMenu" href="#">Menu</a>
					<ul class="nav">
						<li>
							<a href="index.html">خانه</a>
						</li>
						<li  class="test">
							<a href="#">کالا</a>
							<ul>
								<li>
									<a href="#">آشپزی</a>
									<ul>
										<li><a href="#">پنیر</a></li>
										<li><a href="#">Pressure Cookers</a></li>
									</ul>
								</li>
								<li>
									<a href="#">Storage</a>
									<ul>
										<li><a href="#">Bottles & Sippers</a></li>
										<li><a href="#">Containers & Jars</a></li>
									</ul>
								</li>
								<li>
									<a href="#">Cutlery & Tableware</a>
									<ul>
										<li><a href="#">Cutlery</a></li>
										<li><a href="#">Condiment Sets</a></li>
									</ul>
								</li>
								<li>
									<a href="#">Bar Accessories</a>
									<ul>
										<li><a href="#">Bottle Openers</a></li>
										<li><a href="#">Flasks</a></li>
									</ul>
								</li>
							</ul>
						</li>
						<li>
							<a href="contact.html">ارتباط با ما</a>
						</li>
					</ul>
					 <span class="left-ribbon"> </span>
      				 <span class="right-ribbon"> </span>
  		    </div>
  		     <div class="header_bottom">
			   <div class="slider-text">
			   	<h2>Lorem Ipsum Placerat <br/>Elementum Quistue Tunulla Maris</h2>
			   	<p>Vivamus vitae augue at quam frigilla tristique sit amet<br/> acin ante sikumpre tisdin.</p>
			   	<a href="#">Sitamet Tortorions</a>
	  	      </div>
	  	      <div class="slider-img">
	  	      	<img src="img/slider-img.png" alt="" />
	  	      </div>
	  	     <div class="clear"></div>
	      </div>
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
		          	<div class="wrap">
		          	 <div class="ocarousel_slider">
	      				<div class="ocarousel example_photos" data-ocarousel-perscroll="3">
			                <div class="ocarousel_window">
			                   <a href="#" title="img1"> <img src="img/latest-product-img1.jpg" alt="" /><p>Nuncvitae</p></a>
			                </div>
			               <span>
			                <a href="#" data-ocarousel-link="left" style="float: left;" class="prev"> </a>
			                <a href="#" data-ocarousel-link="right" style="float: right;" class="next"> </a>
			               </span>
					   </div>
				     </div>
				   </div>
    	       </div>
    	  <div class="content_bottom">
    	    <div class="wrap">
    	    	<div class="content-bottom-left">
    	    		<div class="categories">
						   <ul>
						  	   <h3>جستجو</h3>
							      <li><a href="#">Appliances</a></li>
						  	 </ul>
						</div>
						<div class="buters-guide">
						<h3>Buyers Guide</h3>
						<p><span>We want you to be happy with your purchase.</span></p>
						<p>So we're committed to giving you all the tools to make the right decision with minimum fuss. </p>
					  </div>
					  <div class="add-banner">
					  	<img src="img/camera.png" alt="" />
					  	<div class="banner-desc">
					  		<h4>Electronics</h4>
					  	    <a href="#">More Info</a>
					  	</div>
					  	<div class="clear"></div>
					  </div>
					    <div class="add-banner add-banner2">
					  	<img src="img/computer.png" alt="" />
					  	<div class="banner-desc">
					  		<h4>Computers</h4>
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
     <script type="text/javascript" src="/js/navigation.js"></script>
</body>
</html>
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

