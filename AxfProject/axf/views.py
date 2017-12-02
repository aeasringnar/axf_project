from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodTypes, Goods, userinfo, NewCart, TwoCart, Xcart
# 导入密码加密模块
import hashlib

# 打开主页
def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shop = Shop.objects.all()
    shop1 = shop[0]
    shop2 = shop[1:3]
    shop3 = shop[3:7]
    shop4 = shop[7:11]
    maininfos = MainShow.objects.all()
    # print(maininfos)
    context = {'pageTitle':'主页','wheels':wheels,'musbuys':mustbuys,
               'navs':navs,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,
               'maininfos':maininfos,
               }

    return render(request,'axf/Home.html',context)

# 因为在基础模板中使用里一种方法 因此这个方法已经失效了
def market(request):
    # 获取所有商品类型
    typenames = FoodTypes.objects.all()
    # 获取刚开始进入时显示的数据
    goodlist = Goods.objects.all().filter(categoryid=104749)
    context = {'pagetitle':'闪送','typenames':typenames,'goodlist':goodlist,}
    # return render(request,'axf/Market.html',context)
    return HttpResponseRedirect(reverse('axf:marketCategory')) #重定向

def marketCategory(request,foodtype,childcid,ordering):
    # 获取所有商品类型
    typenames = FoodTypes.objects.all()
    if ordering =='0':
        orderRule ='id'
    elif ordering =='1':
        orderRule = 'price'
    elif ordering =='2':
        orderRule = '-price'
    elif ordering =='3':
        orderRule = 'storenums'
    else:
        orderRule = 'id'
    if childcid =='0':
        goodlist = Goods.objects.all().filter(categoryid=foodtype).order_by(orderRule)
    else:
        goodlist = Goods.objects.all().filter(categoryid=foodtype).filter(childcid=childcid).order_by(orderRule)
    # 获取显示的数据
    foodtype = int(foodtype)
    # 获取分类的名字
    type = FoodTypes.objects.filter(typeid=foodtype).first()
    # 测试获取数据
    # print(type.childtypenames)
    typename = type.childtypenames
    childtypeandnames = typename.split('#')
    items = []
    for child in childtypeandnames:
    #     分割列表中的每一项 并放在字典里 然后在存在列表里
        childs = child.split(':')
        item = {'childName':childs[0],'childTypeId':childs[1]}
        items.append(item)
        # print(item)
    context = {'pagetitle':'闪送','typenames': typenames, 'goodlist': goodlist,
               'items':items,'foodtypeid':foodtype,'orderRule':ordering,'childcid':childcid}
    return render(request, 'axf/Market.html', context)
# 个人中心
def mine(request):
    try:
        username = request.session.get('username','未登录')
    except KeyError:
        pass
    context = {'pagetitle':'我的','username':username}
    return render(request,'axf/Mine.html',context)

# 点击登录时跳转
def login(request):
    return render(request,'axf/Login.html')
# 执行登录操作
def dologin(request):
    uccount = request.POST.get('useraccount')
    upawd = request.POST.get('upassword')
    if userinfo.objects.all().filter(useraccount=uccount).first():
        print('得到数据')
        user = userinfo.objects.all().filter(useraccount=uccount).first()
        # if user.upassword ==upawd:
    else:
        print('没有得到数据')
    request.session['uccount'] = uccount
    response = HttpResponseRedirect(reverse('axf:mine'))
    return response

# 点击注册时跳转
def register(request):
    return render(request,'axf/Register.html')
# 执行注册,就是保存注册的内容
def doregister(request):
    uccount = request.POST.get('useraccount')
    upawd = request.POST.get('upassword')
    uname = request.POST.get('username')
    uphone = request.POST.get('userphone')
    user = userinfo()
    user.useraccount = uccount
    user.upassword = upawd
    user.username = uname
    user.userphone = uphone
    user.save()
    response = HttpResponseRedirect(reverse('axf:register'))
    return response
# 购物车 并判断是否有账号登录
def cart(request):
    username = request.session.get('username',)
    myuserccount = request.session.get('uccount',)
    if not username:
        # print('没有获取到session数据')
        return render(request, 'axf/qregister.html')
    else:
        # print(username)
        # print(myuserccount)
        # ##########################在这里要准备进行购物车的操作
        # ugoodobjs = NewCart.objects.all().filter(nccount=myuserccount)
        # 购物车2.0
        # ugoodobjs = TwoCart.objects.all().filter(tccount=myuserccount)
        # ugoodsidlist = []
        # ugoodnumdic = {}
        # for ugoodobj in ugoodobjs:
        #     # 获得id
        #     myugoodid = ugoodobj.tgoodid
        #     myugoodobj = Goods.objects.all().filter(id=myugoodid).first()
        #     myugoodnumobj = TwoCart.objects.all().filter(tgoodid=myugoodid).first()
        #     # 获得对应数量
        #     myugoodnum = myugoodnumobj.tgoodnum
        #     ugoodnumdic[myugoodid] = myugoodnum
        #     # ugoodnumlist.append(myugoodnum)
        #     ugoodsidlist.append(myugoodobj)
        # print(ugoodsidlist)  #得到所有的用户添加的商品，但是其中有重复的，需要考虑解决方案
        # print(ugoodnumdic)
        # context = {'ugoods':ugoodsidlist,'ugoodnum':ugoodnumdic}
        # 购物车3.0
        ugoodobjs = Xcart.objects.all().filter(tccount=myuserccount)
        context = {'ugoods': ugoodobjs}
        return render(request,'axf/cart02.html',context)

