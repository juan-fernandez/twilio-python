# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class MessageTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .messages(sid="IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Hello",
                "attributes": "{}",
                "author": "system",
                "date_created": "2016-03-24T20:37:57Z",
                "date_updated": "2016-03-24T20:37:57Z",
                "index": 0,
                "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .messages(sid="IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .messages.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Hello",
                "attributes": "{ \\"foo\\": \\"bar\\" }",
                "author": "message author",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "index": 0,
                "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .messages.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .messages(sid="IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "session_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Hello",
                "attributes": "{ \\"foo\\": \\"bar\\" }",
                "author": "message author",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "index": 0,
                "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .messages(sid="IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .messages.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "messages"
                },
                "messages": [
                    {
                        "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "session_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "body": "Hello",
                        "attributes": "{}",
                        "author": "system",
                        "date_created": "2016-03-24T20:37:57Z",
                        "date_updated": "2016-03-24T20:37:57Z",
                        "index": 0,
                        "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "session_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "body": "Hello",
                        "attributes": "{}",
                        "author": "system",
                        "date_created": "2016-03-24T20:37:57Z",
                        "date_updated": "2016-03-24T20:37:57Z",
                        "index": 0,
                        "url": "https://messaging.twilio.com/v1/Sessions/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .messages.list()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .messages(sid="IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://messaging.twilio.com/v1/Sessions/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.messaging.v1.sessions(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .messages(sid="IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
