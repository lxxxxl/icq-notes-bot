# coding: utf-8
from __future__ import unicode_literals

import json
import requests
import logging
import os
from time import sleep


logging.basicConfig(level=logging.INFO)

api_url = 'https://api.icq.net/bot/v1/'
access_token = os.environ['ICQ_ACCESS_TOKEN']
allowed_userids = os.environ['ICQ_ALLOWED_USERIDS'].split(',')

def api_request(api, params=None):
    """performs HTTP requset to API server
    returns server response as json object
    """
    url = '{}{}'.format(api_url, api)
    if params == None:
        params = dict()
    params['token'] = access_token
    response = requests.get(url, params=params)
    return json.loads(response.content)


def process_events(events):
    """processes all events in server response
    returns max event ID
    """
    max_event_id = -1

    for event in events['events']:
        if event['eventId'] > max_event_id:
            max_event_id = event['eventId']

        if 'newMessage' in event['type']:
            process_event_newMessage(event['payload'])
        else:
            logging.info('Unsupported event: %s', event['type'])
        # Other events are:
        #    editedMessage
        #    deletedMessage
        #    pinnedMessage
        #    unpinnedMessage
        #    newChatMembers
        #    leftChatMembers
        #    callbackQuery
    return max_event_id


def process_event_newMessage(payload):
    """precesses newMessage event"""
    if payload['from']['userId'] in allowed_userids:
        logging.info('newMessage: %s', payload['text'])

        # TODO save note somewhere

        # send response to user
        params = dict(
            chatId = payload['from']['userId'],
            text = 'Saved.'
        )
        api_request('/messages/sendText', params)
    else:
        logging.info('newMessage from unkown user: %s', payload['text'])

        # send response to user
        params = dict(
            chatId = payload['from']['userId'],
            text = 'I don\'t tnow you.'
        )
        api_request('/messages/sendText', params)


def main():
    last_known_event_id = 0
    while True:
        params = dict(
            lastEventId = last_known_event_id,
            pollTime = 60 * 5   # API server should hang connection for 5 mins
        )
        data = api_request('/events/get', params)

        if 'events' in data:
            event_id = process_events(data)
            if event_id != -1:
                last_known_event_id = event_id

main()
