function posts_view_ajax(posts_account){
        first_post_id = $('#posts_account').children().last().data('post_id');
        let user_current_slug =  posts_account.data('user_current_slug');
        let count_elem = 5;
        let data = {};
        data.first_post_id = first_post_id;
        data.user_current_slug = user_current_slug;
        data.count_elem = count_elem;
        // let url = "{% url 'account:account_pos_one_show' %}"
        $.ajax({
            url: "/account/account_post_one_show/",
            type:'GET',
            data: data,
            // cache: true,
            success: function (response){
                $("#posts_account").append(response);
                // console.log('OK')
                r_response = response.replace(/\s/g, '')
                if (r_response.length==0){
                    $('#posts_account').data('post_bool_status', '1')
                }
            },
            error: function (response){
                // console.log('ERR')
            }
        })
    }


$(document).ready(function (){
    let posts_account = $('#posts_account');
    posts_view_ajax(posts_account);
	$(window).scroll(function () {
        let posts_account = $('#posts_account');
        let scrool_bool = false;
        if ($('#posts_account').data('post_bool_status') != '1'){
            if (($(window).scrollTop() >= $(document).height() - $(window).height())) {
                let posts_accounts = $('#posts_account')
                post_bool_status = posts_view_ajax(posts_account);
                window_height = $(document).height() - $(window).height()

            }
        }
	})
})