from requests
from json

def send_fcm_notification(ids, title, body):
    """
    :param ids: fcm push notification target, identification value of the target is the push key.
    :param title: fcm push notification title
    :param body: fcm push notification content
    """
    url = 'https://fcm.googleapis.com/fcm/send'

    headers = {
        'Authorization': 'key={}'.format('your cloud messeging server key in firebase app'),
        'Content-Type': 'application/json; UTF-8',
    }

    content = {
        'registration_ids': ids,
        'notification': {
            'title': title,
            'body': body
        }
    }

    requests.post(url, data=json.dumps(content), headers=headers)
