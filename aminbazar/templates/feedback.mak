<%inherit file="local:templates.master" />
<script src='https://www.google.com/recaptcha/api.js?hl=fa'></script>
<script src='/js/recaptcha_validation.js'></script>

<h2>${page.header}</h2>

<form onsubmit="return checkRecatpcha();" class="feedback" action="${tg.url('/feedback/submit_feedback')}" method="post">
    <div class="feedback-header">جهت ارتباط با مدیریت سایت می توانید از فرم زیر استفاده نمایید.</div>
    <fieldset>

        <label for="name-input">
            <span class="main-label">نام:</span>
            <input name="name" type="text" placeholder="لطفا نام خود را وارد کنید" required title="این فیلد نمی تواند خالی باشد">
        </label>

        <label for="email-input">
            <span class="main-label">نام خانوادگی:</span>
            <input name="last_name" type="text" placeholder="لطفا نام خانوادگی خود را وارد کنید" required title="این فیلد نمی تواند خالی باشد">
        </label>

        <label for="email-input">
            <span class="main-label">پست الکترونیک:</span>
            <input name="email" type="email" placeholder="پست الکترونیک خود را وارد کنید" required title="لطفا آدرس ایمیل را با فرمت صحیح وارد کنید" >
        </label>

        <label for="description-input">
            <span class="main-label">نظرات و توضیحات:</span>
            <textarea name="desc" rows="6" cols="50" placeholder="نظرات و توضیحات خود را بنویسید" required title="این فیلد نمی تواند خالی باشد"></textarea>
        </label>

    </fieldset>
    <div class="g-recaptcha" data-sitekey=${tg_config.get('recaptcha.public_key')}></div>
    <button type="submit">ارسال</button>


</form>
