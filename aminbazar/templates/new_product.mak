<%inherit file="local:templates.master" />
<%def name="title()">Login Form</%def>

<div class="centralized">
    <form action="${tg.url('/products/submit_product')}"
          method="post" accept-charset="UTF-8" class="login" enctype="multipart/form-data">

      <div class="form-group">
        <label class="col-sm-12 control-label">نام محصول:</label>
          <input class="form-control" type="text" name="title" required/>
      </div>

      <div class="form-group">
        <label class="field_labels">سال تولید:</label>
          <input class="form-control" type="number" name="year_of_production" required/>
      </div>

      <div class="form-group">
        <label class="field_labels">کشور سازنده:</label>
          <input class="form-control" type="text" name="country_of_production" required/>
      </div>

      <div class="form-group">
        <label class="field_labels">تعداد:</label>
          <input class="form-control" type="number" name="quantity" required/>
      </div>

      <div class="form-group">
        <label class="field_labels">قیمت هر واحد (تومان):</label>
          <input class="form-control" type="number" name="price" required/>
      </div>

        <div class="form-group">
            <label class="field_labels">دسته بندی محصول</label>
                <select name="sub_category_id" class="form-control" required>
                  %for s in sub_categories:
                  <option value="${s.id}">${s.title}</option>
                  %endfor
                </select>
        </div>
      <div class="form-group">
        <label class="field_labels">تصویر کالا:</label>
          <input class="form-control" type="file" name="image" required/>
      </div>

      <div class="form-group">
        <div class="col-sm-10 col-sm-offset-2">
          <input type="submit" value="ثبت"  class="mybutton">
        </div>
      </div>
    </form>

</div>
