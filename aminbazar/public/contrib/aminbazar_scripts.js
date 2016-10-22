/**
 * Created by amin on 7/26/16.
 */

function validateForm() {
    var recaptcha_value = document.querySelector('.g-recaptcha-response').value;
    var password = document.querySelector('#password').value;
    var confirmPassword = document.querySelector('#confirmPassword').value;
    if (recaptcha_value == null || recaptcha_value == "") {
        alert("با کلیک بر روی جعبه زیر نشان دهید که ربات نیستید");
        return false;
    }
    else if (password != confirmPassword) {
        alert("رمز عبور و تکرار رمز عبور باید مشابه باشند.");
        return false;
    }
}
