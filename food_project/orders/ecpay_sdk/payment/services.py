# coding: utf-8
import requests
import json
import pprint
from urllib.parse import quote_plus, parse_qsl, parse_qs
from .enums import *
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


class CreateOrder(BasePayment):
    # 訂單基本參數
    __ORDER_REQUIRED_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'MerchantTradeNo': {'type': str, 'required': True, 'max': 20},
        'StoreID': {'type': str, 'required': False, 'max': 20},
        'MerchantTradeDate': {'type': str, 'required': True, 'max': 20},
        'PaymentType': {'default': 'aio', 'type': str, 'required': True, 'max': 20},
        'TotalAmount': {'type': int, 'required': True},
        'TradeDesc': {'type': str, 'required': True, 'max': 200},
        'ItemName': {'type': str, 'required': True, 'max': 200},
        'ReturnURL': {'type': str, 'required': True, 'max': 200},
        'ChoosePayment': {'type': str, 'required': True, 'max': 200},
        'ClientBackURL': {'type': str, 'required': False, 'max': 200},
        'ItemURL': {'type': str, 'required': False, 'max': 200},
        'Remark': {'type': str, 'required': False, 'max': 100},
        'ChooseSubPayment': {'type': str, 'required': False, 'max': 20},
        'OrderResultURL': {'type': str, 'required': False, 'max': 200},
        'NeedExtraPaidInfo': {'type': str, 'required': False, 'max': 1},
        'DeviceSource': {'type': str, 'required': False, 'max': 10},
        'IgnorePayment': {'type': str, 'required': False, 'max': 100},
        'PlatformID': {'type': str, 'required': False, 'max': 10},
        'InvoiceMark': {'type': str, 'required': False, 'max': 1},
        'CustomField1': {'type': str, 'required': False, 'max': 50},
        'CustomField2': {'type': str, 'required': False, 'max': 50},
        'CustomField3': {'type': str, 'required': False, 'max': 50},
        'CustomField4': {'type': str, 'required': False, 'max': 50},
        'EncryptType': {'default': 1, 'type': int, 'required': True},
    }

    # 使用 ALL 或 ATM 付款方式
    __ATM_EXTEND_PARAMETERS = {
        'ExpireDate': {'type': int, 'required': False},
        'PaymentInfoURL': {'type': str, 'required': False, 'max': 200},
        'ClientRedirectURL': {'type': str, 'required': False, 'max': 200},
    }

    # 使用 ALL 或 CVS 或 BARCODE 付款方式
    __CVS_BARCODE_EXTEND_PARAMETERS = {
        'StoreExpireDate': {'type': int, 'required': False, },
        'Desc_1': {'type': str, 'required': False, 'max': 20},
        'Desc_2': {'type': str, 'required': False, 'max': 20},
        'Desc_3': {'type': str, 'required': False, 'max': 20},
        'Desc_4': {'type': str, 'required': False, 'max': 20},
        'PaymentInfoURL': {'type': str, 'required': False, 'max': 200},
        'ClientRedirectURL': {'type': str, 'required': False, 'max': 200},
    }

    # 使用 ALL 或 Credit 付款方式
    __CREDIT_EXTEND_PARAMETERS_1 = {
        "BindingCard": {'type': int, 'required': False, },
        "MerchantMemberID": {'type': str, 'required': False, 'max': 30},
    }

    # 使用 Credit 付款方式
    __CREDIT_EXTEND_PARAMETERS_2 = {
        "Language": {'type': str, 'required': False, 'max': 3},
    }

    # 使用 ALL 或 Credit 付款方式: 一次付清(三擇一)
    __CREDIT_EXTEND_PARAMETERS_3 = {
        "Redeem": {'type': str, 'required': False, 'max': 1},
        "UnionPay": {'type': int, 'required': False, },
    }

    # 使用 ALL 或 Credit 付款方式: 分期付款、圓夢分期付款(三擇一)
    __CREDIT_EXTEND_PARAMETERS_4 = {
        "CreditInstallment": {'type': str, 'required': True, 'max': 20},
    }

    # 使用 ALL 或 Credit 付款方式: 定期定額(三擇一)
    __CREDIT_EXTEND_PARAMETERS_5 = {
        "PeriodAmount": {'type': int, 'required': True, },
        "PeriodType": {'type': str, 'required': True, 'max': 1},
        "Frequency": {'type': int, 'required': True, },
        "ExecTimes": {'type': int, 'required': True, },
        "PeriodReturnURL": {'type': str, 'required': False, 'max': 200},
    }

    # 電子發票延伸參數
    __INVOICE_EXTEND_PARAMETERS = {
        "RelateNumber": {'type': str, 'required': True, 'max': 30},
        "CustomerID": {'type': str, 'required': False, 'max': 20},
        "CustomerIdentifier": {'type': str, 'required': False, 'max': 8},
        "CustomerName": {'type': str, 'required': False, 'max': 30},
        "CustomerAddr": {'type': str, 'required': False, 'max': 200},
        "CustomerPhone": {'type': str, 'required': False, 'max': 20},
        "CustomerEmail": {'type': str, 'required': False, 'max': 200},
        "ClearanceMark": {'type': str, 'required': False, 'max': 1},
        "TaxType": {'type': str, 'required': True, 'max': 1},
        "CarruerType": {'type': str, 'required': False, 'max': 1},
        "CarruerNum": {'type': str, 'required': False, 'max': 64},
        "Donation": {'type': str, 'required': True, 'max': 1},
        "LoveCode": {'type': str, 'required': False, 'max': 7},
        "Print": {'type': str, 'required': True, 'max': 1},
        "InvoiceItemName": {'type': str, 'required': True, 'max': 100},
        "InvoiceItemCount": {'type': str, 'required': True, },
        "InvoiceItemWord": {'type': str, 'required': True, },
        "InvoiceItemPrice": {'type': str, 'required': True, },
        "InvoiceItemTaxType": {'type': str, 'required': False, },
        "InvoiceRemark": {'type': str, 'required': False, },
        "DelayDay": {'type': int, 'required': True, },
        "InvType": {'type': str, 'required': True, 'max': 2},
    }

    def create_order(self, client_parameters):
        self.__check_pattern = []
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__ORDER_REQUIRED_PARAMETERS)
        self.__check_pattern.append(self.__ORDER_REQUIRED_PARAMETERS)

        # 看看 client.dict 付款方式
        # 有的話 merge.dict 合併 payment.method.dict
        # 使用 ALL 或 ATM 付款方式
        choose_payment = client_parameters.get('ChoosePayment')
        if choose_payment == ChoosePayment['ALL'] or \
                choose_payment == ChoosePayment['ATM']:
            payment_extend_parameters = self.create_default_dict(
                self.__ATM_EXTEND_PARAMETERS)
            self.__check_pattern.append(self.__ATM_EXTEND_PARAMETERS)
            # 合併
            default_parameters = super().merge(
                default_parameters, payment_extend_parameters)

        # 使用 ALL 或 CVS 或 BARCODE 付款方式
        if choose_payment == ChoosePayment['ALL'] or \
                choose_payment == ChoosePayment['CVS'] or \
                choose_payment == ChoosePayment['BARCODE']:
            payment_extend_parameters = self.create_default_dict(
                self.__CVS_BARCODE_EXTEND_PARAMETERS)
            self.__check_pattern.append(self.__CVS_BARCODE_EXTEND_PARAMETERS)
            # 合併
            default_parameters = super().merge(
                default_parameters, payment_extend_parameters)

        # 使用 ALL 或 Credit 付款方式
        if choose_payment == ChoosePayment['ALL'] or \
                choose_payment == ChoosePayment['Credit']:
            payment_extend_parameters = self.create_default_dict(
                self.__CREDIT_EXTEND_PARAMETERS_1)
            self.__check_pattern.append(self.__CREDIT_EXTEND_PARAMETERS_1)
            # 合併
            default_parameters = super().merge(
                default_parameters, payment_extend_parameters)

        # 使用 Credit 付款方式
        if choose_payment == ChoosePayment['Credit']:
            payment_extend_parameters = self.create_default_dict(
                self.__CREDIT_EXTEND_PARAMETERS_2)
            self.__check_pattern.append(self.__CREDIT_EXTEND_PARAMETERS_2)
            # 合併
            default_parameters = super().merge(
                default_parameters, payment_extend_parameters)

        # 付款子方式 WebATM 大眾銀行跟永豐銀行已經無法使用
        if client_parameters.get('ChooseSubPayment') == ChooseSubPayment['WebATM']['TACHONG'] or \
                client_parameters.get('ChooseSubPayment') == ChooseSubPayment['WebATM']['SINOPAC']:
            raise Exception(
                'ChooseSubPayment is not supported with TACHONG or SINOPAC.')

        if choose_payment == ChoosePayment['ALL'] or \
                choose_payment == ChoosePayment['Credit']:
            credit_extend_parameters = dict()
            # 使用 ALL 或 Credit 付款方式: 一次付清(三擇一)
            if client_parameters.get('Redeem') or \
                    client_parameters.get('UnionPay'):
                credit_extend_parameters = self.create_default_dict(
                    self.__CREDIT_EXTEND_PARAMETERS_3)
                self.__check_pattern.append(self.__CREDIT_EXTEND_PARAMETERS_3)

            # 使用 ALL 或 Credit 付款方式: 分期付款、圓夢分期付款(三擇一)
            elif client_parameters.get('CreditInstallment'):
                credit_extend_parameters = self.create_default_dict(
                    self.__CREDIT_EXTEND_PARAMETERS_4)
                self.__check_pattern.append(self.__CREDIT_EXTEND_PARAMETERS_4)

            # 使用 ALL 或 Credit 付款方式: 定期定額(三擇一)
            elif client_parameters.get('PeriodAmount') or \
                    client_parameters.get('PeriodType') or \
                    client_parameters.get('Frequency') or \
                    client_parameters.get('ExecTimes') or \
                    client_parameters.get('PeriodReturnURL'):
                credit_extend_parameters = self.create_default_dict(
                    self.__CREDIT_EXTEND_PARAMETERS_5)
                self.__check_pattern.append(self.__CREDIT_EXTEND_PARAMETERS_5)
            # 合併
            if credit_extend_parameters:
                default_parameters = super().merge(
                    default_parameters, credit_extend_parameters)

        # 看看 client.dict 有無 invoice='Y'
        # 有的話 new.required.dict 合併 invoice.dict
        if client_parameters.get('InvoiceMark') == 'Y':
            invoice_parameters = self.create_default_dict(
                self.__INVOICE_EXTEND_PARAMETERS)
            self.__check_pattern.append(self.__INVOICE_EXTEND_PARAMETERS)
            # 合併
            default_parameters = super().merge(
                default_parameters, invoice_parameters)

            # 該參數有值時，請帶固定長度為數字 8 碼
            customer_identifier = client_parameters.get('CustomerIdentifier')
            if customer_identifier and (len(customer_identifier) != 8):
                raise Exception(
                    'CustomerIdentifier have to fill fixed length of 8 digits.')
            # 若統一編號 CustomerIdentifier 有值時，填入載具參數應出現錯誤訊息(不可以有載具)
            if customer_identifier and client_parameters.get('CarruerType'):
                raise Exception(
                    'CarruerType do not fill any value, when CustomerIdentifier have value.')
            # 統一編號 CustomerIdentifier 有值時，一定要列印，否則會出現錯誤訊息
            if customer_identifier and (client_parameters.get('Print') == '0'):
                raise Exception(
                    'Print have to fill "1", when CustomerIdentifier have value.')
            # 統一編號 CustomerIdentifier 有值時，Donation 要為 '0'，否則會出現錯誤訊息
            if customer_identifier and (client_parameters.get('Donation') == '1'):
                raise Exception(
                    'Donation have to fill "0", when CustomerIdentifier have value.')

            # 當列印註記 Print 為 1 (列印)時，則 CustomerName 與 CustomerAddr 參數必須有值
            print_param = client_parameters.get('Print')
            if (print_param == '1') and (not client_parameters.get('CustomerName')):
                raise Exception('CustomerName have to fill value.')
            if (print_param == '1') and (not client_parameters.get('CustomerAddr')):
                raise Exception('CustomerAddr have to fill value.')
            if (print_param == '1') and client_parameters.get('CarruerType'):
                raise Exception(
                    'CarruerType do not fill any value, when Print is "1".')

            # 當客戶電子信箱 CustomerEmail 為空字串時，則 CustomerPhone 參數必須有值
            customer_email = client_parameters.get('CustomerEmail')
            if (not customer_email) and (not client_parameters.get('CustomerPhone')):
                raise Exception('CustomerPhone have to fill value.')

            # 當客戶手機號碼 CustomerPhone 為空字串時，則 CustomerEmail 參數必須有值
            customer_email = client_parameters.get('CustomerPhone')
            if (not customer_email) and (not client_parameters.get('CustomerEmail')):
                raise Exception('CustomerEmail have to fill value.')

            # 當 Donation 為 '1' 時，Print 要為 '0'，否則會出現錯誤訊息
            donation_param = client_parameters.get('Donation')
            if (donation_param == '1') and (print_param == '1'):
                raise Exception(
                    'Print have to fill "0", when Donation is "1".')
            # 若捐贈註記 Donation = '1' (捐贈)時，LoveCode 須有值
            love_code = client_parameters.get('LoveCode')
            if (donation_param == '1') and (not love_code):
                raise Exception(
                    'LoveCode have to fill value, when Donation is "1".')
            if love_code:
                if len(love_code) < 3 or len(love_code) > 7:
                    raise Exception(
                        'LoveCode have to fill fixed length of 3~7 digits.')

            urlencode_parameters = ['CustomerName', 'CustomerAddr', 'CustomerEmail',
                                    'InvoiceItemName', 'InvoiceItemWord', 'InvoiceRemark']

            for urlencode_parameter in urlencode_parameters:
                for k, v in client_parameters.items():
                    if urlencode_parameter == k:
                        client_parameters.update(
                            {k: quote_plus(str(v)).lower()})

        # 用 new.required.dict 與 client.dict 合併為 merge.dict
        self.final_merge_parameters = super().merge(
            default_parameters, client_parameters)

        # 檢查參數, 並產生 CheckMacValue
        self.final_merge_parameters = self.integrate_parameter(
            self.final_merge_parameters,
            self.__check_pattern)

        # 回傳給 client
        return self.final_merge_parameters


