"""
物流類型
"""
LogisticsType = {
    'CVS': 'CVS',  # 超商取貨
    'HOME': 'Home',  # 宅配
}

"""
物流子類型
"""
LogisticsSubType = {
    'TCAT': 'TCAT',  # 黑貓(宅配)
    'ECAN': 'ECAN',  # 宅配通
    'FAMILY': 'FAMI',  # 全家
    'UNIMART': 'UNIMART',  # 統一超商
    'HILIFE': 'HILIFE',  # 萊爾富
    'FAMILY_C2C': 'FAMIC2C',  # 全家店到店
    'UNIMART_C2C': 'UNIMARTC2C',  # 統一超商寄貨便
    'HILIFE_C2C': 'HILIFEC2C',  # 萊爾富富店到店
}

"""
是否代收貨款
"""
IsCollection = {
    'YES': 'Y',  # 貨到付款
    'NO': 'N',  # 僅配送
}

"""
使用設備
"""
Device = {
    'PC': 0,  # PC
    'MOBILE': 1,  # 行動裝置
}

"""
測試廠商編號
"""
ECPayTestMerchantID = {
    'B2C': '2000132',  # B2C
    'C2C': '2000933',  # C2C
}

"""
正式環境網址
"""
ECPayURL = {
    'CVS_MAP': 'https://logistics.ecpay.com.tw/Express/map',  # 電子地圖
    'SHIPPING_ORDER': 'https://logistics.ecpay.com.tw/Express/Create',  # 物流訂單建立
    'HOME_RETURN_ORDER': 'https://logistics.ecpay.com.tw/Express/ReturnHome',  # 宅配逆物流訂單
    # 超商取貨逆物流訂單(統一超商B2C)
    'UNIMART_RETURN_ORDER': 'https://logistics.ecpay.com.tw/express/ReturnUniMartCVS',
    # 超商取貨逆物流訂單(萊爾富超商B2C)
    'HILIFE_RETURN_ORDER': 'https://logistics.ecpay.com.tw/express/ReturnHiLifeCVS',
    # 超商取貨逆物流訂單(全家超商B2C)
    'FAMILY_RETURN_ORDER': 'https://logistics.ecpay.com.tw/express/ReturnCVS',
    # 全家逆物流核帳(全家超商B2C)
    'FAMILY_RETURN_CHECK': 'https://logistics.ecpay.com.tw/Helper/LogisticsCheckAccoounts',
    # 統一修改物流資訊(全家超商B2C)
    'UNIMART_UPDATE_LOGISTICS_INFO': 'https://logistics.ecpay.com.tw/Helper/UpdateShipmentInfo',
    # 更新門市(統一超商C2C)
    'UNIMART_UPDATE_STORE_INFO': 'https://logistics.ecpay.com.tw/Express/UpdateStoreInfo',
    # 取消訂單(統一超商C2C)
    'UNIMART_CANCEL_LOGISTICS_ORDER': 'https://logistics.ecpay.com.tw/Express/CancelC2COrder',
    'QUERY_LOGISTICS_INFO': 'https://logistics.ecpay.com.tw/Helper/QueryLogisticsTradeInfo/V2',  # 物流訂單查詢
    # 產生托運單(宅配)/一段標(超商取貨)
    'PRINT_TRADE_DOC': 'https://logistics.ecpay.com.tw/helper/printTradeDocument',
    # 列印繳款單(統一超商C2C)
    'PRINT_UNIMART_C2C_BILL': 'https://logistics.ecpay.com.tw/Express/PrintUniMartC2COrderInfo',
    # 全家列印小白單(全家超商C2C)
    'PRINT_FAMILY_C2C_BILL': 'https://logistics.ecpay.com.tw/Express/PrintFAMIC2COrderInfo',
    # 萊爾富列印小白單(萊爾富超商C2C)
    'Print_HILIFE_C2C_BILL': 'https://logistics.ecpay.com.tw/Express/PrintHILIFEC2COrderInfo',
    'CREATE_TEST_DATA': 'https://logistics.ecpay.com.tw/Express/CreateTestData',  # 產生 B2C 測標資料
}

