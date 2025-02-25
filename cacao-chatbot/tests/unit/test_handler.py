import json
import pytest

from PinpointSNSHandler import lambda_handler

@pytest.fixture()
def event():
    

    return { "Records": [
            {
                "EventSource": "aws:sns",
                "EventVersion": "1.0",
                "EventSubscriptionArn": "arn:aws:sns:us-west-2: 285396213403:LexPinpointIntegration: 9d821c3f-e2f4-4ed8-81ae-e23178217fd3",
                "Sns": {
                    "Type": "Notification",
                    "MessageId": "cc69fbbe-c77d-5f92-a525-a1258d639e7f",
                    "TopicArn": "arn:aws:sns:us-west-2: 285396213403:LexPinpointIntegration",
                    "Subject": "None",
                    "Message": {
                        "originationNumber": "+18052152660",
                        "destinationNumber": "+18559365255",
                        "messageKeyword": "KEYWORD_285396213403",
                        "messageBody": "Book an appointment",
                        "inboundMessageId": "574c3b68-86af-4525-964b-b63d0fd51945"
                    },
                    "Timestamp": "2022-03-03T22: 57: 34.298Z",
                    "SignatureVersion": "1",
                    "Signature": "WmisGtSCqRCYY4naXXzIYBLeu5iLmm5EZZBHnFju5lPhOK2e22qq4xKWcGdo6HejqUK4vZNMzCPYHPljTbp6ONpO1B31e5ZH1i0YYXKQtRPk31QrLlXlgzRwNDPV6VbH2OhY9OEIaZx/r8CB2FDTKafAVp+b5mERwpASSTKfkBO9jUHi367XA6JXWZOmZawAN6/W9HNpLK1PnPI7iXBEb5TyZWtwjxZ4gpRbfQIFCP6v1h/h2pzrndsHU5xMSbNdLFcsftvKir9Rks4fHM8AkShrNqkOyIuEHhQfdTBeLBPPyl5Df6uPGJq+M+ZAJyMx+blymlB2sn/hvJ/Zhn9qTw==",
                    "SigningCertUrl": "https: //sns.us-west-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                    "UnsubscribeUrl": "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:285396213403:ÎLexPinpointIntegration:9d821c3f-e2f4-4ed8-81ae-e23178217fd3",
                    "MessageAttributes": {}
                }
            }
        ]       
    }


def test_lambda_handler(event, mocker):

    ret = lambda_handler.lambda_handler(event, "")
    data = json.loads(ret["body"])

   
