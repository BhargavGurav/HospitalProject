
$(document).ready(function(){
    var verify = $('#chk_td').length;
    if (verify == 0){
        $('#no-data').text('No data found');
    }
});

setInterval(function(){
    let date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

function validateEmail(email){
    var regex =  /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateAll(){
    var name = $('#name').val();
    var phone = $('#phone').val();
    var email = $('#email').val();
    var age = $('#age').val();
    var gender = $('#gender').val();
    
    if(name == ''){
        swal('Oops !', 'Name field can not be empty !', 'error')
        return false;
    }
    else if(name.split(' ').length < 2){
        swal('Oops !', 'Please enter last name also', 'info')
        return false;
    }
    else if(email == ''){
        swal('Oops !', 'Email field can not be empty !', 'error')
        return false;
    }
    else if(!(validateEmail(email))){
        swal('Oops !', 'Please enter a valid email', 'error')
        $('#email').val('');
        return false;
    }
    else if(phone == ''){
        swal('Oops !', 'Phone field can not be empty !', 'error')
        return false;
    }
    else if(age == ''){
        swal('Oops !', 'Age field can not be empty !', 'error')
        return false;
    }
    else if(parseInt(age) > 110){
        swal('Oops !', 'Please enter a valid age !', 'error')
        return false;
    }
    else if(gender == ''){
        swal('Oops !', 'Gender field can not be empty !', 'error')
        return false;
    }
    else{
        console.log(name.split(' '));
        return true;
    }
}

$('#btn-add').bind("click", validateAll);

$(document).ready(function(){
    jQuery('input[name="name"]').keyup(function(){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');  /* replacing space*/
        jQuery(this).val(allow);
    });

    $('input').on('keypress', function(e) { 
        if (e.which === 32 && !this.value.length)
        e.preventDefault();
    });

});

$('#name').keyup(function(){
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){
        return $1.toUpperCase( );
    }))
})


$(document).ready(function(){
    $('#phone').inputmask('+919999999999', {'onincomplete': function(){
        swal('Oops !', 'Please enter full contact number.', 'info')
        return false;
    }})
})

$(document).ready(function(){
    $('#email').keyup(function(){
        this.value = this.value.toLowerCase();
    });
})

$('#age').keyup(function(){
    if(!/^[0-9]*$/.test(this.value)){
        this.value = this.value.split(/[^0-9]/).join('');
    }
})
