$(document).ready(function (){
    var form = $('#form_subscripe_unsubscripe');
    form.on('submit', function (e){
        e.preventDefault();
       var submit_btn_subscripe_unsubscripe = $('#submit_btn_subscripe_unsubscripe');
       var user_current_slug = submit_btn_subscripe_unsubscripe.data("user_current_slug");
       var user_slug = submit_btn_subscripe_unsubscripe.data("user_slug");
       var master_slug = submit_btn_subscripe_unsubscripe.data("master_slug");
       var url_type = submit_btn_subscripe_unsubscripe.data("url_type");
        if ($('#submit_p').text() == 'Отписаться'){
            $('#submit_p').text('Подписаться')
        }
        else if($('#submit_p').text() == 'Подписаться') {
            $('#submit_p').text('Отписаться')
        }

        var data = {};
        data.user_current_slug = user_current_slug;
        data.user_slug = user_slug;
        data.master_slug = master_slug;
        data.url_type = url_type;
        var csrf_token = $('#form_subscripe_unsubscripe [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");
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
})