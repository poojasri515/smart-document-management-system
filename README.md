
# Cloud-Based Smart Document Management System

## Project Overview
The Cloud-Based Smart Document Management System is a serverless cloud application that stores documents in Amazon S3 and automatically sends email notifications whenever a new document is uploaded.

## Problem Statement
Managing uploaded documents manually and tracking new uploads can be difficult. This project automates document upload notifications using AWS cloud services.

## Objectives
- Store documents securely in Amazon S3.
- Detect new document uploads automatically.
- Process upload events using AWS Lambda.
- Send email notifications using Amazon SNS.
- Monitor execution through Amazon CloudWatch.

## AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Stores uploaded documents |
| AWS Lambda | Processes S3 upload events |
| Amazon SNS | Sends email notifications |
| Amazon CloudWatch | Monitors Lambda execution logs |

## System Architecture

1. User uploads a document to Amazon S3.
2. S3 generates an ObjectCreated event.
3. AWS Lambda is automatically triggered.
4. Lambda extracts the bucket name and uploaded file name.
5. Lambda publishes a notification to Amazon SNS.
6. SNS sends an email notification to the subscribed email address.
7. CloudWatch stores Lambda execution logs.

## Implementation
- Created an S3 bucket named `smartdocvault2026pooja`.
- Created an SNS topic named `DocumentUploadNotifications`.
- Configured an email subscription.
- Developed a Python Lambda function named `document-upload-processor`.
- Configured an S3 ObjectCreated event trigger.
- Integrated Lambda with SNS using the SNS topic ARN.

## Testing and Results
The system was tested by uploading a text file named `Hi.txt` to the S3 bucket.

The Lambda function processed the upload event and Amazon SNS delivered an email notification.

**Result:** Successful email notification received after document upload.

## Conclusion
The project demonstrates an automated, serverless document notification workflow using AWS cloud services. It reduces manual monitoring and provides immediate email notifications when new documents are uploaded.

## Technologies
- AWS Cloud
- Python
- Boto3
- Amazon S3
- AWS Lambda
- Amazon SNS
- Amazon CloudWatch

## GitHub Repository
https://github.com/poojasri515/smart-document-management-system
