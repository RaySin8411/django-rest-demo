"""
付款方式
"""
ChoosePayment = {
    'Credit': 'Credit',  # 信用卡及 GooglePay
    'GooglePay': 'GooglePay',  # GooglePay (若為PC版時不支援)
    'WebATM': 'WebATM',  # 網路 ATM (若為手機版時不支援)
    'ATM': 'ATM',  # 自動櫃員機
    'CVS': 'CVS',  # 超商代碼
    'BARCODE': 'BARCODE',  # 超商條碼 (若為手機版時不支援)
    'ApplePay': 'ApplePay',  # ApplePay (僅支援Safari瀏覽器)
    'ALL': 'ALL',  # 不指定付款方式，由綠界顯示付款方式選擇頁面。
}

"""
付款方式子項目
"""
ChooseSubPayment = {
    'WebATM': {
        'TAISHIN': 'TAISHIN',  # 台新銀行
        'ESUN': 'ESUN',  # 玉山銀行
        'BOT': 'BOT',  # 台灣銀行
        'FUBON': 'FUBON',  # 台北富邦
        'CHINATRUST': 'CHINATRUST',  # 中國信託
        'FIRST': 'FIRST',  # 第一銀行
        'CATHAY': 'CATHAY',  # 國泰世華
        'MEGA': 'MEGA',  # 兆豐銀行
        'LAND': 'LAND',  # 土地銀行
        'TACHONG': 'TACHONG',  # 大眾銀行
        'SINOPAC': 'SINOPAC',  # 永豐銀行
    },
    'ATM': {
        'TAISHIN': 'TAISHIN',  # 台新銀行
        'ESUN': 'ESUN',  # 玉山銀行
        'BOT': 'BOT',  # 台灣銀行
        'FUBON': 'FUBON',  # 台北富邦
        'CHINATRUST': 'CHINATRUST',  # 中國信託
        'FIRST': 'FIRST',  # 第一銀行
        'LAND': 'LAND',  # 土地銀行
        'CATHAY': 'CATHAY',  # 國泰世華銀行
        'TACHONG': 'TACHONG',  # 大眾銀行
    },
    'CVS': {
        'CVS': 'CVS',  # 超商代碼繳款
        'OK': 'OK',  # OK 超商代碼繳款
        'FAMILY': 'FAMILY',  # 全家超商代碼繳款
        'HILIFE': 'HILIFE',  # 萊爾富超商代碼繳款
        'IBON': 'IBON',  # 7-11 ibon 代碼繳款
    },
    'BARCODE': 'BARCODE',  # 超商條碼繳款
    'Credit': 'Credit',  # 信用卡 (MasterCard/JCB/VISA)
    'GooglePay': 'GooglePay',  # GooglePay
    'ApplePay': '',  # ApplePay
}

"""
回覆付款方式
"""
ReplyPaymentType = {
    'WebATM_TAISHIN': '台新銀行 WebATM',
    'WebATM_ESUN': '玉山銀行 WebATM',
    'WebATM_BOT': '台灣銀行 WebATM',
    'WebATM_FUBON': '台北富邦 WebATM',
    'WebATM_CHINATRUST': '中國信託 WebATM',
    'WebATM_FIRST': '第一銀行 WebATM',
    'WebATM_CATHAY': '國泰世華 WebATM',
    'WebATM_MEGA': '兆豐銀行 WebATM',
    'WebATM_LAND': '土地銀行 WebATM',
    'WebATM_TACHONG': '元大銀行 WebATM',
    'WebATM_SINOPAC': '永豐銀行 WebATM',
    'ATM_TAISHIN': '台新銀行 ATM',
    'ATM_ESUN': '玉山銀行 ATM',
    'ATM_BOT': '台灣銀行 ATM',
    'ATM_FUBON': '台北富邦 ATM',
    'ATM_CHINATRUST': '中國信託 ATM',
    'ATM_FIRST': '第一銀行 ATM',
    'ATM_LAND': '土地銀行 ATM',
    'ATM_CATHAY': '國泰世華銀行 ATM',
    'ATM_TACHONG': '元大銀行 ATM',
    'CVS_CVS': '超商代碼繳款',
    'CVS_OK': 'OK 超商代碼繳款',
    'CVS_FAMILY': '全家超商代碼繳款',
    'CVS_HILIFE': '萊爾富超商代碼繳款',
    'CVS_IBON': '7-11 ibon 代碼繳款',
    'BARCODE_BARCODE': '超商條碼繳款',
    'Credit_CreditCard': '信用卡',
    'GooglePay': 'GooglePay',
    'ApplePay': 'ApplePay',
}

"""
額外付款資訊
"""
NeedExtraPaidInfo = {
    'Yes': 'Y',  # 需要額外付款資訊
    'No': 'N',  # 不需要額外付款資訊
}

"""
裝置來源
"""
DeviceSource = ""  # 請帶空值，由系統自動判定。

"""
信用卡關帳/退刷/取消/放棄
"""
Action = {
    'C': 'C',  # 關帳
    'R': 'R',  # 退刷
    'E': 'E',  # 取消
    'N': 'N',  # 放棄
}

"""
定期定額的週期種類
"""
PeriodType = {
    'Y': 'Y',  # 以年為週期
    'M': 'M',  # 以月為週期
    'D': 'D',  # 以天為週期
}

"""
電子發票開立註記
"""
InvoiceMark = 'Y'  # 需要開立電子發票

"""
電子發票載具類別
"""
CarruerType = {
    'None': '',  # 無載具
    'Member': '1',  # 特店載具
    'Citizen': '2',  # 買受人自然人憑證
    'Cellphone': '3',  # 買受人手機條碼
}

"""
電子發票捐贈註記
"""
Donation = {
    'No': '2',  # 若為不捐贈或統一編號 [CustomerIdentifier] 有值時, 不捐贈
    'Yes': '1',  # 捐贈
}

"""
電子發票列印註記
"""
Print = {
    'No': '0',  # 若為不列印或捐贈註記 [Donation] 為 1 (捐贈) 時, 不列印
    'Yes': '1',  # 若為列印或統一編號 [CustomerIdentifier] 有值時, 列印
}

"""
通關方式, 當課稅類別 [TaxType] 為 2 (零稅率)時
"""
ClearanceMark = {
    'Yes': '1',  # 經海關出口
    'No': '2',  # 非經海關出口
}

"""
課稅類別
"""
TaxType = {
    'Dutiable': '1',  # 應稅
    'Zero': '2',  # 零稅率
    'Free': '3',  # 免稅
    'Mix': '9',  # 應稅與免稅混合(限收銀機發票無法分辦時使用，且需通過申請核可)
}

"""
字軌類別
"""
InvType = {
    'General': '07',  # 一般稅額
    'Special': '08',  # 特種稅額
}

"""
銀聯卡交易選項
"""
UnionPay = {
    'Select': 0,  # 消費者於交易頁面可選擇是否使用銀聯交易
    'Only': 1,  # 只使用銀聯卡交易, 且綠界會將交易頁面直接導到銀聯網站
    'Hidden': 2,  # 不可使用銀聯卡, 綠界會將交易頁面隱藏銀聯選項
}
