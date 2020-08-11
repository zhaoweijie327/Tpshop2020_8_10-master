from selenium.webdriver.common.by import By


class FindElement:

    #_________________首页
    # 首页登陆元素
    home_page_login = (By.CSS_SELECTOR,'.red')
    # 首页搜索框元素
    home_page_searchbox = (By.CSS_SELECTOR,'[placeholder="请输入搜索关键字..."]')
    # 首页搜索按钮元素
    home_page_search = (By.CSS_SELECTOR,'.ecsc-search-button')
    # 购物车元素
    home_page_card = (By.CSS_SELECTOR, '.c-n span')
    # 首页我的订单元素
    home_page_order = (By.LINK_TEXT,'我的订单')
    #_________________登陆页面
    # 用户框元素
    login_page_user = (By.CSS_SELECTOR,'#username')
    # 密码框元素
    login_page_pwd = (By.CSS_SELECTOR,'#password')
    # 验证码框元素
    login_page_code = (By.CSS_SELECTOR,'#verify_code')
    # 登陆按钮元素
    login_page_submit = (By.CSS_SELECTOR,'.J-login-submit')
    # _________________商品页面
    # 商品名连接元素
    commodity_page_goods = (By.PARTIAL_LINK_TEXT,'小米9')
    # 添加购物车按钮元素
    commodity_page_addcard = (By.CSS_SELECTOR,'#join_cart')
    # 子页面元素
    commodity_page_ifram = (By.CSS_SELECTOR,'.layui-layer-content iframe')
    # "添加成功文本元素"
    commodity_page_text = (By.CSS_SELECTOR,'.conect-title span')
    # X号元素
    commodity_page_X = (By.CSS_SELECTOR,'.layui-layer-setwin')
    # 购物车元素
    commodity_page_card = (By.CSS_SELECTOR,'.c-n span')
    # 获取购物车文本信息
    commodity_page_rice = (By.CSS_SELECTOR,'.goods-name')
    # _________________购物车页面
    # 去结算按钮元素
    shopping_page_card = (By.CSS_SELECTOR,'.gwc-qjs')
    # 提交订单按钮元素
    shopping_page_place_order = (By.CSS_SELECTOR,'.Sub-orders')
    # 提交成功后文本信息
    shopping_page_text = (By.CSS_SELECTOR,'.erhuh h3')
    # _________________我的订单页面
    # 待支付元素
    myorder_page_payment = (By.LINK_TEXT,'待付款')
    # 立即付款元素
    myorder_page_immediately = (By.XPATH,'//*[@class="paysoon"]/a[1]')
    # 货到付款元素
    myorder_page_cod = (By.CSS_SELECTOR,'[src="/plugins/payment/cod/logo.jpg"]')
    # 点击确认付款元素
    myorder_page_confirm = (By.CSS_SELECTOR,'.button-confirm-payment')
    # 获取支付成功文本元素
    myorder_page_success = (By.CSS_SELECTOR,'.erhuh h3')