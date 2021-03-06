# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class AuthCallsCredentialListMappingTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .sip \
                                 .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .auth \
                                 .calls \
                                 .credential_list_mappings.create(credential_list_sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {'CredentialListSid': "CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SIP/Domains/SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Auth/Calls/CredentialListMappings.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Thu, 30 Jul 2015 20:00:00 +0000",
                "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",
                "friendly_name": "friendly_name",
                "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .sip \
                                      .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .auth \
                                      .calls \
                                      .credential_list_mappings.create(credential_list_sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .sip \
                                 .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .auth \
                                 .calls \
                                 .credential_list_mappings.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SIP/Domains/SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Auth/Calls/CredentialListMappings.json',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Auth/Calls/CredentialListMappings.json?PageSize=50&Page=0",
                "end": 0,
                "previous_page_uri": null,
                "contents": [],
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Auth/Calls/CredentialListMappings.json?PageSize=50&Page=0",
                "page_size": 50,
                "start": 0,
                "next_page_uri": null,
                "page": 0
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .sip \
                                      .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .auth \
                                      .calls \
                                      .credential_list_mappings.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Auth/Calls/CredentialListMappings.json?PageSize=50&Page=0",
                "end": 0,
                "previous_page_uri": null,
                "contents": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Thu, 30 Jul 2015 20:00:00 +0000",
                        "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",
                        "friendly_name": "friendly_name",
                        "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/Domains/SDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Auth/Calls/CredentialListMappings.json?PageSize=50&Page=0",
                "page_size": 50,
                "start": 0,
                "next_page_uri": null,
                "page": 0
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .sip \
                                      .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .auth \
                                      .calls \
                                      .credential_list_mappings.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .sip \
                                 .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .auth \
                                 .calls \
                                 .credential_list_mappings(sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SIP/Domains/SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Auth/Calls/CredentialListMappings/CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Thu, 30 Jul 2015 20:00:00 +0000",
                "date_updated": "Thu, 30 Jul 2015 20:00:00 +0000",
                "friendly_name": "friendly_name",
                "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .sip \
                                      .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .auth \
                                      .calls \
                                      .credential_list_mappings(sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .sip \
                                 .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .auth \
                                 .calls \
                                 .credential_list_mappings(sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SIP/Domains/SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Auth/Calls/CredentialListMappings/CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .sip \
                                      .domains(sid="SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .auth \
                                      .calls \
                                      .credential_list_mappings(sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
