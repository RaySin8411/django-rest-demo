# coding: utf-8
from urllib.parse import parse_qsl
from .utils import BasePayment


class ExtendFunction(BasePayment):

    def gen_html_post_form(self, action, parameters):
        html = '<form id="data_set" action="' + action + '" method="post">'
        for k, v in parameters.items():
            html += '<input type="hidden" name="' + \
                    str(k) + '" value="' + str(v) + '" />'

        html += '<script type="text/javascript">document.getElementById("data_set").submit();</script>'
        html += "</form>"
        return html


class CvsMap(BasePayment):
    __CVS_MAP_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'MerchantTradeNo': {'type': str, 'required': False, 'max': 20},
        'LogisticsType': {'type': str, 'required': True, 'max': 20},
        'LogisticsSubType': {'type': str, 'required': True, 'max': 20},
        'IsCollection': {'type': str, 'required': True, 'max': 1},
        'ServerReplyURL': {'type': str, 'required': True, 'max': 200},
        'ExtraData': {'type': str, 'required': False, 'max': 20},
        'Device': {'type': int, 'required': False, },
    }

    __url = 'https://logistics.ecpay.com.tw/Express/map'
    __final_merge_parameters = dict()
    __check_pattern = []

    def cvs_map(self, client_parameters):
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CVS_MAP_PARAMETERS)
        self.__check_pattern.append(
            self.__CVS_MAP_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        # CheckMacValue 並無使用, 移除它
        self.final_merge_parameters.pop('CheckMacValue')

        return self.final_merge_parameters


class CreateShippingOrder(BasePayment):
    __CREATE_SHIPPING_ORDER_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'MerchantTradeNo': {'type': str, 'required': False, 'max': 20},
        'MerchantTradeDate': {'type': str, 'required': True, 'max': 20},
        'LogisticsType': {'type': str, 'required': True, 'max': 20},
        'LogisticsSubType': {'type': str, 'required': True, 'max': 20},
        'GoodsAmount': {'type': int, 'required': True, },
        'CollectionAmount': {'type': int, 'required': False, },
        'IsCollection': {'type': str, 'required': False, 'max': 1},
        'GoodsName': {'type': str, 'required': False, 'max': 50},
        'SenderName': {'type': str, 'required': True, 'max': 10},
        'SenderPhone': {'type': str, 'required': False, 'max': 20},
        'SenderCellPhone': {'type': str, 'required': False, 'max': 20},
        'ReceiverName': {'type': str, 'required': True, 'max': 10},
        'ReceiverPhone': {'type': str, 'required': False, 'max': 20},
        'ReceiverCellPhone': {'type': str, 'required': False, 'max': 20},
        'ReceiverEmail': {'type': str, 'required': False, 'max': 50},
        'TradeDesc': {'type': str, 'required': False, 'max': 200},
        'ServerReplyURL': {'type': str, 'required': True, 'max': 200},
        'ClientReplyURL': {'type': str, 'required': False, 'max': 200},
        'LogisticsC2CReplyURL': {'type': str, 'required': False, 'max': 200},
        'Remark': {'type': str, 'required': False, 'max': 200},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/Create'
    __final_merge_parameters = dict()
    __check_pattern = []

    def create_shipping_order(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CREATE_SHIPPING_ORDER_PARAMETERS)
        self.__check_pattern.append(self.__CREATE_SHIPPING_ORDER_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        # 回傳給 client
        response = super().send_post(
            action_url, self.final_merge_parameters)
        normal_qs = response.text.split('|')[1]
        query = dict(parse_qsl(normal_qs, keep_blank_values=True))

        return query


class CreateHomeReturnOrder(BasePayment):
    __CREATE_HOME_RETURN_ORDER_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': False, 'max': 20},
        'LogisticsSubType': {'type': str, 'required': False, 'max': 20},
        'ServerReplyURL': {'type': str, 'required': True, 'max': 200},
        'SenderName': {'type': str, 'required': False, 'max': 10},
        'SenderPhone': {'type': str, 'required': False, 'max': 20},
        'SenderCellPhone': {'type': str, 'required': False, 'max': 20},
        'SenderZipCode': {'type': str, 'required': False, 'max': 5},
        'SenderAddress': {'type': str, 'required': False, 'max': 60},
        'ReceiverName': {'type': str, 'required': False, 'max': 10},
        'ReceiverPhone': {'type': str, 'required': False, 'max': 20},
        'ReceiverCellPhone': {'type': str, 'required': False, 'max': 20},
        'ReceiverZipCode': {'type': str, 'required': False, 'max': 5},
        'ReceiverAddress': {'type': str, 'required': False, 'max': 60},
        'ReceiverEmail': {'type': str, 'required': False, 'max': 50},
        'GoodsAmount': {'type': int, 'required': True, },
        'GoodsName': {'type': str, 'required': False, 'max': 60},
        'Temperature': {'type': str, 'required': True, 'max': 4},
        'Distance': {'type': str, 'required': True, 'max': 2},
        'Specification': {'type': str, 'required': True, 'max': 4},
        'ScheduledPickupTime': {'type': str, 'required': False, 'max': 1},
        'ScheduledDeliveryTime': {'type': str, 'required': False, 'max': 2},
        'ScheduledDeliveryDate': {'type': str, 'required': False, 'max': 10},
        'PackageCount': {'type': int, 'required': True, },
        'Remark': {'type': str, 'required': False, 'max': 200},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/ReturnHome'
    __final_merge_parameters = dict()
    __check_pattern = []

    def create_home_return_order(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CREATE_HOME_RETURN_ORDER_PARAMETERS)
        self.__check_pattern.append(self.__CREATE_HOME_RETURN_ORDER_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        # 回傳給 client
        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class CreateFamilyB2CReturnOrder(BasePayment):
    __CREATE_FAMILY_B2C_RETURN_ORDER_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': False, 'max': 20},
        'ServerReplyURL': {'type': str, 'required': True, 'max': 200},
        'GoodsName': {'type': str, 'required': False, 'max': 50},
        'GoodsAmount': {'type': int, 'required': True, },
        'CollectionAmount': {'type': int, 'required': False, },
        'ServiceType': {'type': str, 'required': True, 'max': 5},
        'SenderName': {'type': str, 'required': True, 'max': 50},
        'SenderPhone': {'type': str, 'required': False, 'max': 20},
        'Remark': {'type': str, 'required': False, 'max': 20},
        'Quantity': {'type': str, 'required': False, 'max': 50},
        'Cost': {'type': str, 'required': False, 'max': 50},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/express/ReturnCVS'
    __final_merge_parameters = dict()
    __check_pattern = []

    def create_family_b2c_return_order(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CREATE_FAMILY_B2C_RETURN_ORDER_PARAMETERS)
        self.__check_pattern.append(
            self.__CREATE_FAMILY_B2C_RETURN_ORDER_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class CheckFamilyB2CLogistics(BasePayment):
    __CHECK_FAMILY_B2C_LOGISTICS_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'RtnMerchantTradeNo': {'type': str, 'required': True, 'max': 13},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Helper/LogisticsCheckAccoounts'
    __final_merge_parameters = dict()
    __check_pattern = []

    def check_family_b2c_logistics(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CHECK_FAMILY_B2C_LOGISTICS_PARAMETERS)
        self.__check_pattern.append(
            self.__CHECK_FAMILY_B2C_LOGISTICS_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class CreateHiLifeB2CReturnOrder(BasePayment):
    __CREATE_HILIFE_B2C_RETURN_ORDER_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': False, 'max': 20},
        'ServerReplyURL': {'type': str, 'required': True, 'max': 200},
        'GoodsName': {'type': str, 'required': False, 'max': 60},
        'GoodsAmount': {'type': int, 'required': True, },
        'CollectionAmount': {'type': int, 'required': False, },
        'ServiceType': {'type': str, 'required': True, 'max': 5},
        'SenderName': {'type': str, 'required': True, 'max': 50},
        'SenderPhone': {'type': str, 'required': False, 'max': 20},
        'Remark': {'type': str, 'required': False, 'max': 20},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/express/ReturnHiLifeCVS'
    __final_merge_parameters = dict()
    __check_pattern = []

    def create_hilife_b2c_return_order(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CREATE_HILIFE_B2C_RETURN_ORDER_PARAMETERS)
        self.__check_pattern.append(
            self.__CREATE_HILIFE_B2C_RETURN_ORDER_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class CreateUnimartB2CReturnOrder(BasePayment):
    __CREATE_UNIMART_B2C_RETURN_ORDER_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': False, 'max': 20},
        'ServerReplyURL': {'type': str, 'required': True, 'max': 200},
        'GoodsName': {'type': str, 'required': False, 'max': 50},
        'GoodsAmount': {'type': int, 'required': True, },
        'CollectionAmount': {'type': int, 'required': False, },
        'ServiceType': {'type': str, 'required': True, 'max': 5},
        'SenderName': {'type': str, 'required': True, 'max': 50},
        'SenderPhone': {'type': str, 'required': False, 'max': 20},
        'Remark': {'type': str, 'required': False, 'max': 20},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/express/ReturnUniMartCVS'
    __final_merge_parameters = dict()
    __check_pattern = []

    def create_unimart_b2c_return_order(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CREATE_UNIMART_B2C_RETURN_ORDER_PARAMETERS)
        self.__check_pattern.append(
            self.__CREATE_UNIMART_B2C_RETURN_ORDER_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class UpdateUnimartLogisticsInfo(BasePayment):
    # 訂單基本參數
    __UPDATE_UNIMART_LOGISTICS_INFO_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'ShipmentDate': {'type': str, 'required': False, 'max': 10},
        'ReceiverStoreID': {'type': str, 'required': False, 'max': 6},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Helper/UpdateShipmentInfo'
    __final_merge_parameters = dict()
    __check_pattern = []

    def update_unimart_logistics_info(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__UPDATE_UNIMART_LOGISTICS_INFO_PARAMETERS)
        self.__check_pattern.append(
            self.__UPDATE_UNIMART_LOGISTICS_INFO_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class UpdateUnimartStore(BasePayment):
    __UPDATE_UNIMART_STORE_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'CVSPaymentNo': {'type': str, 'required': True, 'max': 15},
        'CVSValidationNo': {'type': str, 'required': True, 'max': 10},
        'StoreType': {'type': str, 'required': True, 'max': 2},
        'ReceiverStoreID': {'type': str, 'required': False, 'max': 6},
        'ReturnStoreID': {'type': str, 'required': False, 'max': 6},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/UpdateStoreInfo'
    __final_merge_parameters = dict()
    __check_pattern = []

    def update_unimart_store(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__UPDATE_UNIMART_STORE_PARAMETERS)
        self.__check_pattern.append(self.__UPDATE_UNIMART_STORE_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class CancelUnimartLogisticsOrder(BasePayment):
    __CANCEL_UNIMART_LOGISTICS_ORDER_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'CVSPaymentNo': {'type': str, 'required': True, 'max': 15},
        'CVSValidationNo': {'type': str, 'required': True, 'max': 10},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/CancelC2COrder'
    __final_merge_parameters = dict()
    __check_pattern = []

    def cancel_unimart_logistics_order(self, action_url=__url, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CANCEL_UNIMART_LOGISTICS_ORDER_PARAMETERS)
        self.__check_pattern.append(
            self.__CANCEL_UNIMART_LOGISTICS_ORDER_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        response = super().send_post(
            action_url, self.final_merge_parameters)
        return response.text


class QueryLogisticsInfo(BasePayment):
    __QUERY_LOGISTICS_INFO_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'TimeStamp': {'type': int, 'required': True, },
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Helper/QueryLogisticsTradeInfo/V2'
    __final_merge_parameters = dict()
    __check_pattern = []

    def query_logistics_info(self, action_url=None, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__QUERY_LOGISTICS_INFO_PARAMETERS)
        self.__check_pattern.append(self.__QUERY_LOGISTICS_INFO_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        # 回傳給 client
        response = super().send_post(
            action_url, self.final_merge_parameters)
        query = dict(parse_qsl(response.text, keep_blank_values=True))

        return query


class PrintTradeDoc(BasePayment):
    __PRINT_TRADE_DOC_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/helper/printTradeDocument'
    __final_merge_parameters = dict()
    __check_pattern = []

    def print_trade_doc(self, action_url=None, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__PRINT_TRADE_DOC_PARAMETERS)
        self.__check_pattern.append(self.__PRINT_TRADE_DOC_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        return self.final_merge_parameters


class PrintUnimartC2CBill(BasePayment):
    __PRINT_UNIMART_C2C_BILL_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'CVSPaymentNo': {'type': str, 'required': True, 'max': 15},
        'CVSValidationNo': {'type': str, 'required': True, 'max': 10},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/PrintUniMartC2COrderInfo'
    __final_merge_parameters = dict()
    __check_pattern = []

    def print_unimart_c2c_bill(self, action_url=None, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__PRINT_UNIMART_C2C_BILL_PARAMETERS)
        self.__check_pattern.append(
            self.__PRINT_UNIMART_C2C_BILL_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        return self.final_merge_parameters


class PrintFamilyC2CBill(BasePayment):
    __PRINT_FAMILY_C2C_BILL_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'CVSPaymentNo': {'type': str, 'required': True, 'max': 15},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/PrintFAMIC2COrderInfo'
    __final_merge_parameters = dict()
    __check_pattern = []

    def print_family_c2c_bill(self, action_url=None, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__PRINT_FAMILY_C2C_BILL_PARAMETERS)
        self.__check_pattern.append(
            self.__PRINT_FAMILY_C2C_BILL_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        return self.final_merge_parameters


class PrintHiLifeC2CBill(BasePayment):
    __PRINT_HILIFE_C2C_BILL_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'AllPayLogisticsID': {'type': str, 'required': True, 'max': 20},
        'CVSPaymentNo': {'type': str, 'required': True, 'max': 15},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/PrintHILIFEC2COrderInfo'
    __final_merge_parameters = dict()
    __check_pattern = []

    def print_hilife_c2c_bill(self, action_url=None, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__PRINT_HILIFE_C2C_BILL_PARAMETERS)
        self.__check_pattern.append(
            self.__PRINT_HILIFE_C2C_BILL_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        return self.final_merge_parameters


class CreateTestData(BasePayment):
    __CREATE_TEST_DATA_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'ClientReplyURL': {'type': str, 'required': False, 'max': 200},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
        'LogisticsSubType': {'type': str, 'required': True, 'max': 20},
    }

    __url = 'https://logistics.ecpay.com.tw/Express/CreateTestData'
    __final_merge_parameters = dict()
    __check_pattern = []

    def create_test_data(self, action_url=None, client_parameters=None):
        if client_parameters is None:
            client_parameters = {}
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CREATE_TEST_DATA_PARAMETERS)
        self.__check_pattern.append(
            self.__CREATE_TEST_DATA_PARAMETERS)

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        # 回傳給 client
        response = super().send_post(
            action_url, self.final_merge_parameters)
        query = dict(parse_qsl(response.text, keep_blank_values=True))

        return query