class OrderSearch(BasePayment):
    # 訂單基本參數
    __ORDER_SEARCH_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'MerchantTradeNo': {'type': str, 'required': True, 'max': 20},
        'TimeStamp': {'type': int, 'required': True, },
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://payment.ecpay.com.tw/Cashier/QueryTradeInfo/V5'

    def order_search(self, action_url=__url, client_parameters={}):
        self.__check_pattern = []
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__ORDER_SEARCH_PARAMETERS)
        self.__check_pattern.append(self.__ORDER_SEARCH_PARAMETERS)

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
        if query.get('CheckMacValue') == self.generate_check_value(query):
            query.pop('CheckMacValue')
            return query
        else:
            raise Exception("CheckMacValue is error!")


class OrderSearchPeriodic(BasePayment):
    # 訂單基本參數
    __ORDER_SEARCH_PERIODIC_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'MerchantTradeNo': {'type': str, 'required': True, 'max': 20},
        'TimeStamp': {'type': int, 'required': True, },
    }

    __url = 'https://payment.ecpay.com.tw/Cashier/QueryCreditCardPeriodInfo'

    def order_search_period(self, action_url=__url, client_parameters={}):
        self.__check_pattern = []
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__ORDER_SEARCH_PERIODIC_PARAMETERS)
        self.__check_pattern.append(self.__ORDER_SEARCH_PERIODIC_PARAMETERS)

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
        query = json.loads(response.text)
        return query


