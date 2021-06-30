$(document).ready(function () {
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
   //Refresh
    $('a[name="btn_refresh_change_password"]').on("click", function(){
       $('#error_confirm_password').empty();
       $('#error_new_password').empty();
       $('#oldPassword').val('');
       $('#newPassword').val('');
       $('#renewPassword').val('');
       $('a[name="btn_refresh_change_password"]').attr('disabled', true);
    });
    //Change fullname
    $('#fullName, #fullname_teacher').on('keyup', function () {
        if($('#fullname_teacher').val() != '') {
            $('#fullname_display').val($('#fullname_teacher'))
        } else {
            $('#fullname_display').val($('#fullName'))
        }
    });
});
