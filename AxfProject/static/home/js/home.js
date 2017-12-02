$(function () {
    initSwiperEheel();
    swipermenu2();
});

function initSwiperEheel() {
    var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        autoplay : 1000,
        autoplayDisableOnInteraction : false,  //这里设置了False的话当我们点击或自行滑动之后仍然可以自定播放
    });
}

function swipermenu2() {
     var swiper = new Swiper('.swiper-myswiper', {
        slidesPerView: 3,   //设置每页轮播显示的数量
        spaceBetween: 5,    //设置每个图片之间的距离
    });
}
