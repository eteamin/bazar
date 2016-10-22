<%inherit file="local:templates.master" />
<h3>${title}</h3>
<div class="section group">
    % for p in products:
      <div class="grid_1_of_4 images_1_of_4">
         <h4><a href="#">${p.title}</a></h4>
          <a href="${tg.url('/products/details')}/${p.id}"><img src="${p.image.url}" alt="" /></a>
          <div class="price-details">
           <div class="price-number">
                <p><span class="rupees">${p.price}</span> تومان</p>
            </div>
                    <div class="add-cart">
                        <h4><a href="${tg.url('/products/details')}/${p.id}">جزئیات</a></h4>
                        <h4><a class="delete-product" href="${tg.url('/products/remove_product')}/${p.id}">حذف</a></h4>
                     </div>
                 <div class="clear"></div>
        </div>
    </div>
    % endfor

</div>
    <p class="pagelist">
        <a class="prevPage" href="?page=${tmpl_context.paginators.products.previous_page}">&lt;&lt;&lt;</a>
        ${tmpl_context.paginators.products.pager(format='~3~', page_param='page', show_if_single_page=False)}
        <a class="nextPage" href="?page=${tmpl_context.paginators.products.next_page}">&gt;&gt;&gt;</a>
    </p>

<script>
    $(document).ready(function() {
    $(".delete-product").click(function() {
        return confirm('آیا از حذف اطمینان دارید؟')
    });
});
</script>