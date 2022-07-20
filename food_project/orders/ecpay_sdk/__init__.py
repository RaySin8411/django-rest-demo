from .payment.services import *
from .logistic.services import *


class ECPayPaymentSdk(CreateOrder, OrderSearch, OrderSearchPeriodic,
                      CreditDoAction, DownloadMerchantBalance, SearchSingleTransaction,
                      DownloadDisbursementBalance, ExtendFunction):

    def __init__(self, MerchantID='', HashKey='', HashIV=''):
        self.MerchantID = MerchantID
        self.HashKey = HashKey
        self.HashIV = HashIV


class ECPayLogisticSdk(CvsMap, CreateShippingOrder, CreateHomeReturnOrder,
                       CreateFamilyB2CReturnOrder, CheckFamilyB2CLogistics,
                       CreateHiLifeB2CReturnOrder, CreateUnimartB2CReturnOrder,
                       UpdateUnimartLogisticsInfo, UpdateUnimartStore,
                       CancelUnimartLogisticsOrder, QueryLogisticsInfo,
                       PrintTradeDoc, PrintUnimartC2CBill, PrintFamilyC2CBill,
                       PrintHiLifeC2CBill, CreateTestData,
                       ExtendFunction):

    def __init__(self, MerchantID='', HashKey='', HashIV=''):
        self.MerchantID = MerchantID
        self.HashKey = HashKey
        self.HashIV = HashIV
