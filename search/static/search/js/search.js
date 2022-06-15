function view_accounts(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 1;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.filters_account_location = $('#filters_account_location').val();
    data.filters_account_gender = $('#filters_account_id_gender').val();
    data.number_elem = $('#result_search').data("number_elem")
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    $.ajax({
        url: "/search/accounts/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
            $("#result_account").append(response);
            r_response = response.replace(/\s/g, '')
            $('#result_search').data("number_elem", Number($('#result_search').data("number_elem"))+count_elem)
            if (r_response.length==0){
                $('#result_search').data('scroll_bool_status', '1')
            }
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}


function view_masters(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 1;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.filters_master_id_location = $('#filters_master_id_location').val();
    data.number_elem = $('#result_search').data("number_elem")
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    $.ajax({
        url: "/search/masters/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
            $("#result_master").append(response);
            r_response = response.replace(/\s/g, '')
            $('#result_search').data("number_elem", Number($('#result_search').data("number_elem"))+count_elem)
            if (r_response.length==0){
                $('#result_search').data('scroll_bool_status', '1')
            }
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}

function view_posts(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 4;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.number_elem = $('#result_search').data("number_elem")
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    $.ajax({
        url: "/search/posts/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
            $("#result_post").append(response);
            r_response = response.replace(/\s/g, '')
            $('#result_search').data("number_elem", Number($('#result_search').data("number_elem"))+count_elem)
            if (r_response.length==0){
                $('#result_search').data('scroll_bool_status', '1')
            }
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}


function view_service(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 1;
    data.count_elem = count_elem;
    data.text_search = text_search.toLowerCase();
    data.btn_group_value = $('#btn_group').data("btn_group_value")
    data.number_elem = $('#result_search').data("number_elem")
    data.filters_service_id_service_category = $('#filters_service_id_service_category').val();
    $.ajax({
        url: "/search/services/",
        type:'GET',
        data: data,
        // cache: true,
        success: function (response){
             $("#result_service").append(response);
            r_response = response.replace(/\s/g, '')
            $('#result_search').data("number_elem", Number($('#result_search').data("number_elem"))+count_elem)
            if (r_response.length==0){
                $('#result_search').data('scroll_bool_status', '1')
            }
        },
        error: function (response){
            // console.log('ERR')
        }
    })
}


function view_all(){
    $('#btn_group').data("btn_group_value", "btn_all");
    $("#result_search").html ('<p>---Пользователи---</p> <input class="border btn btn-primary m-2 active" id="btn_all_account" type="submit" value="Показать все" onclick="btn_all_account()">' +
        '<div id="result_account"></div>' +
        '<p>---Мастера---</p><input class="border btn btn-primary m-2 active" id="btn_all_master" type="submit" value="Показать все" onclick="btn_all_master()">' +
        '<div id="result_master"></div>' +
        '<p>---Посты---</p><input class="border btn btn-primary m-2 active" id="btn_all_post" type="submit" value="Показать все" onclick="btn_all_post()">' +
        '<div id="result_post"></div>' +
        '<p>---Услуги---</p><input class="border btn btn-primary m-2 active" id="btn_all_service" type="submit" value="Показать все" onclick="btn_all_service()">' +
        '<div id="result_service"></div>');
    let text_search = $('#text_search').val();
    view_accounts(text_search,'','')
    view_masters(text_search,'')
    view_posts(text_search)
    view_service(text_search)
}

function btn_all_account(){
    $('#result_search').data('scroll_bool_status', '0')
    $('#btn_group').data("btn_group_value", "btn_account");
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<p>---Пользователи---</p><div id="result_account"></div>');
    view_accounts()
}

function btn_all_master(){
    $('#result_search').data('scroll_bool_status', '0')
    $('#btn_group').data("btn_group_value", "btn_master");
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<p>---Мастера---</p><div id="result_master"></div>');
    view_masters()
}

function btn_all_post(){
    $('#btn_group').data("btn_group_value", "btn_post");
    $('#result_search').data('scroll_bool_status', '0')
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<p>---Посты---</p><div id="result_post"></div>');
    view_posts()
}

function btn_all_service(){
    $('#btn_group').data("btn_group_value", "btn_service");
    $('#result_search').data('scroll_bool_status', '0')
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<p>---Услуги---</p><div id="result_service"></div>');
    view_service()
}

$(document).ready(function (){

    //Все
    view_all();
    let btn_all = $('#btn_all');  //Кнопка все
    btn_all.on('click', function() {
        view_all();
    });


    //Пользователи
    let btn_account = $('#btn_account');
    btn_account.on('click', function() {
        $('#result_search').data('scroll_bool_status', '0')
        $('#btn_group').data("btn_group_value", "btn_account");
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<p>---Пользователи---</p><div id="result_account"></div>');
        view_accounts()
    });

    let filters_account_id_gender = $('#filters_account_id_gender');
    filters_account_id_gender.change(function (){
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<p>---Пользователи---</p><div id="result_account"></div>');
        view_accounts()
    })


    //Мастера
    let btn_master = $('#btn_master');
    btn_master.on('click', function() {
        $('#result_search').data('scroll_bool_status', '0')
        $('#btn_group').data("btn_group_value", "btn_master");
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<p>---Мастера---</p><div id="result_master"></div>');
        view_masters()
    });

    let filters_master_id_location = $('#filters_master_id_location');
    filters_master_id_location.change(function (){
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<p>---Мастера---</p><div id="result_master"></div>');
        view_masters()
    })


    //Посты
    let btn_post = $('#btn_post');
    btn_post.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_post");
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<p>---Посты---</p><div id="result_post"></div>');
        view_posts()
    });


    //Услуги
    let btn_service = $('#btn_service');
    btn_service.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_service");
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<p>---Услуги---</p><div id="result_service"></div>');
        view_service()
    });


    let filters_service_id_service_category = $('#filters_service_id_service_category');
    filters_service_id_service_category.change( function() {
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<p>---Услуги---</p><div id="result_service"></div>');
        view_service()
    });


    //Поле поиска
    let text_search = $('#text_search');
    text_search.keydown(function (e){   //собфтие нажатия интер на строке ввода
        if(e.keyCode ===13){
            if (($('#btn_group').data("btn_group_value")) == "btn_all"){
                view_all();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_account"){
                view_accounts();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_master"){
                view_masters();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_post"){
                view_posts();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_service"){
                view_service();
            }
        }
    })


    //Прокрутка

    $(window).scroll(function () {
        if ($("#result_search").data('scroll_bool_status') != '1'){
            if ((($(window).scrollTop() >= $(document).height() - $(window).height()))&&($(document).height() - $(window).height()!=0)) {

                if (($('#btn_group').data("btn_group_value")) == "btn_account"){
                    view_accounts();
                }
                else if (($('#btn_group').data("btn_group_value")) == "btn_master"){
                    view_masters();
                }
                else if (($('#btn_group').data("btn_group_value")) == "btn_post"){
                    view_posts();
                }
                else if (($('#btn_group').data("btn_group_value")) == "btn_service"){
                    view_service();

                }
                window_height = $(document).height() - $(window).height()
            }
        }
    })



})