from .payment.services import *


class ECPayPaymentSdk(CreateOrder, OrderSearch, OrderSearchPeriodic,
                      CreditDoAction, DownloadMerchantBalance, SearchSingleTransaction,
                      DownloadDisbursementBalance, ExtendFunction):

    def __init__(self, MerchantID='', HashKey='', HashIV=''):
        self.MerchantID = MerchantID
        self.HashKey = HashKey
        self.HashIV = HashIV
