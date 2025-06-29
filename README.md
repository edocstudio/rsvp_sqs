# RSVP Online – Lambda SQS Consumer

This AWS Lambda function consumes RSVP registration messages from an Amazon SQS queue  
and sends confirmation emails to guests using Amazon SES.

---

## Features

- Consumes RSVP data from SQS
- Parses guest details, RSVP status
- Sends email (accept/decline) via SES, with Jinja2 templating

---

## AWS Lambda Integration

- **Event source:** SQS (serverless, decoupled event-driven)
- **Output:** Amazon SES (email confirmation)
- **Security:** Lambda IAM role only allows SQS read and SES send
- **Runtime:** Python 3.x (ARM64 Docker image)

---

## Usage

### Prerequisites

- AWS SQS queue with RSVP registration messages (JSON)
- Amazon SES set up with a verified sender email
- AWS Lambda (Python 3.x, custom container, arm64)

---

## Contact

Ittipon Bangudsareh\
[coversoul.bank@gmail.com](mailto:coversoul.bank@gmail.com)

---

## Demo

- **Demo**: [RSVP Online - AWSLambdaHackathon2025](https://youtu.be/1c4nMngYk-U)

---

## Related Repositories

This project is part of a complete serverless RSVP management system.  
See also:

- [Lambda API Request (Main Handler)](https://github.com/your-username/lambda-api-request) – Accepts and processes RSVP submissions
- [Lambda SQS Consumer (Email Notifier)](https://github.com/your-username/lambda-sqs-consumer) – Consumes messages from SQS and sends confirmation emails via SES

Both repositories work together as part of the same architecture and are required for end-to-end functionality.

---

**Contributions, feedback, and ideas are welcome!**
