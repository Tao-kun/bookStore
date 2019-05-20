from django.shortcuts import render, redirect
import watch_buy.models as watch_buy_models
import login_manage.models as login_manage_models
# Create your views here.


# 显示商品列表
def catalog_grid(request):
    if not request.session.get('studentID'):
        request.session.flush()
        return redirect('/login/')
    rtn_list = watch_buy_models.Goods.objects.all()
    rtn_pic = []
    for i in range(len(rtn_list)):
        GoodID = rtn_list[i].GoodISBN
        pic_tmp = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=GoodID)
        rtn_pic.append(pic_tmp[0])
    rtn_dic = dict(map(lambda x, y: [x, y], rtn_pic, rtn_list))
    return render(request, "watch_buy/catalog_grid.html", locals())


# 结账
def checkout(request):
    if not request.session.get('studentID'):
        request.session.flush()
        return redirect('/login/')
    good_name = request.GET.get("good_name")
    good_price = request.GET.get("good_price")
    return render(request, "watch_buy/checkout.html", locals())


# 查看购物车
def shopping_cart(request):
    if not request.session.get('studentID'):
        request.session.flush()
        return redirect('/login/')
    good_num_list = watch_buy_models.Cart.objects.all()
    class rtn:
        def __init__(self, pic, info, qty):
            self.pic = pic
            self.info = info
            self.qty = qty
    rtn_list = []
    studentID = request.session.get('studentID')
    for i in range(len(good_num_list)):
        GoodID = good_num_list[i].GoodID_id
        pic_tmp = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=GoodID)
        info_tmp = watch_buy_models.Goods.objects.get(GoodISBN=GoodID)
        Qty_tmp = watch_buy_models.Cart.objects.get(GoodID_id=GoodID, studentID_id=studentID)
        re = rtn(pic_tmp[0], info_tmp, Qty_tmp.Qty)
        rtn_list.append(re)
        #print(Qty_tmp)
    return render(request, "watch_buy/shopping_cart.html", locals())


# 加入购物车
def add_to_cart(request):
    good_name = request.GET.get("good_name")
    good_price = request.GET.get("good_price")
    good_pic = request.GET.get("good_pic")
    good_ISBN = watch_buy_models.Goods.objects.get(GoodName=good_name).GoodISBN
    studentID = request.session.get('studentID')
    new_good = watch_buy_models.Goods.objects.get(GoodISBN=good_ISBN)
    new_stu = login_manage_models.User.objects.get(studentID=studentID)
    flag = watch_buy_models.Cart.objects.get(GoodID_id=good_ISBN, studentID_id=studentID)
    if not flag:
        new_cart = watch_buy_models.Cart()
        new_cart.GoodID = new_good
        new_cart.studentID = new_stu
        new_cart.save()
    else:
        new_cart = flag
        new_cart.Qty = new_cart.Qty + 1
        new_cart.save()
    return render(request, "watch_buy/add_to_cart.html", locals())


# 查看商品详细信息
def good_detail(request):
    Good_ISBN = request.GET.get('ISBN')
    Good = watch_buy_models.Goods.objects.get(GoodISBN=Good_ISBN)
    Good_pic_list = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=Good_ISBN)
    return render(request, "watch_buy/product_page.html", locals())
