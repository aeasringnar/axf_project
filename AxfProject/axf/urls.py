from django.conf.urls import url
from axf import views

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^market/',views.market,name='market'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^cart/',views.cart,name='cart'),
    # 传递参数的方式
    url(r'^marketname/(\d+)/(\d+)/(\d+)',views.marketCategory,name='marketCategory'),
    url(r'^login/',views.login,name='login'),
    url(r'^dologin/',views.dologin,name='dologin'),
    url(r'^register/',views.register,name='register'),
    url(r'^doregister/',views.doregister,name='doregister'),
    url(r'^checkuser/',views.checkuser,name='checkuser'),
    url(r'^checklogin/',views.checklogin,name='checklogin'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^dellcart/',views.dellcart,name='dellcart'),
    url(r'^goodadd/(\d+)',views.goodadd,name='goodadd'),
    url(r'^goodsub/(\d+)',views.goodsub,name='goodsub'),
    url(r'^register_two',views.register_two,name='register_two'),
    url(r'^doregister_two/',views.doregister_tow,name='doregister_two'),
    url(r'^checkuser_two/',views.checkuser_two,name='checkuser_two'),
    url(r'^cart02/', views.cart02, name='cart02'),
    url(r'^delgoods/',views.delgoods,name='delgoods'),
]