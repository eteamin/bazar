<%inherit file="local:templates.master" />
<%
    address = "products/remove_product/"
%>
<div class="product-content-area">
    <img src="${product.image.url}">
    <h3>جزئیات محصول</h3>
    <ul class="product-grid">
        <li>
            <div class="product-label">عنوان محصول</div>
            <div class="product-info">${product.price}</div>
        </li>
        <li>
            <div class="product-label">سال تولید</div>
            <div class="product-info">${product.price}</div>
        </li>
        <li>
            <div class="product-label"> تولید کننده</div>
            <div class="product-info">${product.price}</div>
        </li>
        <li>
            <div class="product-label">تعداد</div>
            <div class="product-info">${product.price}</div>
        </li>
        <li>
            <div class="product-label">قیمت</div>
            <div class="product-info"><span class="rupees">${product.price}</span> تومان </div>
        </li>
        <li>
            <div class="product-label">اطلاعات فروشنده</div>
            <div class="product-info">${product.price}</div>
        </li>

         % if 'user_name' in session and session['user_name'] == product.account.user_name:
         <li>
            <div class="product-label">اعمال تغییرات</div>
            <div class="product-info"><a class="delete-product" href="${tg.url('/products/remove_product/')}${product.id}">حذف</a></div>
         </li>
         % endif

    </ul>
</div>


<script>
    $(document).ready(function() {
    $(".delete-product").click(function() {
        return confirm('آیا از حذف اطمینان دارید؟')
    });
});
</script>