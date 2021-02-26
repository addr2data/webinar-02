import boto3
import simplejson as json
import time



def main():
    client = boto3.client('sqs')

    msg = {'msgType': 'test',
           'msgId': ""}

    # Add ten messages to queue
    for msg_num in range(1, 11):
        msg['msgId'] = f"m-{msg_num}"

        response = client.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/649887181190/test',
            MessageBody='{"type": "test2"}'
        )
        print(json.dumps(response, indent=4, sort_keys=False))
        """

if __name__ == "__main__":
    main()
