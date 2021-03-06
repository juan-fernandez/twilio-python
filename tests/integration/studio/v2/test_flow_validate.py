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


class FlowValidateTestCase(IntegrationTestCase):

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.studio.v2.flow_valid.update(friendly_name="friendly_name", status="draft", definition="definition")

        values = {'FriendlyName': "friendly_name", 'Status': "draft", 'Definition': "definition", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://studio.twilio.com/v2/Flows/Validate',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "valid": true
            }
            '''
        ))

        actual = self.client.studio.v2.flow_valid.update(friendly_name="friendly_name", status="draft", definition="definition")

        self.assertIsNotNone(actual)
