window.onload = maskload;

function maskload() {
    const inputElement = document.getElementById('phone') // ищем наш единственный input
    const maskOptions = { // создаем объект параметров
      mask: '+{7}(000)000-00-00' // задаем единственный параметр mask
    }
    IMask(inputElement, maskOptions) // запускаем плагин с переданными параметрами
}

$(function() {
    let header = $('header');
    let section = $('section');

    $(window).scroll(function() {
        if($(this).scrollTop() > 150) {
            header.addClass('header_fixed');
            header.removeClass('m-4');
            section.addClass('body_padding')
        } else {
            header.removeClass('header_fixed');
            header.addClass('m-4');
            section.removeClass('body_padding');
        }
    });
});