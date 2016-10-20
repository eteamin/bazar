<%inherit file="local:templates.master" />
<h3>محصولات امین بازار</h3>
<div class="section group">
    % for p in products:
      <div class="grid_1_of_4 images_1_of_4">
         <h4><a href="#">${p.title}</a></h4>
          <a href="${tg.url('/products/details')}/${p.id}"><img src="${p.image.url}" alt="" /></a>
          <div class="price-details">
           <div class="price-number">
                <p><span class="rupees">${p.price} تومان</span></p>
            </div>
                    <div class="add-cart">
                        <h4><a href="${tg.url('/products/details')}/${p.id}">جزئیات</a></h4>
                     </div>
                 <div class="clear"></div>
        </div>
    </div>
    % endfor
</div>
<div class="product-articles">
  <h3>آخرین اخبار</h3>
  <ul>
    <li>
  <div class="article">
    <p><span>عنوان</span></p>
    <p>شرح خبر</p>
    <p><a href="#">+ متن کامل</a></p>
  </div>
  </li>
  </ul>
</div>

