<%inherit file="local:templates.master" />
<%
    address = "products/remove_product/"
%>
<div class="product-content-area">
    <img src="${product.image.url}">
    <h3>جزئیات محصول</h3>
    <ul class="product-grid">
        <li>
            <span class="product-label">عنوان محصول</span>
            <span class="product-info">${product.price}</span>
        </li>
        <li>
            <span class="product-label">سال تولید</span>
            <span>${product.price}</span>
        </li>
        <li>
            <span class="product-label"> تولید کننده</span>
            <span>${product.price}</span>
        </li>
        <li>
            <span class="product-label">تعداد</span>
            <span>${product.price}</span>
        </li>
        <li>
            <span class="product-label">قیمت</span>
            <span>${product.price}</span>
        </li>
        <li>
            <span class="product-label">اطلاعات فروشنده</span>
            <span>${product.price}</span>
        </li>


         % if 'user_name' in session and session['user_name'] == product.account.user_name:
            <li class="col-sm-1"><p>اعمال تغییرات</p></li>
         % endif

##         <div class="col-sm-2"><p>${product.title}</p></div>
##         <div class="col-sm-1"><p>${product.year_of_production}</p></div>
##         <div class="col-sm-2"><p>${product.country_of_production}</p></div>
##         <div class="col-sm-1"><p>${product.quantity}</p></div>
##         <div class="col-sm-1"><p>${product.price}</p></div>
##         <div class="col-sm-1"><p>${product.account.bio}</p></div>
##         % if 'user_name' in session and session['user_name'] == product.account.user_name:
##             <div class="col-sm-1"><a href="${tg.url('/')}${address}${product.id}"><p>حذف محصول</p></a></div>
##         % endif

    </ul>
</div>
