<%inherit file="local:templates.master"/>
<%def name="title()">Login Form</%def>
## <script src='https://www.google.com/recaptcha/api.js?hl=fa'></script>
<script src='/js/form_validation.js'></script>

<div class="centralized">
    <form onsubmit="return validateForm();" action="${tg.url('/account/register')}"
          method="post" accept-charset="UTF-8">

      <div class="form-group">
        <label class="col-sm-12 control-label" style="font-size: 14px;">نام کاربری:</label>
          <input class="form-control" type="text" name="user_name" required/>
      </div>

      <div class="form-group">
         <label class="col-sm-12 control-label" style="font-size: 14px;">رمز عبور:</label>
            <input id="password" class="form-control" type="password" name="password" required/>
      </div>

      <div class="form-group">
        <label class="col-sm-12 control-label" style="font-size: 14px;">تکرار رمز عبور:</label>
          <input id="confirmPassword" class="form-control" type="password" name="repeat-password" required/>
      </div>

      <div class="form-group">
         <label class="col-sm-12 control-label" style="font-size: 14px;">آدرس ایمیل:</label>
            <input class="form-control" type="email" name="email_address" required/>
      </div>

      <div class="form-group">
        <label class="col-sm-12 control-label" style="font-size: 14px;">اطلاعات تماس شما:</label>
        <input class="form-control" type="text" name="bio" required/>
      </div>

      <div class="form-group">
         <div class="g-recaptcha" data-sitekey=${tg_config.get('recaptcha.public_key')}></div>
      </div>

      <div class="form-group">
        <div class="col-sm-10 col-sm-offset-2">
          <input type="submit" value="ثبت نام"  class="mybutton">
        </div>
      </div>
    </form>
</div>