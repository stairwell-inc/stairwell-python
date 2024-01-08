# coding: utf-8

"""
    Stairwell V1 HTTP APIs

    Restful APIs for the Stairwell platform. Most APIs expose named resources: each resource has a unique identifier that users use to reference that resource, and these names are what users should store as the canonical names for the resources. The base URL for this API is https://app.stairwell.com

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from stairwell_openapi_client.models.object_signature import ObjectSignature  # noqa: E501

class TestObjectSignature(unittest.TestCase):
    """ObjectSignature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectSignature:
        """Test ObjectSignature
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectSignature`
        """
        model = ObjectSignature()  # noqa: E501
        if include_optional:
            return ObjectSignature(
                x509_certificates = [
                    stairwell_openapi_client.models.x509_certificate.X509Certificate(
                        signature = '', 
                        issuer = '', 
                        subject = '', 
                        earliest_valid_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        latest_valid_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                pkcs7_verification_result = 'PKCS7_VERIFICATION_RESULT_UNSPECIFIED'
            )
        else:
            return ObjectSignature(
        )
        """

    def testObjectSignature(self):
        """Test ObjectSignature"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()