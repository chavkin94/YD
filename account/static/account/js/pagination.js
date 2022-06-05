function posts_view_ajax(posts_all_view){
        first_post_id = $('#posts_all_view').children().last().data('post_id');
        let user_master_current_slug =  posts_all_view.data('user_master_current_slug');
        let count_elem = 5;
        let data = {};
        let type_posts =  posts_all_view.data('type_posts');
        data.first_post_id = first_post_id;
        data.user_master_current_slug = user_master_current_slug;
        data.count_elem = count_elem;
        data.type_posts = type_posts;
        // let url = "{% url 'account:account_pos_one_show' %}"
        $.ajax({
            url: "/account/account_post_one_show/",
            type:'GET',
            data: data,
            // cache: true,
            success: function (response){
                $("#posts_all_view").append(response);
                // console.log('OK')
                r_response = response.replace(/\s/g, '')
                if (r_response.length==0){
                    $('#posts_all_view').data('post_bool_status', '1')
                }
            },
            error: function (response){
                // console.log('ERR')
            }
        })
    }


$(document).ready(function (){
    let posts_all_view = $('#posts_all_view');
    posts_view_ajax(posts_all_view);
	$(window).scroll(function () {
        let posts_all_view = $('#posts_all_view');
        let scrool_bool = false;
        if ($('#posts_all_view').data('post_bool_status') != '1'){
            if ((($(window).scrollTop() >= $(document).height() - $(window).height()))&&($(document).height() - $(window).height()!=0)) {
                let posts_all_views = $('#posts_all_view')
                post_bool_status = posts_view_ajax(posts_all_view);
                window_height = $(document).height() - $(window).height()

            }
        }
	})
})