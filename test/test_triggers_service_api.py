# coding: utf-8

"""
    Stairwell V1 HTTP APIs

    Restful APIs for the Stairwell platform. Most APIs expose named resources: each resource has a unique identifier that users use to reference that resource, and these names are what users should store as the canonical names for the resources. The base URL for this API is https://app.stairwell.com

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stairwell_openapi_client.api.triggers_service_api import TriggersServiceApi  # noqa: E501


class TestTriggersServiceApi(unittest.TestCase):
    """TriggersServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TriggersServiceApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_triggers_service_list_trigger_matches(self) -> None:
        """Test case for triggers_service_list_trigger_matches

        ListTriggerMatches  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
