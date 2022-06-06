function view_accounts(text_search,filters_account_location,filters_account_gender,filters_account_id_age_from,filters_account_id_age_up_to){
    let data = {};
    let count_elem = 3;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.filters_account_location = filters_account_location;
    data.filters_account_gender = filters_account_gender;
    data.filters_account_id_age_from = filters_account_id_age_from;
    data.filters_account_id_age_up_to = filters_account_id_age_up_to;
    $.ajax({
        url: "/search/accounts/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
            $("#result_account").append(response);
            console.log('OK account')
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}

function view_masters(text_search){
    let data = {};
    let count_elem = 3;
    data.count_elem = count_elem;
    $.ajax({
        url: "/search/masters/",
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

function view_posts(text_search){
    let data = {};
    let count_elem = 3;
    data.count_elem = count_elem;
    $.ajax({
        url: "/search/posts/",
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

function view_service(text_search){
    let data = {};
    let count_elem = 3;
    data.count_elem = count_elem;
    $.ajax({
        url: "/search/service/",
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

    let btn_all = $('#btn_all');  //Кнопка все
    btn_all.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_all");
        let text_search = $('#text_search').val();

    });


    let btn_account = $('#btn_account');   //Кнопка люди
    btn_account.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_account");
        let text_search = $('#text_search').val();
        let filters_account_location=$('#filters_account_location').val();
        let filters_account_gender=$('#filters_account_id_gender').val();
        let filters_account_id_age_from=$('#filters_account_id_age_from').val();
        let filters_account_id_age_up_to=$('#filters_account_id_age_up_to').val();
        view_accounts(text_search,filters_account_location,filters_account_gender,filters_account_id_age_from,filters_account_id_age_up_to)


    });


    let btn_master = $('#btn_master');   //Кнопка мастера
    btn_master.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_master");
        let text_search = $('#text_search').val();
    });


    let btn_post = $('#btn_post');     //Кнопка посты
    btn_post.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_post");
        let text_search = $('#text_search').val();
    });


    let btn_service = $('#btn_service');     //Кнопка объявления
    btn_service.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_service");
        let text_search = $('#text_search').val();
    });


    let text_search = $('#text_search');
    text_search.keydown(function (e){   //собфтие нажатия интер на строке ввода
        if(e.keyCode ===13){
            let btn_group_value = $('#btn_group').data("btn_group_value");
            let text_search = $('#text_search').val();
        }
    })
})