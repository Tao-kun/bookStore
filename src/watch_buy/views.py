from django.shortcuts import render
import watch_buy.models as watch_buy_models
import login_manage.models as login_manage_models
# Create your views here.


def catalog_grid(request):
    rtn1 = watch_buy_models.Goods.objects.all()
    ISBN = rtn1[0].GoodISBN
    Price = rtn1[0].GoodPrice
    Name = rtn1[0].GoodName
    rtn2 = watch_buy_models.GoodsPic.objects.filter(GoodISBN=ISBN)
    src = rtn2[0].GoodPic
    srcc = src.url
    print(src.url)
    return render(request, "watch_buy/catalog_grid.html", locals())


def checkout(request):
    good_name = request.GET.get("good_name")
    good_price = request.GET.get("good_price")
    return render(request, "watch_buy/checkout.html", locals())


def shopping_cart(request):
    good_num_list = watch_buy_models.Cart.objects.all()
    pic_list = []
    good_info_list = []
    studentID = request.session.get('studentID')
    for i in range(len(good_num_list)):
        GoodID = good_num_list[i].GoodID_id
        pic_tmp = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=GoodID)
        pic_list.append(pic_tmp[0])
        info_tmp = watch_buy_models.Goods.objects.get(GoodISBN=GoodID)
        good_info_list.append(info_tmp)
    dic = dict(map(lambda x, y: [x, y], pic_list, good_info_list))
    # print(dic)
    return render(request, "watch_buy/shopping_cart.html", locals())


def add_to_cart(request):
    good_name = request.GET.get("good_name")
    good_price = request.GET.get("good_price")
    good_pic = request.GET.get("good_pic")
    good_ISBN = watch_buy_models.Goods.objects.get(GoodName=good_name).GoodISBN
    studentID = request.session.get('studentID')
    new_good = watch_buy_models.Goods.objects.get(GoodISBN=good_ISBN)
    new_stu = login_manage_models.User.objects.get(studentID=studentID)
    new_cart = watch_buy_models.Cart()
    new_cart.GoodID = new_good
    new_cart.studentID = new_stu
    new_cart.save()
    return render(request, "watch_buy/add_to_cart.html", locals())