"""
測試環境網址
"""
ECPayTestURL = {
    'CVS_MAP': 'https://logistics-stage.ecpay.com.tw/Express/map',  # 電子地圖
    'SHIPPING_ORDER': 'https://logistics-stage.ecpay.com.tw/Express/Create',  # 物流訂單建立
    'HOME_RETURN_ORDER': 'https://logistics-stage.ecpay.com.tw/Express/ReturnHome',  # 宅配逆物流訂單
    # 超商取貨逆物流訂單(統一超商B2C)
    'UNIMART_RETURN_ORDER': 'https://logistics-stage.ecpay.com.tw/express/ReturnUniMartCVS',
    # 超商取貨逆物流訂單(萊爾富超商B2C)
    'HILIFE_RETURN_ORDER': 'https://logistics-stage.ecpay.com.tw/express/ReturnHiLifeCVS',
    # 超商取貨逆物流訂單(全家超商B2C)
    'FAMILY_RETURN_ORDER': 'https://logistics-stage.ecpay.com.tw/express/ReturnCVS',
    # 全家逆物流核帳(全家超商B2C)
    'FAMILY_RETURN_CHECK': 'https://logistics-stage.ecpay.com.tw/Helper/LogisticsCheckAccoounts',
    # 統一修改物流資訊(全家超商B2C)
    'UNIMART_UPDATE_LOGISTICS_INFO': 'https://logistics-stage.ecpay.com.tw/Helper/UpdateShipmentInfo',
    # 更新門市(統一超商C2C)
    'UNIMART_UPDATE_STORE_INFO': 'https://logistics-stage.ecpay.com.tw/Express/UpdateStoreInfo',
    # 取消訂單(統一超商C2C)
    'UNIMART_CANCEL_LOGISTICS_ORDER': 'https://logistics-stage.ecpay.com.tw/Express/CancelC2COrder',
    'QUERY_LOGISTICS_INFO': 'https://logistics-stage.ecpay.com.tw/Helper/QueryLogisticsTradeInfo/V2',  # 物流訂單查詢
    # 產生托運單(宅配)/一段標(超商取貨)
    'PRINT_TRADE_DOC': 'https://logistics-stage.ecpay.com.tw/helper/printTradeDocument',
    # 列印繳款單(統一超商C2C)
    'PRINT_UNIMART_C2C_BILL': 'https://logistics-stage.ecpay.com.tw/Express/PrintUniMartC2COrderInfo',
    # 全家列印小白單(全家超商C2C)
    'PRINT_FAMILY_C2C_BILL': 'https://logistics-stage.ecpay.com.tw/Express/PrintFAMIC2COrderInfo',
    # 萊爾富列印小白單(萊爾富超商C2C)
    'PRINT_HILIFE_C2C_BILL': 'https://logistics-stage.ecpay.com.tw/Express/PrintHILIFEC2COrderInfo',
    'CREATE_TEST_DATA': 'https://logistics-stage.ecpay.com.tw/Express/CreateTestData',  # 產生 B2C 測標資料
}

"""
溫層
"""
Temperature = {
    'ROOM': '0001',  # 常溫
    'REFRIGERATION': '0002',  # 冷藏
    'FREEZE': '0003',  # 冷凍
}

"""
距離
"""
Distance = {
    'SAME': '00',  # 同縣市
    'OTHER': '01',  # 外縣市
    'ISLAND': '02',  # 離島
}

"""
規格
"""
Specification = {
    'CM_60': '0001',  # 60cm
    'CM_90': '0002',  # 90cm
    'CM_120': '0003',  # 120cm
    'CM_150': '0004',  # 150cm
}

"""
預計取件時段
"""
ScheduledPickupTime = {
    'TIME_9_12': '1',  # 9~12時
    'TIME_12_17': '2',  # 12~17時
    'TIME_17_20': '3',  # 17~20時
    'UNLIMITED': '4',  # 不限時
}

"""
預定送達時段
"""
ScheduledDeliveryTime = {
    'TIME_9_12': '1',  # 9~12時
    'TIME_12_17': '2',  # 12~17時
    'TIME_17_20': '3',  # 17~20時
    'UNLIMITED': '4',  # 不限時
    'TIME_20_21': '5',  # 20~21時(需限定區域)
    'TIME_9_17': '12',  # 早午 9~17
    'TIME_9_12_17_20': '13',  # 早晚 9~12 & 17~20
    'TIME_13_20': '23',  # 午晚 13~20
}

"""
門市類型
"""
StoreType = {
    'RECIVE_STORE': '01',  # 取件門市
    'RETURN_STORE': '02',  # 退件門市
}
