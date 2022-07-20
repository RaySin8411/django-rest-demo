from django.test import TestCase
from datetime import datetime

from .ecpay_sdk import ECPayPaymentSdk, ECPayLogisticSdk
from .ecpay_sdk.payment.enums import *
from .ecpay_sdk.logistic.enums import *


# Create your tests here.
def ecpay_payment_test():
    order_params = {
        'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
        'StoreID': '',
        'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'PaymentType': 'aio',
        'TotalAmount': 2000,  # 商品金額
        'TradeDesc': '訂單測試',  # 商品描述
        'ItemName': '商品1#商品2',  # 商品名稱，用井字號當分行
        'ReturnURL': 'https://www.ecpay.com.tw/return_url.php',  # 顧客填完付款資料後的跳轉頁面
        'ChoosePayment': ChoosePayment['ALL'],  # 顧客的付費方式

        # 結帳後，先導到 OrderResultURL，從綠界頁面跳回的頁面
        # 如果沒有參數才會跳轉到 ClientBackURL
        'ClientBackURL': 'https://www.ecpay.com.tw/client_back_url.php',
        'ItemURL': 'https://www.ecpay.com.tw/item_url.php',  # 商品資訊頁面
        'Remark': '交易備註',  # 備註文字
        'ChooseSubPayment': '',

        # 結帳成功/失敗後的結果頁面，告知顧客本次的結帳結果
        'OrderResultURL': 'https://www.ecpay.com.tw/order_result_url.php',
        'NeedExtraPaidInfo': 'Y',
        'DeviceSource': '',
        'IgnorePayment': '',
        'PlatformID': '',
        'InvoiceMark': 'N',
        'CustomField1': '',
        'CustomField2': '',
        'CustomField3': '',
        'CustomField4': '',
        'EncryptType': 1,
    }

    extend_params_1 = {
        'ExpireDate': 7,  # 商品上架期限
        'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',  # 付款資訊頁面
        'ClientRedirectURL': '',  # 看完付款資訊，要重導到哪裡
    }

    extend_params_2 = {
        'StoreExpireDate': 15,
        'Desc_1': '',
        'Desc_2': '',
        'Desc_3': '',
        'Desc_4': '',
        'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
        'ClientRedirectURL': '',
    }

    extend_params_3 = {
        'BindingCard': 0,
        'MerchantMemberID': '',
    }

    extend_params_4 = {
        'Redeem': 'N',
        'UnionPay': 0,
    }

    # 發票資訊
    inv_params = {
        # 'RelateNumber': 'Tea0001', # 特店自訂編號
        # 'CustomerID': 'TEA_0000001', # 客戶編號
        # 'CustomerIdentifier': '53348111', # 統一編號
        # 'CustomerName': '客戶名稱',
        # 'CustomerAddr': '客戶地址',
        # 'CustomerPhone': '0912345678', # 客戶手機號碼
        # 'CustomerEmail': 'abc@ecpay.com.tw',
        # 'ClearanceMark': '2', # 通關方式
        # 'TaxType': '1', # 課稅類別
        # 'CarruerType': '', # 載具類別
        # 'CarruerNum': '', # 載具編號
        # 'Donation': '1', # 捐贈註記
        # 'LoveCode': '168001', # 捐贈碼
        # 'Print': '1',
        # 'InvoiceItemName': '測試商品1|測試商品2',
        # 'InvoiceItemCount': '2|3',
        # 'InvoiceItemWord': '個|包',
        # 'InvoiceItemPrice': '35|10',
        # 'InvoiceItemTaxType': '1|1',
        # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
        # 'DelayDay': '0', # 延遲天數
        # 'InvType': '07', # 字軌類別
    }

    # 建立實體
    ecpay_payment_sdk = ECPayPaymentSdk(
        # 參考綠界後台->系統開發管理->系統界接設定，開發時有測試用的 商店ID
        MerchantID='2000132',

        # 參考綠界後台->系統開發管理->系統界接設定，開發時有測試用的 HashKey
        HashKey='5294y06JbISpM5x9',

        # 參考綠界後台->系統開發管理->系統界接設定，開發時有測試用的 HashIV
        HashIV='v77hoKGq4kWxNNIS'
    )

    # 合併延伸參數
    order_params.update(extend_params_1)
    order_params.update(extend_params_2)
    order_params.update(extend_params_3)
    order_params.update(extend_params_4)

    # 合併發票參數
    order_params.update(inv_params)

    try:
        # 產生綠界訂單所需參數
        final_order_params = ecpay_payment_sdk.create_order(order_params)

        # 產生 html 的 form 格式
        action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'  # 測試環境
        # action_url = 'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5' # 正式環境
        html = ecpay_payment_sdk.gen_html_post_form(action_url, final_order_params)

        # 最後產出 html，回傳回去顯示此 html
        return html
    except Exception as error:
        print('An exception happened: ' + str(error))


def ecpay_logistic_test():
    import pprint
    from datetime import datetime

    create_shipping_order_params = {
        'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
        'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'LogisticsType': LogisticsType['CVS'],
        'LogisticsSubType': LogisticsSubType['UNIMART_C2C'],
        'GoodsAmount': 1500,
        'CollectionAmount': 1500,
        'IsCollection': IsCollection['YES'],
        'GoodsName': '測試商品',
        'SenderName': '測試寄件者',
        'SenderPhone': '0226550115',
        'SenderCellPhone': '0911222333',
        'ReceiverName': '測試收件者',
        'ReceiverPhone': '0226550115',
        'ReceiverCellPhone': '0933222111',
        'ReceiverEmail': 'test@gmail.com',
        'TradeDesc': '測試交易敘述',
        'ServerReplyURL': 'https://www.ecpay.com.tw/server_reply_url',
        'ClientReplyURL': '',
        'Remark': '測試備註',
        'PlatformID': '',
        'LogisticsC2CReplyURL': 'https://www.ecpay.com.tw/logistics_c2c_reply',
    }

    shipping_cvs_params = {
        'ReceiverStoreID': '991182',
        'ReturnStoreID': '991182',
    }

    # 更新及合併參數
    create_shipping_order_params.update(shipping_cvs_params)

    # 建立實體
    ecpay_logistic_sdk = ECPayLogisticSdk(
        MerchantID='2000933',
        HashKey='XBERn1YOvpM9nfZc',
        HashIV='h1ONHk4P4yqbl5LK'
    )

    try:
        # 介接路徑
        action_url = 'https://logistics-stage.ecpay.com.tw/Express/Create'  # 測試環境
        # action_url = 'https://logistics.ecpay.com.tw/Express/Create' # 正式環境

        # 建立物流訂單並接收回應訊息
        reply_result = ecpay_logistic_sdk.create_shipping_order(
            action_url=action_url,
            client_parameters=create_shipping_order_params)
        return reply_result

    except Exception as error:
        print('An exception happened: ' + str(error))
