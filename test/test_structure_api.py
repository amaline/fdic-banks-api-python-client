# coding: utf-8

"""
    FDIC Bank Data API (Beta)

    API to serve banking industry data to the public.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: PublicDataFeedback@fdic.gov
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.structure_api import StructureApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStructureApi(unittest.TestCase):
    """StructureApi unit test stubs"""

    def setUp(self):
        self.api = api.structure_api.StructureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_institutions(self):
        """Test case for search_institutions

        Get Financial Institutions  # noqa: E501
        """
        pass

    def test_search_locations(self):
        """Test case for search_locations

        Get Institution Locations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()