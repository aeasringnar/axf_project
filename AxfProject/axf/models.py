from django.db import models

# Create your models here.
# 首页轮播数据
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
# 首页导航数据
class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
# 首页小轮播
class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
# 首页便利店 块等数据
class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
# 主要信息
class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

# 分类模型
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    typesort = models.IntegerField()
    childtypenames = models.CharField(max_length=150)
# 商品模型类
class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=150)
    # 商品名称
    productname = models.CharField(max_length=50)
    # 商品长名称
    productlongname = models.CharField(max_length=100)
    # 是否精选
    isxf = models.NullBooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.CharField(max_length=10)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.CharField(max_length=10)
    # 超市价格
    marketprice = models.CharField(max_length=10)
    # 组id
    categoryid = models.CharField(max_length=10)
    # 子类组id
    childcid = models.CharField(max_length=10)
    # 子类组名称
    childcidname = models.CharField(max_length=10)
    # 详情页id
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销量
    productnum = models.IntegerField()
    # 购买者



# 简易用户模型
class userinfo(models.Model):
    # 用户账户 要唯一性
    useraccount = models.CharField(max_length=20,unique=True)
    # 密码
    upassword = models.CharField(max_length=300)
    # 昵称
    username = models.CharField(max_length=20)
    # 手机号
    userphone = models.CharField(max_length=20)
    #用户地址
    useradderss = models.CharField(max_length=200,null=False)  #这里的null=False就是默认使当前字段为空
# 这个是错误的
class cart(models.Model):
    userccount = models.CharField(max_length=20)
    usergoods = models.CharField(max_length=20)
# 购物车1.0版本
class NewCart(models.Model):
    nccount = models.CharField(max_length=20)
    ngoodsid = models.CharField(max_length=20)
# 购物车2.0版本
class TwoCart(models.Model):
    tccount = models.CharField(max_length=20)
    tgoodid = models.CharField(max_length=20)
    # 新增数量字段
    tgoodnum = models.IntegerField()
# 购物车3.0版本
class Xcart(models.Model):
    tccount = models.CharField(max_length=20)
    tgoodid = models.ForeignKey(Goods)
    # 新增数量字段
    tgoodnum = models.IntegerField()
