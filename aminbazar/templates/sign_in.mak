<%inherit file="local:templates.master"/>
<%def name="title()">Login Form</%def>

<div class="centralized">
  <div class="col-md-8 col-md-offset-1">
    <form action="${tg.url('/account/login')}"
          method="post" accept-charset="UTF-8" class="login">

      <div class="form-group">
        <label class="col-sm-10 control-label">نام کاربری:</label>
          <input class="form-control" type="text" name="user_name" style="width: 302px;"/>
      </div>

      <div class="form-group">
        <label class="col-sm-2 control-label">رمز عبور:</label>
          <input class="form-control" type="password" name="password" style="width: 302px;"/>
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
          <button type="submit" class="btn btn-default">ورود</button>
        </div>
      </div>
        <div class="col-sm-10 col-sm-offset-2">
            <button type="button" onclick="location.href='${tg.url("/account/sign_up")}'">ثبت نام</button>
        </div>
    </form>

  </div>
</div>
