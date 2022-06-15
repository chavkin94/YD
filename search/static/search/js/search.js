function view_accounts(text_search,filters_account_location,filters_account_gender){
    let data = {};
    let count_elem = 3;
    first_account_id = $('#result_account').children().last().data('account');
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.filters_account_location = filters_account_location;
    data.filters_account_gender = filters_account_gender;
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    data.first_account_id = first_account_id;
    $.ajax({
        url: "/search/accounts/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
            $("#result_account").append(response);
            // console.log('OK account')
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}


function filter_account(){
    $('#btn_group').data("btn_group_value", "btn_account");
    let text_search = $('#text_search').val();
    let filters_account_location=$('#filters_account_location').val();
    let filters_account_gender=$('#filters_account_id_gender').val();
    $("#result_search").html ('<p>---Пользователи---</p><div id="result_account"></div>');
    view_accounts(text_search,filters_account_location,filters_account_gender)
}

function view_masters(text_search, filters_master_id_location){
    let data = {};
    let count_elem = 3;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.filters_master_id_location = filters_master_id_location;
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    $.ajax({
        url: "/search/masters/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
            $("#result_master").append(response);
            // console.log('OK account')
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}


function filter_master(){
    $('#btn_group').data("btn_group_value", "btn_master");
    let text_search = $('#text_search').val();
    let filters_master_id_location=$('#filters_master_id_location').val();
    $("#result_search").html ('<p>---Мастера---</p><div id="result_master"></div>');
    view_masters(text_search,filters_master_id_location)
}

function view_posts(text_search){
    let data = {};
    let count_elem = 3;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    $.ajax({
        url: "/search/posts/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
            $("#result_post").append(response);
            // console.log('OK account')
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}


function filter_post(){
    $('#btn_group').data("btn_group_value", "btn_post");
    let text_search = $('#text_search').val();
    $("#result_search").html ('<p>---Посты---</p><div id="result_post"></div>');
    view_posts(text_search)
}


function view_service(text_search, filters_service_id_service_category){
    let data = {};
    let count_elem = 3;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    data.filters_service_id_service_category = filters_service_id_service_category;
    $.ajax({
        url: "/search/services/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
             $("#result_service").append(response);
            // console.log('OK')
            // r_response = response.replace(/\s/g, '')
            // if (r_response.length==0){
            //     $('#posts_all_view').data('post_bool_status', '1')
            // }
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}


function filter_service(){
    $('#btn_group').data("btn_group_value", "btn_service");
    let text_search = $('#text_search').val();
    $("#result_search").html ('<p>---Услуги---</p><div id="result_service"></div>');
    let filters_service_id_service_category=$('#filters_service_id_service_category').val();
    view_service(text_search, filters_service_id_service_category)
}


function view_all(){
    $('#btn_group').data("btn_group_value", "btn_all");
    $("#result_search").html ('<p>---Пользователи---</p><div id="result_account"></div><p>---Мастера---</p><div id="result_master"></div><p>---Посты---</p><div id="result_post"></div><p>---Услуги---</p><div id="result_service"></div>');
    let text_search = $('#text_search').val();
    view_accounts(text_search,'','')
    view_masters(text_search,'')
    view_posts(text_search)
    view_service(text_search)
}



$(document).ready(function (){
    view_all();
    let btn_all = $('#btn_all');  //Кнопка все
    btn_all.on('click', function() {
        view_all();
    });


    let btn_account = $('#btn_account');
    btn_account.on('click', function() {
        filter_account();
    });

    let filters_account_id_gender = $('#filters_account_id_gender');
    filters_account_id_gender.change(function (){
        filter_account();
    })



    let btn_master = $('#btn_master');
    btn_master.on('click', function() {
        filter_master();
    });

    let filters_master_id_location = $('#filters_master_id_location');
    filters_master_id_location.change(function (){
        filter_master();
    })


    let btn_post = $('#btn_post');
    btn_post.on('click', function() {
        filter_post();
    });


    let btn_service = $('#btn_service');
    btn_service.on('click', function() {
        filter_service();
    });


    let filters_service_id_service_category = $('#filters_service_id_service_category');
    filters_service_id_service_category.change( function() {
        filter_service();
    });


    let text_search = $('#text_search');
    text_search.keydown(function (e){   //собфтие нажатия интер на строке ввода
        if(e.keyCode ===13){
            if (($('#btn_group').data("btn_group_value")) == "btn_all"){
                view_all();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_account"){
                filter_account();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_master"){
                filter_master();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_post"){
                filter_post();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_service"){
                filter_service();
            }
        }
    })
})