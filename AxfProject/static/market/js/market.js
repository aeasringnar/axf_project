$(function () {

    $('.mtopleft').click(function () {
        $('.goodtype').css('display', 'block');
        $('.goodsorder').hide();
    })

    $('.goodtype').click(function () {
        $(this).hide();
    })

    $('.mtopright').click(function () {
        $('.goodsorder').show();
        $('.goodtype').hide();
    })

    $('.goodsorder').click(function () {
        $(this).hide();
    })
    $('.mycart').click(function () {
        need = $(this).addClass('needgold');
        //终于获取到this下的span 里面的内容
        var goodid = $(this).children('span').html();
        var url = 'http://127.0.0.1:8000/axf/dellcart';
        $.get(url, {'goodid': goodid}, function (result) {
            // $('#span01').html(uresult.status);
            // console.log(result.status);
            if (result.status == 'error') {
                // console.log(result.status);
                alert('好像还没登录哦，请登录后重试！');
            }
        })
        setTimeout(function () {
            need.removeClass('needgold');
        },100);
    })
})
