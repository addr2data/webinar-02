import boto3
import simplejson as json
import time



def main():
    client = boto3.client('sqs')

    while True:
        print("Receiving msg...")
        response = client.receive_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/649887181190/jobs',
            MaxNumberOfMessages=1,
        )
        if "Messages" in response:
            for msg in response['Messages']:
                print("Building configuration...")
                receipt = response['Messages'][0]['ReceiptHandle']

                for step in range(1, 11):
                    print(f"Performing step {step}")
                    time.sleep(3)

                print("Finalizing...")
                response = client.delete_message(
                    QueueUrl='https://sqs.us-east-1.amazonaws.com/649887181190/jobs',
                    ReceiptHandle=receipt
                )


if __name__ == "__main__":
    main()