<%inherit file="local:templates.master" />
<div class="product-thumbnails">
    %if products:
        <h2>محصولات دسته بندی ${products[0].sub_category.title}</h2>
        <ul>
            %for p in products:
                <li>
                    <div class="product_image">
                        <a href="${tg.url('/products/details/')}${p.id}">
                            <img src="${p.image.url}"/>
                        </a>
                    </div>
                    <div class="product_details">
                        <p>${p.title}</p>
                    </div>
                    <div class="product_quantity">
                        <p>تعداد ${p.quantity}</p>
                    </div>
                    <div class="product_price">
                        <p>${p.price}     تومان</p>
                    </div>
                </li>
            %endfor
        </ul>
    %else:
        <h4>هیچ محصولی وجود ندارد</h4>
    %endif
</div>