class CreditDoAction(BasePayment):
    # 訂單基本參數
    __CREDIT_DO_ACTION_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'MerchantTradeNo': {'type': str, 'required': True, 'max': 20},
        'TradeNo': {'type': str, 'required': True, 'max': 20},
        'Action': {'type': str, 'required': True, 'max': 1},
        'TotalAmount': {'type': int, 'required': True, },
        'PlatformID': {'type': str, 'required': False, 'max': 10},
    }

    __url = 'https://payment.ecpay.com.tw/CreditDetail/DoAction'

    def credit_do_action(self, action_url=__url, client_parameters={}):
        self.__check_pattern = []
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__CREDIT_DO_ACTION_PARAMETERS)
        self.__check_pattern.append(self.__CREDIT_DO_ACTION_PARAMETERS)

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


class DownloadMerchantBalance(BasePayment):
    # 基本參數
    __DOWNLOAD_MERCHANT_BALANCE_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'DateType': {'type': str, 'required': True, 'max': 1},
        'BeginDate': {'type': str, 'required': True, 'max': 10},
        'EndDate': {'type': str, 'required': True, 'max': 10},
        'PaymentType': {'type': str, 'required': False, 'max': 2},
        'PlatformStatus': {'type': str, 'required': False, 'max': 1},
        'PaymentStatus': {'type': str, 'required': False, 'max': 1},
        'AllocateStatus': {'type': str, 'required': False, 'max': 1},
        'MediaFormated': {'type': str, 'required': True, 'max': 1},
    }

    __url = 'https://vendor.ecpay.com.tw/PaymentMedia/TradeNoAio'

    def download_merchant_balance(self, action_url=__url, client_parameters={}):
        self.__check_pattern = []
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__DOWNLOAD_MERCHANT_BALANCE_PARAMETERS)
        self.__check_pattern.append(
            self.__DOWNLOAD_MERCHANT_BALANCE_PARAMETERS)

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
        response.encoding = 'big5'
        return response.text


