from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = '12345678910'  # Replace with a secure key

# AWS SQS setup
sqs = boto3.client(
    'sqs',
    region_name=os.getenv('AWS_REGION'),  # Change as needed
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
QUEUE_URL = os.getenv('SQS_QUEUE_URL')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produce', methods=['GET', 'POST'])
def produce():
    if request.method == 'POST':
        message = request.form.get('message')
        print(f"Sending message: {message}")
        if message:
            sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=message)
            flash('Message sent!')
            return redirect(url_for('produce'))
    return render_template('producer.html')

@app.route('/consume')
def consume():
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=2
    )
    messages = response.get('Messages', [])
    print(messages)
    return render_template('consumer.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)