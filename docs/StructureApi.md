# swagger_client.StructureApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_institutions**](StructureApi.md#search_institutions) | **GET** /institutions | Get Financial Institutions
[**search_locations**](StructureApi.md#search_locations) | **GET** /locations | Get Institution Locations

# **search_institutions**
> object search_institutions(filters=filters, search=search, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, format=format, download=download, filename=filename)

Get Financial Institutions

Returns a list of financial institutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructureApi()
filters = 'filters_example' # str | The filter for the bank search. Examples: * Filter by State name   `STNAME:\"West Virginia\"`     * Filter for any one of multiple State names   `STNAME:(\"West Virginia\",\"Delaware\")`     * Filter by last updated within an inclusive date range   `DATEUPDT:[\"2010-01-01\" TO \"2010-12-31\"]` * Filter for deposits over 50,000,000 (50000 thousands of dollars)   `DEP:[50000 TO *]`  (optional)
search = 'search_example' # str | Flexible text search against institution records - currently only supporting name search.  Search supports text search and fuzzy matching, as opposed to filters that are exact matches. Examples: * Search by name `NAME: Island` * Search by name (fuzzy match) `NAME: Iland`  (optional)
fields = 'fields_example' # str | Comma delimited list of fields to search. (optional)
sort_by = 'NAME' # str | Field name by which to sort returned data (optional) (default to NAME)
sort_order = 'ASC' # str | Indicator if ascending (ASC) or descending (DESC) (optional) (default to ASC)
limit = 10 # int | The number of records to return. Default is 10 and maximum is 10,000. (optional) (default to 10)
offset = 0 # int | The offset of page to return. (optional) (default to 0)
format = 'format_example' # str | The format of the data to return. (optional)
download = 'download_example' # str | Whether the data should be downloaded as a file. (optional)
filename = 'filename_example' # str | The filename to use when downloading data. (optional)

try:
    # Get Financial Institutions
    api_response = api_instance.search_institutions(filters=filters, search=search, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, format=format, download=download, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructureApi->search_institutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| The filter for the bank search. Examples: * Filter by State name   &#x60;STNAME:\&quot;West Virginia\&quot;&#x60;     * Filter for any one of multiple State names   &#x60;STNAME:(\&quot;West Virginia\&quot;,\&quot;Delaware\&quot;)&#x60;     * Filter by last updated within an inclusive date range   &#x60;DATEUPDT:[\&quot;2010-01-01\&quot; TO \&quot;2010-12-31\&quot;]&#x60; * Filter for deposits over 50,000,000 (50000 thousands of dollars)   &#x60;DEP:[50000 TO *]&#x60;  | [optional] 
 **search** | **str**| Flexible text search against institution records - currently only supporting name search.  Search supports text search and fuzzy matching, as opposed to filters that are exact matches. Examples: * Search by name &#x60;NAME: Island&#x60; * Search by name (fuzzy match) &#x60;NAME: Iland&#x60;  | [optional] 
 **fields** | **str**| Comma delimited list of fields to search. | [optional] 
 **sort_by** | **str**| Field name by which to sort returned data | [optional] [default to NAME]
 **sort_order** | **str**| Indicator if ascending (ASC) or descending (DESC) | [optional] [default to ASC]
 **limit** | **int**| The number of records to return. Default is 10 and maximum is 10,000. | [optional] [default to 10]
 **offset** | **int**| The offset of page to return. | [optional] [default to 0]
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

# **search_locations**
> object search_locations(filters=filters, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, format=format, download=download, filename=filename)

Get Institution Locations

Returns locations/branches of financial institutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StructureApi()
filters = 'filters_example' # str | The filter for the location search. (optional)
fields = 'fields_example' # str | Comma delimited list of fields to return. (optional)
sort_by = 'NAME' # str | Field name by which to sort returned data (optional) (default to NAME)
sort_order = 'ASC' # str | Indicator if ascending (ASC) or descending (DESC) (optional) (default to ASC)
limit = 10 # int | The number of records to return. Default is 10 and maximum is 10,000. (optional) (default to 10)
offset = 0 # int | The offset of page to return. (optional) (default to 0)
format = 'format_example' # str | The format of the data to return. (optional)
download = 'download_example' # str | Whether the data should be downloaded as a file. (optional)
filename = 'filename_example' # str | The filename to use when downloading data. (optional)

try:
    # Get Institution Locations
    api_response = api_instance.search_locations(filters=filters, fields=fields, sort_by=sort_by, sort_order=sort_order, limit=limit, offset=offset, format=format, download=download, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructureApi->search_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| The filter for the location search. | [optional] 
 **fields** | **str**| Comma delimited list of fields to return. | [optional] 
 **sort_by** | **str**| Field name by which to sort returned data | [optional] [default to NAME]
 **sort_order** | **str**| Indicator if ascending (ASC) or descending (DESC) | [optional] [default to ASC]
 **limit** | **int**| The number of records to return. Default is 10 and maximum is 10,000. | [optional] [default to 10]
 **offset** | **int**| The offset of page to return. | [optional] [default to 0]
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