# 检查用户名是否可注册，这里是一个异步请求时发生的函数
# 当失去焦点时就进行一个异步请求，请求数据是否合理
def checkuser(request):
    precheck = request.GET.get('useraccount')
    print(precheck)
    prechecknum = userinfo.objects.all().filter(useraccount=precheck).first()
    print(prechecknum)
    if not prechecknum:
        context = {'status': '用户名可用'}
        print(context)
    else:
        context = {'status': '用户名已经存在'}
        print('不可以注册，用户名存在')
    return JsonResponse(context)
#检查登录
def checklogin(request):
    checkuaccount = request.GET.get('useraccount')
    checkupawd = request.GET.get('upassword')
    checknum = userinfo.objects.all().filter(useraccount=checkuaccount).first()
    if checknum:
        userobj = userinfo.objects.all().filter(useraccount=checkuaccount).first()
        # print(userobj.upassword)
        # 1.创建一个hash对象
        h = hashlib.sha256()
        # 2.填充要加密的数据
        h.update(bytes(checkupawd, encoding='utf-8'))
        # 3.获取加密结果
        checkresult = h.hexdigest()
        if userobj.upassword == str(checkupawd) or userobj.upassword == str(checkresult):
            # 这个时候应该弹出一个框 登录成功然后跳转到个人中心
            # 也要设置cookie或者session
            username = userobj.username
            uccount = userobj.useraccount
            # 获取用户账号并为购物车存储一个关键session
            request.session['uccount'] = uccount
            request.session['username'] = username
            context = {'status':''}
        else:
            context = {'status': '用户密码错误'}
    else:
        # print('not')
        context = {'status': '用户名不存在'}
    return JsonResponse(context)

#检查购物车，这一步是在添加购物车的时候进行的操作，进行了Ajax请求
def dellcart(request):
    # 已经获取到了用户 和添加的 商品id
    goodid = request.GET.get('goodid')
    uccount = request.session.get('uccount')
    # print(uccount)
    if not uccount:
        # print(uccount)
        # 检查是否登录，没登录时会提示登录
        mycontext = {'status': 'error'}
    else:
        # print(goodid, uccount)
        goodid = str(goodid)
        uccount = str(uccount)
        # 存储购物车 1.0版本
        # newcart = NewCart()
        # newcart.nccount = uccount
        # newcart.ngoodsid = goodid
        # newcart.save()
        # 存储购物车2.0版本
        # twocart = TwoCart()
        # checkgood = TwoCart.objects.all().filter(tccount=uccount).filter(tgoodid=goodid).first()
        # 购物车3.0版本
        twocart = Xcart()
        checkgood = Xcart.objects.all().filter(tccount=uccount).filter(tgoodid__id=goodid).first()
        if not checkgood:
            goodobj = Goods.objects.all().filter(id=goodid).first()
            # print(checkgood)
            twocart.tccount = uccount
            twocart.tgoodid = goodobj
            twocart.tgoodnum = 1
            twocart.save()
        else:
            # print('第二次你才会看到我')
            checkgood.tgoodnum += 1
            checkgood.save()
        mycontext = {'status': 'ok'}
    return JsonResponse(mycontext)

# 退出按钮
def logout(request):
    try:
        del request.session['username']
        del request.session['uccount']
    except KeyError:
        pass
    return render(request,'axf/logout.html')

# 购买数量加一
def goodadd(request,goodid):
    uccount = request.session.get('uccount')
    goodaddobj = Xcart.objects.all().filter(tgoodid__id=goodid).filter(tccount=uccount).first()
    goodaddobj.tgoodnum += 1
    goodaddobj.save()
    return HttpResponseRedirect(reverse('axf:cart'))

# 购买数量减一
def goodsub(request,goodid):
    uccount = request.session.get('uccount')
    goodaddobj = Xcart.objects.all().filter(tgoodid__id=goodid).filter(tccount=uccount).first()
    if goodaddobj.tgoodnum <= 1:
        pass
    else:
        goodaddobj.tgoodnum -= 1
        goodaddobj.save()
    return HttpResponseRedirect(reverse('axf:cart'))

# 用户注册2.0版本
def register_two(request):
    return render(request,'axf/Register-two.html')

def doregister_tow(request):
    uccount = request.POST.get('useraccount')
    upawd = request.POST.get('upassword')
    uname = request.POST.get('username')
    uphone = request.POST.get('userphone')
    h = hashlib.sha256()
    h.update(bytes(upawd,encoding='utf-8'))
    pawdresult = h.hexdigest()
    user = userinfo()
    user.useraccount = uccount
    user.upassword = pawdresult
    user.username = uname
    user.userphone = uphone
    user.save()
    response = HttpResponseRedirect(reverse('axf:login'))
    return response

def checkuser_two(request):
    precheck = request.GET.get('useraccount')
    print(precheck)
    prechecknum = userinfo.objects.all().filter(useraccount=precheck).first()
    print(prechecknum)
    if not prechecknum:
        context = {'status': '用户名可用'}
        print(context)
    else:
        context = {'status': '用户名已经存在'}
        print('不可以注册，用户名存在')
    return JsonResponse(context)

#购物车版本2.0
def cart02(request):
    username = request.session.get('username', )
    myuserccount = request.session.get('uccount', )
    if not username:
        # print('没有获取到session数据')
        return render(request, 'axf/qregister.html')
    else:
        ugoodobjs = Xcart.objects.all().filter(tccount=myuserccount)
        context = {'ugoods': ugoodobjs}
    return render(request,'axf/cart02.html',context)

# 用来删除商品的接口
@csrf_exempt
def delgoods(request):
    arr = request.POST.getlist('ids')
    for i in arr:
        needid = int(i)
        needgood = Xcart.objects.all().filter(id=needid).first()
        # print(needgood)
        needgood.delete()
    return HttpResponseRedirect(reverse('axf:cart'))