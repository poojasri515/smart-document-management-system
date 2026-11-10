AWS PROJECT EVIDENCE
Project: Cloud-Based Smart Document Management System
Core services: Amazon S3, AWS Lambda, Amazon SNS
Supporting monitoring: Amazon CloudWatch

Screenshots:
01 - S3 bucket and uploaded objects
02 - SNS topic and confirmed email subscription
03 - SNS subscription details
04 - Lambda function overview and test page
05 - Lambda function code
06 - S3 trigger configured on Lambda (ObjectCreated events)
07 - Lambda test invocation succeeded (test event)
08 - Email notification received
09 - CloudWatch log group details
10 - Lambda function overview

Important evidence note:
The Lambda test success screenshot proves that the function's test-event execution returned success.
The trigger configuration screenshot proves that an S3 ObjectCreated trigger was configured.
For a fully demonstrated end-to-end S3-triggered run, add a fresh screenshot showing:
(1) a newly uploaded file in S3, (2) a corresponding Lambda invocation in CloudWatch Logs,
and (3) the matching email notification. Do not describe the simulated Lambda test alone
as proof that a real S3 event triggered the function.

Not included:
- Duplicate S3 bucket screenshot
- Duplicate email screenshot with browser popup
- AWS Academy README/session-status/console-home screenshots (not project implementation evidence)