class SearchSingleTransaction(BasePayment):
    # 基本參數
    __SEARCH_SINGLE_TRANSACTION_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'CreditRefundId': {'type': int, 'required': True, },
        'CreditAmount': {'type': int, 'required': True, },
        'CreditCheckCode': {'type': int, 'required': True, },
    }

    __url = 'https://payment.ecPay.com.tw/CreditDetail/QueryTrade/V2'

    def search_single_transaction(self, action_url=__url, client_parameters={}):
        self.__check_pattern = []
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__SEARCH_SINGLE_TRANSACTION_PARAMETERS)
        self.__check_pattern.append(
            self.__SEARCH_SINGLE_TRANSACTION_PARAMETERS)

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
        query = json.loads(response.text)

        return query


class DownloadDisbursementBalance(BasePayment):
    # 基本參數
    __DOWNLOAD_DISBURSEMENT_BALANCE_PARAMETERS = {
        'MerchantID': {'type': str, 'required': True, 'max': 10},
        'PayDateType': {'type': str, 'required': True, 'max': 10},
        'StartDate': {'type': str, 'required': True, 'max': 10},
        'EndDate': {'type': str, 'required': True, 'max': 10},
    }

    __url = 'https://payment.ecPay.com.tw/CreditDetail/FundingReconDetail'

    def download_disbursement_balance(self, action_url=__url, client_parameters={}):
        self.__check_pattern = []
        if action_url is None:
            action_url = self.__url
        # 先用 required.dict 設定預設值並產生新 new.required.dict
        default_parameters = dict()
        default_parameters = self.create_default_dict(
            self.__DOWNLOAD_DISBURSEMENT_BALANCE_PARAMETERS)
        self.__check_pattern.append(
            self.__DOWNLOAD_DISBURSEMENT_BALANCE_PARAMETERS)

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
        response.encoding = 'big5'
        return response.text
