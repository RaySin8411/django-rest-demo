# coding: utf-8
import collections
import copy
import hashlib
import requests
from decimal import Decimal
from urllib.parse import quote_plus


class BasePayment(object):

    def merge(self, x, y):
        """
        Given two dicts, merge them into a new dict as a shallow copy.
        """
        z = x.copy()
        z.update(y)
        return z

    # 檢查必填參數
    # 檢查 merge.dict 是否有填正確的值或範圍
    def check_required_parameter(self, parameters, patterns):
        for patten in patterns:
            for k, v in patten.items():
                if v.get('required') and (v.get('type') is str):
                    if parameters.get(k) is None:
                        raise Exception('parameter %s is required.' % k)
                    elif len(parameters.get(k)) == 0:
                        raise Exception('%s content is required.' % k)
                    elif len(parameters.get(k)) > v.get('max'):
                        raise Exception('%s max langth is %d.' %
                                        (k, v.get('max')))
                elif v.get('required') and (v.get('type') is int):
                    if parameters.get(k) is None:
                        raise Exception('parameter %s is required.' % k)

    # 先用 required.dict 設定預設值並產生新 new.required.dict
    def create_default_dict(self, parameters):
        default_dict = dict()
        for k, v in parameters.items():
            if v['type'] is str:
                default_dict.setdefault(k, '')
            elif v['type'] is int:
                default_dict.setdefault(k, 0)
            else:
                raise Exception('unsupported type!')
        for k, v in parameters.items():
            if v.get('default'):
                default_dict[k] = v.get('default')
        return default_dict

    # 檢查 merge.dict 是否有填正確的值或範圍
    def filter_parameter(self, parameters, pattern):
        for patten in pattern:
            for k, v in patten.items():
                if (v.get('required') is False) and (v.get('type') is str):
                    if parameters.get(k) is None:
                        continue
                    if len(parameters.get(k)) == 0:
                        del parameters[k]
                elif (v.get('required') is False) and (v.get('type') is int):
                    if parameters.get(k) is None:
                        continue
                    if parameters.get(k) == 0:
                        del parameters[k]

    def generate_check_value(self, params):
        _params = copy.deepcopy(params)

        if 'CheckMacValue' in _params:
            _params.pop('CheckMacValue')

        ordered_params = collections.OrderedDict(
            sorted(_params.items(), key=lambda k: k[0]))

        encoding_lst = []
        encoding_lst.append('HashKey=%s&' % self.HashKey)
        encoding_lst.append(''.join(
            ['{}={}&'.format(key, value) for key, value in ordered_params.items()]))
        encoding_lst.append('HashIV=%s' % self.HashIV)

        safe_characters = '-_.!*()'

        encoding_str = ''.join(encoding_lst)
        encoding_str = quote_plus(
            str(encoding_str), safe=safe_characters).lower()

        check_mac_value = hashlib.md5(
            encoding_str.encode('utf-8')).hexdigest().upper()
        return check_mac_value

    def integrate_parameter(self, parameters, patterns):
        # 更新 MerchantID
        parameters['MerchantID'] = self.MerchantID
        # 檢查必填參數
        self.check_required_parameter(parameters, patterns)
        # 將 merge.dict 內的無用參數消除
        self.filter_parameter(parameters, patterns)
        # 計算 CheckMacValue
        parameters['CheckMacValue'] = self.generate_check_value(parameters)
        return parameters

    def send_post(self, url, params):
        response = requests.post(url, data=params)
        return response
