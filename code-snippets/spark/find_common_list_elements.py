# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:40:27 2019

@author: amitabh.gunjan
"""
a_d = [{'passThrough': 'No', 'totalNoOfRecords': '211', 'pricing': 'P', 'quotaMonth': 'May 2019 To Oct 2019', 'contractType': 'CONCENTRATES', 'finalInvoicedQty': '0 MT', 'titleTransferQty': '0 MT', 'tollingServiceType': 'Sell Tolling', 'quotaOpenQty': '249.94 MT', 'quotaQuantityBasis': 'N/A', 'qualityName': 'Copper cooling scrap', 'quotaQty': '300', 'location': 'Sweden,Sweden,Ronnskar', 'qpPricing': '', 'provInvoicedQty': '0 MT', 'userId': '23', 'contractRefNo': 'SCT-1924-BLD', 'allocatedQty': '0 MT', 'itemStatus': '', 'rnum': '117', 'tabRequestId': '', 'fullfillmentQty': '0', 'calledOffQty': 'N/A', 'quotaInvoicedQty': '', 'tradeType': '', 'quotaDeliveredReceivedQty': '', 'lisitngCreatedBy': '', 'listingCreatedDate': '', 'cpName': 'MC Metallhandel GmbH', 'fromDate': 'May 2019', 'incotermLocation': 'Ronnskar-DAP-2010', 'contractqty': '1200 Dry', 'contractStatus': 'In Position', 'fixedPriceQty': '0 MT', 'executableQty': '249.94 MT', 'isInterCompanyContract': 'No', 'assetclass': 'Cu material', 'quotaQuantityMax': '300', 'traxysOrg': '', 'issueDate': '30-Apr-2019', 'strategy': 'BCAB', 'deliveryItemRefNo': 'SCT-1924-BLD-1', 'executedQty': '50.06 MT', 'payInCurrency': 'EUR', 'fullfillmentStatus': 'Not Fulfilled', 'dealType': '', 'pricingStatus': 'Not Applicable', 'delLocation': 'Ronnskar', 'pcdiId': '8733', 'attributes': 'Details', 'productGroupType': 'CONCENTRATES', 'quotaPriceFixedQty': '', 'quotaCalloffQty': '', 'quotaQtyBasis': '', 'interCompanyContractRefNo': 'N/A', 'listingUpdatedBy': '', 'toDate': 'Oct 2019', 'openQty': '249.94 MT', 'orderLineNo': '', 'qp': '', 'physicalOptPresent': 'N', 'cpAddress': 'Gwinnerstrasse 11\nDE-60388 Frankfurt am Main\nGermany,Germany', 'trader': 'Anders Dahlberg', 'internalContractRefNo': '3480', 'lisitingUpdatedDate': '', 'bookProfitCenter': 'Boliden Commercial AB', 'qpPricingBasis': '', 'priceOptionCallOffStatus': 'Not Applicable', 'toBeCalledOffQty': 'N/A', 'quotaQtyUnit': 'MT'},
{'passThrough': 'No', 'totalNoOfRecords': '211', 'pricing': 'P', 'quotaMonth': 'May 2019 To Dec 2019', 'contractType': 'CONCENTRATES', 'finalInvoicedQty': '0 MT', 'titleTransferQty': '52.15 MT', 'tollingServiceType': 'Sell Tolling', 'quotaOpenQty': '185.55 MT', 'quotaQuantityBasis': 'N/A', 'qualityName': 'Electronic scrap', 'quotaQty': '300', 'location': 'Sweden,Sweden,Ronnskar', 'qpPricing': '', 'provInvoicedQty': '0 MT', 'userId': '23', 'contractRefNo': 'SCT-1922-BLD', 'allocatedQty': '0 MT', 'itemStatus': '', 'rnum': '114', 'tabRequestId': '', 'fullfillmentQty': '0', 'calledOffQty': 'N/A', 'quotaInvoicedQty': '', 'tradeType': '', 'quotaDeliveredReceivedQty': '', 'lisitngCreatedBy': '', 'listingCreatedDate': '', 'cpName': 'METALLUM METAL TRADING AG', 'fromDate': 'May 2019', 'incotermLocation': 'Ronnskar-DAP-2010', 'contractqty': '300 Dry', 'contractStatus': 'In Position', 'fixedPriceQty': '0 MT', 'executableQty': '185.55 MT', 'isInterCompanyContract': 'No', 'assetclass': 'E material', 'quotaQuantityMax': '300', 'traxysOrg': '', 'issueDate': '25-Apr-2019', 'strategy': 'BCAB', 'deliveryItemRefNo': 'SCT-1922-BLD-1', 'executedQty': '114.45 MT', 'payInCurrency': 'EUR', 'fullfillmentStatus': 'Not Fulfilled', 'dealType': '', 'pricingStatus': 'Not Applicable', 'delLocation': 'Ronnskar', 'pcdiId': '8726', 'attributes': 'Details', 'productGroupType': 'CONCENTRATES', 'quotaPriceFixedQty': '', 'quotaCalloffQty': '', 'quotaQtyBasis': '', 'interCompanyContractRefNo': 'N/A', 'listingUpdatedBy': '', 'toDate': 'Dec 2019', 'openQty': '185.55 MT', 'orderLineNo': '', 'qp': '', 'physicalOptPresent': 'N', 'cpAddress': 'Althardstrasse 345,Switzerland', 'trader': 'Jörgen Johansson', 'internalContractRefNo': '3478', 'lisitingUpdatedDate': '', 'bookProfitCenter': 'Boliden Commercial AB', 'qpPricingBasis': '', 'priceOptionCallOffStatus': 'Not Applicable', 'toBeCalledOffQty': 'N/A', 'quotaQtyUnit': 'MT'}]
var_list =  ['qtyUnitName', 'incoterm', 'LoadingLocationCountry', 'city', 'incoTermId', 'LoadingLocationCity', 'particleSize', 'supplierName', 'dischargeCountryId', 'dischargeCityId', 'incoLocation', 'maxLotSize', 'qtyUnitId', 'Quality', 'supplierId']

def extract_variables(list_dicts, all_vars_list):
    """Remove the variables that are not useful for model training."""
    dict_list = []
    for dicts in list_dicts:
#        print(dicts)
#        print(1)
        # if all(keys in dicts for keys in all_vars_list):
        keys_list = [k for k,v in dicts.items()]
        print(keys_list)
        if all(keys in all_vars_list for keys in keys_list):
            dict_list.append(dicts)
        else:
            pass
    return dict_list
vars_ = extract_variables(a_d, var_list)
print(vars_)

