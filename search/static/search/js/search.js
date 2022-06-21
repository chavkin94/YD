function view_accounts(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 6;
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
        }
    })
}


function view_masters(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 6;
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
        }
    })
}

function view_posts(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 12;
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
        }
    })
}


function view_service(){
    let data = {};
    let text_search = $('#text_search').val();
    let count_elem = 12;
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
        }
    })
}

function removeClassUl(){
    $('#all').removeClass('show active');
    $('#masters').removeClass('show active');
    $('#post').removeClass('show active');
    $('#service').removeClass('show active');
    $('#people').removeClass('show active');
}

function view_all(){
    removeClassUl()
    $('#btn_group').data("btn_group_value", "btn_all");
    $("#result_search").html ('<div class="d-flex fs-5 btn-primary border mt-3"> <p class="m-2">Объявления</p><input class="btn btn-link" id="btn_all_service" type="submit" value="Показать все" onclick="btn_all_service()"></div>' +
    '<div id="result_service" class=""></div>'+
    '<div class="d-flex fs-5 btn-primary border mt-3"> <p class="m-2">Мастера</p> <input class="btn btn-link" id="btn_all_master" type="submit" value="Показать все" onclick="btn_all_master()"></div>' +
    '<div id="result_master" class=""></div>' +
    '<div class="d-flex fs-5 btn-primary border mt-3"> <p class="m-2">Публикации</p><input class="btn btn-link" id="btn_all_post" type="submit" value="Показать все" onclick="btn_all_post()"></div>' +
    '<div id="result_post" class=""></div>' +
    '<div class="d-flex fs-5 btn-primary border mt-3"> <p class="m-2">Пользователи</p> <input class="btn btn-link" id="btn_all_account" type="submit" value="Показать все" onclick="btn_all_account()"></div>' +
    '<div id="result_account" class=""></div>');
    $('#result_search').data("number_elem", '0')
    $('#result_search').data('scroll_bool_status', '0')
    view_accounts()
    view_masters()
    view_posts()
    view_service()
}

function btn_all_account(){
    removeClassUl()
    $('#result_search').data('scroll_bool_status', '0')
    $('#btn_group').data("btn_group_value", "btn_account");
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<div id="result_account"></div>');
    $('#btn_account').addClass('active');
    $('#people').addClass('show active');
    $('#btn_all').removeClass('active');
    view_accounts()
}

function btn_all_master(){
    removeClassUl()
    $('#result_search').data('scroll_bool_status', '0')
    $('#btn_group').data("btn_group_value", "btn_master");
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<div id="result_master"></div>');
    $('#btn_master').addClass('active');
    $('#masters').addClass('show active');
    $('#btn_all').removeClass('active');
    view_masters()
}

function btn_all_post(){
    removeClassUl()
    $('#btn_group').data("btn_group_value", "btn_post");
    $('#result_search').data('scroll_bool_status', '0')
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<div id="result_post"></div>');
    $('#btn_post').addClass('active');
    $('#post').addClass('show active');
    $('#btn_all').removeClass('active');
    view_posts()
}

function btn_all_service(){
    removeClassUl()
    $('#btn_group').data("btn_group_value", "btn_service");
    $('#result_search').data('scroll_bool_status', '0')
    $('#result_search').data("number_elem", '0')
    $("#result_search").html ('<div id="result_service"></div>');
    $('#btn_service').addClass('active');
    $('#service').addClass('show active');
    $('#btn_all').removeClass('active');
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
        $("#result_search").html ('<div id="result_account"></div>');
        view_accounts()
    });

    let filters_account_id_gender = $('#filters_account_id_gender');
    filters_account_id_gender.change(function (){
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<div id="result_account"></div>');
        view_accounts()
    })


    //Мастера
    let btn_master = $('#btn_master');
    btn_master.on('click', function() {
        $('#result_search').data('scroll_bool_status', '0')
        $('#btn_group').data("btn_group_value", "btn_master");
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<div id="result_master"></div>');
        view_masters()
    });

    let filters_master_id_location = $('#filters_master_id_location');
    filters_master_id_location.change(function (){
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<div id="result_master"></div>');
        view_masters()
    })


    //Посты
    let btn_post = $('#btn_post');
    btn_post.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_post");
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<div id="result_post"></div>');
        view_posts()
    });


    //Услуги
    let btn_service = $('#btn_service');
    btn_service.on('click', function() {
        $('#btn_group').data("btn_group_value", "btn_service");
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<div id="result_service"></div>');
        view_service()
    });


//    let filters_service_id_service_category = $('#filters_service_id_service_category');
    $('#filters_service_id_service_category').change( function() {
        $('#result_search').data('scroll_bool_status', '0')
        $('#result_search').data("number_elem", '0')
        $("#result_search").html ('<div id="result_service"></div>');
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
                btn_all_account();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_master"){
                btn_all_master();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_post"){
                btn_all_post();
            }
            else if (($('#btn_group').data("btn_group_value")) == "btn_service"){
                btn_all_service();
            }
        }
    })


    //Прокрутка


    var element = document.querySelector('#target');
    var visible_element = 0;
    $(window).scroll(function () {
        if (visible_element != 1 && target.getBoundingClientRect().top < window.pageYOffset){
            visible_element = 1;
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
        }
        if (target.getBoundingClientRect().top > window.pageYOffset)
        {
            visible_element = 0;
        }
//        if ($("#result_search").data('scroll_bool_status') != '1'){
//            if ((($(window).scrollTop() >= $(document).height() - $(window).height()))&&($(document).height() - $(window).height()!=0)) {
//
//                if (($('#btn_group').data("btn_group_value")) == "btn_account"){
//                    view_accounts();
//                }
//                else if (($('#btn_group').data("btn_group_value")) == "btn_master"){
//                    view_masters();
//                }
//                else if (($('#btn_group').data("btn_group_value")) == "btn_post"){
//                    view_posts();
//                }
//                else if (($('#btn_group').data("btn_group_value")) == "btn_service"){
//                    view_service();
//
//                }
//                window_height = $(document).height() - $(window).height()
//            }
//        }
    })



})