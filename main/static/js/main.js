// $(document).ready(function (){
//     var form = $('#form_buying_product');
//     console.log(form);
//     form.on('submit', function (e){
//         e.preventDefault();
//        console.log('123');
//        var nmb = $('#number').val();
//        console.log(nmb);
//        var submit_btn = $('#submit_btn');
//        var product_id = submit_btn.data("product_id");
//         console.log(product_id);
//         $('#submit_btn').text('Ура')
//
//
//     });

$(document).ready(function (){
var form = $('#form_buying_product');
console.log(form);
form.on('submit', function (e){
    e.preventDefault();
   console.log('123');
   var nmb = $('#number').val();
   console.log(nmb);
   var submit_btn = $('#submit_btn');
   var user_id = submit_btn.data("user_id");
    console.log(user_id);
    $('#submit_btn').text('Ура')

    var data = {};
    data.user_id = user_id;
    data.nmb = nmb;
    var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
    data["csrfmiddlewaretoken"] = csrf_token;
    var url = form.attr("action");
    console.log(data)
    $.ajax({
        url: url,
        type:'POST',
        data: data,
        cache: true,
        success: function (data){
            console.log('OK')
        },
        error: function (data){
            console.log('ERR')
        }
    })
});




    // $(".btn").click(function (){
    //     $.ajax({
    //         url: '',
    //         type: 'get',
    //         data:{
    //             button_text: $(this).text()
    //         },
    //         success: function(response) {
    //             $(".btn").text(response.seconds)
    //             $("$seconds").append('<li>' + response.seconds + '</li>')
    //         }
    //     })
    // })
})