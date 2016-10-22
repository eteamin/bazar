<%inherit file="local:templates.master"/>
<%def name="title()">Login Form</%def>
-
<div class="centralized">
    <form action="${tg.url('/account/login')}"
          method="post" accept-charset="UTF-8" class="login">

      <div class="form-group">
        <label class="col-sm-12 control-label">نام کاربری:</label>
          <input class="form-control" type="text" name="user_name" required/>
      </div>

      <div class="form-group">
        <label class="col-sm-12 control-label">رمز عبور:</label>
          <input class="form-control" type="password" name="password" required/>
      </div>

      <div class="form-group">
        <div class="col-sm-10 col-sm-offset-2">
          <div class="checkbox">
            <label>
              <input type="checkbox" name="remember" value="2252000"/> مرا به خاطر بسپار
            </label>
          </div>
        </div>
      </div>

      <div class="form-group">
        <div class="col-sm-10 col-sm-offset-2">
          <input type="submit" value="ورود"  class="mybutton">
        </div>
      </div>
    </form>

</div>
