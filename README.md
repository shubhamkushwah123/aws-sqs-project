# Amazon SQS Flask POC App

This is a simple proof-of-concept web application built with Flask that demonstrates how to send and receive messages using Amazon Simple Queue Service (SQS).

## Features

- **Producer UI:** Send messages to an SQS queue via a web form.
- **Consumer UI:** View messages received from the SQS queue.
- **Secure credentials:** Uses a `.env` file for AWS credentials and queue configuration.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd aws-sqs
   ```

2. **Create a `.env` file in the project root:**
   ```
   AWS_ACCESS_KEY_ID=your_aws_access_key_id
   AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
   AWS_REGION=your_aws_region
   SQS_QUEUE_URL=https://sqs.<region>.amazonaws.com/<account-id>/<queue-name>
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

5. **Access the web UIs:**
   - Producer: [http://localhost:5000/produce](http://localhost:5000/produce)
   - Consumer: [http://localhost:5000/consume](http://localhost:5000/consume)

## Notes

- **Do not commit your `.env` file.** It contains sensitive credentials.
- Make sure your AWS credentials have permission to access SQS.
- The app uses the region and queue URL specified in your `.env` file.

## License

MIT License