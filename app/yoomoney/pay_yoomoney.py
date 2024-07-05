
import requests
import os
import logging

from dotenv import load_dotenv

load_dotenv()
YOOMONEY_TOKEN = os.getenv("YOOMONEY_TOKEN")
YOOMONEY_RECEIVER = os.getenv("YOOMONEY_ID")


def create_payment_link(amount, label, description):
    url = "https://yoomoney.ru/api/request-payment"
    headers = {
        "Authorization": f"Bearer {YOOMONEY_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "pattern_id": "p2p",
        "to": YOOMONEY_RECEIVER,
        "amount_due": amount,
        "comment": description,
        "message": description,
        "label": label
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.status_code != 200:
        logging.error(f"Error while requesting payment: {response.status_code} - {response.text}")
        return None

    try:
        response_data = response.json()
    except ValueError as e:
        logging.error(f"JSON decode error: {e} - {response.text}")
        return None
    
    if 'status' in response_data and response_data['status'] == 'success':
        request_id = response_data['request_id']
        process_url = f"https://yoomoney.ru/quickpay/confirm.xml?id={request_id}"
        return process_url
    else:
        logging.error(f"Error while requesting payment: {response_data}")
        return None
