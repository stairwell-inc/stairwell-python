# coding: utf-8

"""
    Stairwell V1 HTTP APIs

    Restful APIs for the Stairwell platform. Most APIs expose named resources: each resource has a unique identifier that users use to reference that resource, and these names are what users should store as the canonical names for the resources. The base URL for this API is https://app.stairwell.com

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stairwell_openapi_client.api.threat_reports_api import ThreatReportsApi  # noqa: E501


class TestThreatReportsApi(unittest.TestCase):
    """ThreatReportsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ThreatReportsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_threat_reports_create_threat_report(self) -> None:
        """Test case for threat_reports_create_threat_report

        CreateThreatReport  # noqa: E501
        """
        pass

    def test_threat_reports_delete_threat_report(self) -> None:
        """Test case for threat_reports_delete_threat_report

        DeleteThreatReport  # noqa: E501
        """
        pass

    def test_threat_reports_list_threat_report_iocs(self) -> None:
        """Test case for threat_reports_list_threat_report_iocs

        ListThreatReportIocs  # noqa: E501
        """
        pass

    def test_threat_reports_list_threat_report_matches(self) -> None:
        """Test case for threat_reports_list_threat_report_matches

        ListThreatReportMatches  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
