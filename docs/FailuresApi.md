# swagger_client.FailuresApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_failures**](FailuresApi.md#get_failures) | **GET** /failures | Get detail on historical bank failures from 1934 to present.

# **get_failures**
> object get_failures(filters=filters, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, total_fields=total_fields, subtotal_by=subtotal_by, agg_by=agg_by, agg_term_fields=agg_term_fields, agg_sum_fields=agg_sum_fields, agg_limit=agg_limit, format=format, download=download, filename=filename)

Get detail on historical bank failures from 1934 to present.

Returns details on failed financial institutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FailuresApi()
filters = 'filters_example' # str | The filter criteria that refines the records returned.  Examples: * Filter by Location               `CITYST:\"MEMPHIS, TN\"`   * Filter by institution fail year range   `FAILYR:[\"2015\" TO \"2016\"]`  (optional)
fields = 'fields_example' # str | Comma delimited list of fields of failed financial institutions to return. (optional)
sort_by = 'FAILDATE' # str | Field name by which to sort returned data (optional) (default to FAILDATE)
sort_order = 'ASC' # str | Indicator if ascending (ASC) or descending (DESC) (optional) (default to ASC)
limit = 100 # int | The number of records to return. Default is 10 and maximum is 10,000. (optional) (default to 100)
offset = 0 # int | The offset of page to return. (optional) (default to 0)
total_fields = 'total_fields_example' # str | Fields to sum up (in a totals response object). Only numeric columns are valid. (optional)
subtotal_by = 'subtotal_by_example' # str | The field by which data will be subtotaled (in totals response object). Only categorical values should be used. (optional)
agg_by = 'agg_by_example' # str | The field(s) by which data will be aggregated. Valid values are 'FAILYR' or 'FAILYR,PSTALP'. (optional)
agg_term_fields = 'agg_term_fields_example' # str | The field(s) for which aggregations will be counted for each unique term. (optional)
agg_sum_fields = 'agg_sum_fields_example' # str | The field(s) for which aggregations will be summed or aggregated. (optional)
agg_limit = 10 # int | The limit on how many aggregated results will be displayed (optional) (default to 10)
format = 'format_example' # str | The format of the data to return. (optional)
download = 'download_example' # str | Whether the data should be downloaded as a file. (optional)
filename = 'filename_example' # str | The filename to use when downloading data. (optional)

try:
    # Get detail on historical bank failures from 1934 to present.
    api_response = api_instance.get_failures(filters=filters, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, total_fields=total_fields, subtotal_by=subtotal_by, agg_by=agg_by, agg_term_fields=agg_term_fields, agg_sum_fields=agg_sum_fields, agg_limit=agg_limit, format=format, download=download, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FailuresApi->get_failures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| The filter criteria that refines the records returned.  Examples: * Filter by Location               &#x60;CITYST:\&quot;MEMPHIS, TN\&quot;&#x60;   * Filter by institution fail year range   &#x60;FAILYR:[\&quot;2015\&quot; TO \&quot;2016\&quot;]&#x60;  | [optional] 
 **fields** | **str**| Comma delimited list of fields of failed financial institutions to return. | [optional] 
 **sort_by** | **str**| Field name by which to sort returned data | [optional] [default to FAILDATE]
 **sort_order** | **str**| Indicator if ascending (ASC) or descending (DESC) | [optional] [default to ASC]
 **limit** | **int**| The number of records to return. Default is 10 and maximum is 10,000. | [optional] [default to 100]
 **offset** | **int**| The offset of page to return. | [optional] [default to 0]
 **total_fields** | **str**| Fields to sum up (in a totals response object). Only numeric columns are valid. | [optional] 
 **subtotal_by** | **str**| The field by which data will be subtotaled (in totals response object). Only categorical values should be used. | [optional] 
 **agg_by** | **str**| The field(s) by which data will be aggregated. Valid values are &#x27;FAILYR&#x27; or &#x27;FAILYR,PSTALP&#x27;. | [optional] 
 **agg_term_fields** | **str**| The field(s) for which aggregations will be counted for each unique term. | [optional] 
 **agg_sum_fields** | **str**| The field(s) for which aggregations will be summed or aggregated. | [optional] 
 **agg_limit** | **int**| The limit on how many aggregated results will be displayed | [optional] [default to 10]
 **format** | **str**| The format of the data to return. | [optional] 
 **download** | **str**| Whether the data should be downloaded as a file. | [optional] 
 **filename** | **str**| The filename to use when downloading data. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

