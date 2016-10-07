<%inherit file="local:templates.scaffold" />
<%
    address = "products/remove_product/"
%>
<div class="product-content-area">
    <img src="${product.image.url}">
    <h3>جزئیات محصول</h3>
    <div class="product-grid-view">
          <div class="row">
            <div class="col-sm-2"><p>نام محصول</p></div>
            <div class="col-sm-1"><p>سال تولید</p></div>
            <div class="col-sm-2"><p>کشور سازنده</p></div>
            <div class="col-sm-1"><p>تعداد</p></div>
            <div class="col-sm-1"><p>قیمت هر واحد (تومان)</p></div>
            <div class="col-sm-1"><p>اطلاعات فروشنده</p></div>
             % if 'user_name' in session and session['user_name'] == product.account.user_name:
                <div class="col-sm-1"><p>اعمال تغییرات</p></div>
             % endif
          </div>

        <div class="row">
            <div class="col-sm-2"><p>${product.title}</p></div>
            <div class="col-sm-1"><p>${product.year_of_production}</p></div>
            <div class="col-sm-2"><p>${product.country_of_production}</p></div>
            <div class="col-sm-1"><p>${product.quantity}</p></div>
            <div class="col-sm-1"><p>${product.price}</p></div>
            <div class="col-sm-1"><p>${product.account.bio}</p></div>
            % if 'user_name' in session and session['user_name'] == product.account.user_name:
                <div class="col-sm-1"><a href="${tg.url('/')}${address}${product.id}"><p>حذف محصول</p></a></div>
            % endif

        </div>
    </div>
</div>
