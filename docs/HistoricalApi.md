# swagger_client.HistoricalApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_historical**](HistoricalApi.md#get_historical) | **GET** /summary | Get Historical Aggregate Data by Year

# **get_historical**
> object get_historical(filters=filters, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, agg_by=agg_by, agg_term_fields=agg_term_fields, agg_sum_fields=agg_sum_fields, agg_limit=agg_limit, format=format, download=download, filename=filename)

Get Historical Aggregate Data by Year

Returns aggregate financial and structure data, subtotaled by year, regarding finanical institutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HistoricalApi()
filters = 'filters_example' # str | The filter criteria that refines the records included in the calculated result. example: >- STNAME:\"Alabama\" AND YEAR:2005 Examples: * Filter by Community Banks (CB) vs. Savings Institutions (SI)   `CB_SI:CB`   * Filter by State name   `STNAME:\"Virginia\"`     * Filter for any one of multiple State names   `STNAME:(\"West Virginia\",\"Delaware\")`     * Filter data by the year range   `YEAR:[\"2015\" TO \"2017\"]`  (optional)
fields = 'fields_example' # str | Comma delimited list of fields with aggregated annual financial data to return. (optional)
sort_by = 'YEAR' # str | Field name by which to sort returned data (optional) (default to YEAR)
sort_order = 'ASC' # str | Indicator if ascending (ASC) or descending (DESC) (optional) (default to ASC)
limit = 10 # int | The number of records to return. Default is 10 and maximum is 10,000. (optional) (default to 10)
offset = 0 # int | The offset of page to return. (optional) (default to 0)
agg_by = 'agg_by_example' # str | The field(s) by which data will be aggregated. Valid values are 'YEAR' or 'YEAR,STNAME'. (optional)
agg_term_fields = 'agg_term_fields_example' # str | The field(s) for which aggregations will be counted for each unique term. (optional)
agg_sum_fields = 'agg_sum_fields_example' # str | The field(s) for which aggregations will be summed or aggregated. (optional)
agg_limit = 56 # int | The limit on how many aggregated results will be displayed (optional)
format = 'format_example' # str | The format of the data to return. (optional)
download = 'download_example' # str | Whether the data should be downloaded as a file. (optional)
filename = 'filename_example' # str | The filename to use when downloading data. (optional)

try:
    # Get Historical Aggregate Data by Year
    api_response = api_instance.get_historical(filters=filters, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, agg_by=agg_by, agg_term_fields=agg_term_fields, agg_sum_fields=agg_sum_fields, agg_limit=agg_limit, format=format, download=download, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoricalApi->get_historical: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| The filter criteria that refines the records included in the calculated result. example: &gt;- STNAME:\&quot;Alabama\&quot; AND YEAR:2005 Examples: * Filter by Community Banks (CB) vs. Savings Institutions (SI)   &#x60;CB_SI:CB&#x60;   * Filter by State name   &#x60;STNAME:\&quot;Virginia\&quot;&#x60;     * Filter for any one of multiple State names   &#x60;STNAME:(\&quot;West Virginia\&quot;,\&quot;Delaware\&quot;)&#x60;     * Filter data by the year range   &#x60;YEAR:[\&quot;2015\&quot; TO \&quot;2017\&quot;]&#x60;  | [optional] 
 **fields** | **str**| Comma delimited list of fields with aggregated annual financial data to return. | [optional] 
 **sort_by** | **str**| Field name by which to sort returned data | [optional] [default to YEAR]
 **sort_order** | **str**| Indicator if ascending (ASC) or descending (DESC) | [optional] [default to ASC]
 **limit** | **int**| The number of records to return. Default is 10 and maximum is 10,000. | [optional] [default to 10]
 **offset** | **int**| The offset of page to return. | [optional] [default to 0]
 **agg_by** | **str**| The field(s) by which data will be aggregated. Valid values are &#x27;YEAR&#x27; or &#x27;YEAR,STNAME&#x27;. | [optional] 
 **agg_term_fields** | **str**| The field(s) for which aggregations will be counted for each unique term. | [optional] 
 **agg_sum_fields** | **str**| The field(s) for which aggregations will be summed or aggregated. | [optional] 
 **agg_limit** | **int**| The limit on how many aggregated results will be displayed | [optional] 
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

