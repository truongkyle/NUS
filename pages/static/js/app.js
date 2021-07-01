$(document).ready(function () {
    // Check Password
    $('#newPassword').on('keyup', function () {
        if($('#newPassword').val().length < 10) {
            $('#error_new_password').addClass("text-danger");
            $('#error_new_password').html('Your password must contain 9 characters.');
            $('button[id="btn_change_password"]').attr('disabled', true);
        } else {
            if ((/\d/.test($('#newPassword').val())) && (/[a-z]/.test($('#newPassword').val())) && (/[A-Z]/.test($('#newPassword').val())) && (/[!@#\$%\^\&*\)\(+=._-]/.test($('#newPassword').val()))) {
                $('#error_new_password').removeClass("text-danger").removeClass("text-warning").addClass("text-success");
                $('#error_new_password').html('Your password is strong.');
                $('button[id="btn_change_password"]').attr('disabled', false);
            } else {
                if ((/[A-Z]/.test($('#newPassword').val())) || (/[!@#\$%\^\&*\)\(+=._-]/.test($('#newPassword').val())) || (/\d/.test($('#newPassword').val()))) {
                    $('#error_new_password').removeClass("text-danger").removeClass("text-success").addClass("text-warning");
                    $('#error_new_password').html('Your password is middle.');
                    $('button[id="btn_change_password"]').attr('disabled', false);
                } else {
                    $('#error_new_password').removeClass("text-warning").removeClass("text-success").addClass("text-danger");
                    $('#error_new_password').html('Your password is weak.');
                    $('button[id="btn_change_password"]').attr('disabled', true);
                }
            }
        }
    });
    $('#newPassword, #renewPassword').on('keyup', function () {
        if($('#newPassword').val() !=  $('#renewPassword').val()) {
            $('#error_confirm_password').addClass("text-danger");
            $('#error_confirm_password').html('The two password fields did not match.');
            $('button[id="btn_change_password"]').attr('disabled', true);
        } else {
            if (($('#newPassword').val() == $('#newPassword').val().toLowerCase()) && /[A-Z]/.test($('#newPassword').val()) == false && /[!@#\$%\^\&*\)\(+=._-]/.test($('#newPassword').val()) == false && /\d/.test($('#newPassword').val()) == false) {
                $('#error_confirm_password').html('');
                $('button[id="btn_change_password"]').attr('disabled', true);
            } else {
                $('#error_confirm_password').html('');
                $('button[id="btn_change_password"]').attr('disabled', false);
            }
        }
    });


   //Refresh change password
    $('a[name="btn_refresh_change_password"]').on("click", function(){
       $('#error_confirm_password').empty();
       $('#error_new_password').empty();
       $('#oldPassword').val('');
       $('#newPassword').val('');
       $('#renewPassword').val('');
       $('a[name="btn_refresh_change_password"]').attr('disabled', true);
    });


    //Change fullname
    $('#full_name').on('keyup', function () {
       $('#fullname_display').html($('#full_name').val())
    });


    // Check Phone
    $('#phone').on('keyup', function () {
        if($('#phone').val() == '' || !((/((09|03|07|08|05)+([0-9]{8})\b)/g).test($('#phone').val()))) {
            $('#error_phone').html('Your phone is invalid.');
            $('button[id="btn_save_info_user"]').attr('disabled', true);
        } else {
            $('#error_phone').html('');
            $('button[id="btn_save"]').attr('disabled', false);
        }
    });


    // Check Email
    $('#email').on('keyup', function () {
        if($('#email').val() == '' || !((/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/).test($('#email').val()))) {
            $('#error_email').html('Your email is invalid.');
            $('button[id="btn_save_info_user"]').attr('disabled', true);
        } else {
            $('#error_email').html('');
            $('button[id="btn_save"]').attr('disabled', false);
        }
    });


    //Refresh User Info
    $('a[name="btn_refresh"]').on("click", function(){
       $('#error_phone').empty();
       $('#error_email').empty();
       $('#full_name').val('');
       $('#christian_name').val('');
       $('#homeland').val('');
       $('#phone').val('');
       $('#email').val('');
       $('#birthday').val('');
       $('#position').val(0);
       $('#status').val(0);
       $('#image').val('');
       $('#community').val(0);
       $('#community_name').val('');
       $('#patron').val('');
       $('#address').val('');
       $('#amount').val(0);
       $('#gender').val(0);
       $('#subject').val(0);
       $('#day_of_week').val(0);
       $('#teacher').val(0);
       $('#start_date').val('');
       $('#end_date').val('');
       $('#department').val('');
       $('#position').val('');
       $('#date').val('');
       $('#candidate').val(0);
       $('#report_file').val('');
       $('#schedule_file').val('');
       $('#receipts_and_payments_file').val('');
       $('#note').val('');
    });


    // Change Image
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#profile_image').attr('src', e.target.result);
                $('#default_image').attr('src', e.target.result);
                $('#image_menu').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#image_user_info").change(function(){
        readURL(this);
    });


});
