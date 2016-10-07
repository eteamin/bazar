<header class="top-ribbon">

  <div class="container">

    <div class="grid-xs-12 grid-md-1">
      <a href="/" id="mainLogo"></a>
    </div>
    <div class="account_nav">
        <ul>
        % if 'user_name' in session:
            <li>
                <a>${session['user_name']} خوش آمدید</a>
            </li>

            <li>
                <a href="${tg.url('/account/log_out')}">خروج</a>
            </li>
        % else:
            <li>
                <a href="${tg.url('/account/sign_in')}">ورود</a>
            </li>

            <li>
                <a href="${tg.url('/account/sign_up')}">ثبت نام</a>
            </li>
        % endif
        </ul>
    </div>

    <div class="grid-xs-0 grid-md-6">
    </div>
  <span class="pull-left persian-date">
    ${h.persian_date()}
  </span>
  </div>
</header>

<%def name="script()">
  <script>
    twa.Logo.get($('#mainLogo'));
    twa.LogoType.get($('#logotype'));
  </script>
</%def>
